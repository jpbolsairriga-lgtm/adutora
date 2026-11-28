/**
 * Protocolo de Projetos — Bolsa Irriga
 * Planilha online: numeração única de protocolos + histórico de revisões.
 *
 * NÚMERO:  CÓDIGO-AAMM-SEQ   ex.: JP-2611-07
 *          CÓDIGO = código do consultor (aba Consultores) · AAMM = ano/mês · SEQ = sequência do consultor no mês
 * REVISÃO: alterações reenviadas mantêm o número e ganham revisão: JP-2611-07 R1, R2…
 *
 * ARMAZENAMENTO (v2):
 *  - A planilha guarda só o ÍNDICE (uma linha leve por revisão) → continua rápida com o passar dos anos.
 *  - Cada revisão vira um arquivo compactado na pasta "Dados" (ao lado da planilha): "JP-2611-07 R1.json.gz".
 *  - Backup automático semanal da planilha na pasta "Backups" (mantém as 12 últimas cópias).
 *  - Protocolos salvos no formato antigo (JSON dentro da planilha) são migrados sozinhos para arquivos.
 *
 * INSTALAÇÃO / ATUALIZAÇÃO (pelo gestor):
 *  1. Extensões → Apps Script na planilha. Apague o conteúdo e cole ESTE arquivo inteiro. SALVE (Ctrl+S).
 *  2. Escolha a função "configurar" e clique em Executar → autorize (inclui acesso ao Drive para criar os arquivos).
 *     Cria/atualiza as abas, as pastas Dados e Backups, migra o formato antigo e liga o backup semanal.
 *  3. Na aba Consultores: Nome, Código (2 letras, único), PIN (4 a 6 dígitos), Ativo (Sim/Não).
 *  4. 1ª vez: Implementar → Nova implementação → App da Web (Executar como: Eu · Quem tem acesso: Qualquer pessoa).
 *     Atualização: Implementar → Gerir implementações → lápis (editar) → Versão: "Nova versão" → Implementar.
 *     (a URL /exec continua a mesma)
 */
const ABA_P = 'Protocolos', ABA_C = 'Consultores';
const CAB_P = ['Número','Revisão','Número completo','Consultor','Código','Cliente','Propriedade','Município','Área (ha)','Tipo','Data do protocolo','Salvo em','Hash','Arquivo (ID)','Arquivo (link)'];
const CAB_C = ['Nome','Código','PIN','Ativo','E-mail'];
const COL_ARQ = 14;            // coluna N
const N_INDICE = 13;           // colunas A..M = índice
const MANTER_BACKUPS = 12;

/* planilha usada: a do próprio script (Extensões → Apps Script) ou, se o script foi criado solto,
   uma planilha "Protocolos Bolsa Irriga" criada automaticamente no seu Drive. */
function planilha(){
  const a = SpreadsheetApp.getActive(); if(a) return a;
  const props = PropertiesService.getScriptProperties(), id = props.getProperty('PLANILHA_ID');
  if(id){ try{ return SpreadsheetApp.openById(id); }catch(e){} }
  const ss = SpreadsheetApp.create('Protocolos Bolsa Irriga'); props.setProperty('PLANILHA_ID', ss.getId()); return ss;
}
/* pastas "Dados" e "Backups" ficam na mesma pasta da planilha */
function pastaBase(){
  const it = DriveApp.getFileById(planilha().getId()).getParents();
  return it.hasNext() ? it.next() : DriveApp.getRootFolder();
}
function subpasta(nome){
  const props = PropertiesService.getScriptProperties(), k = 'PASTA_' + nome, id = props.getProperty(k);
  if(id){ try{ const f = DriveApp.getFolderById(id); if(!f.isTrashed()) return f; }catch(e){} }
  const base = pastaBase(), it = base.getFoldersByName(nome);
  const f = it.hasNext() ? it.next() : base.createFolder(nome);
  props.setProperty(k, f.getId()); return f;
}

/* ---------- configuração (rodar manualmente uma vez, e a cada atualização do script) ---------- */
function configurar(){
  garantirAbas();
  subpasta('Dados'); subpasta('Backups');
  instalarBackup();
  backupSemanal();
  Logger.log('Planilha pronta: ' + planilha().getUrl());
  Logger.log('Arquivos dos protocolos: ' + subpasta('Dados').getUrl());
  Logger.log('Backups semanais: ' + subpasta('Backups').getUrl());
}
function garantirAbas(){
  const ss = planilha();
  let c = ss.getSheetByName(ABA_C);
  if(!c) c = ss.insertSheet(ABA_C);
  if(c.getLastRow() === 0){
    c.getRange('A:E').setNumberFormat('@');
    c.appendRow(CAB_C); c.appendRow(['Nome do Consultor','JP','1234','Sim','']); c.setFrozenRows(1);
  }
  let p = ss.getSheetByName(ABA_P);
  if(!p) p = ss.insertSheet(ABA_P);
  if(p.getLastRow() === 0){
    p.getRange('A:O').setNumberFormat('@');
    p.appendRow(CAB_P); p.setFrozenRows(1);
  } else if(p.getRange(1, COL_ARQ).getDisplayValue() !== CAB_P[COL_ARQ-1]){
    migrar(p);                                   // formato antigo → arquivos
  }
}
/* move o JSON que ficava nas colunas N, O, P… para arquivos .json.gz e deixa só o ID/link */
function migrar(sh){
  const n = sh.getLastRow(), lc = Math.max(sh.getLastColumn(), COL_ARQ+1);
  if(n >= 2){
    const vals = sh.getRange(2, 1, n-1, lc).getValues();
    vals.forEach((r, i) => {
      const json = r.slice(COL_ARQ-1).map(String).join('');
      if(!json || json.charAt(0) !== '{') return;
      const f = gravarArquivo(String(r[2] || r[0]), json, 'json');
      sh.getRange(i+2, COL_ARQ, 1, lc-COL_ARQ+1).clearContent();
      sh.getRange(i+2, COL_ARQ, 1, 2).setValues([[f.getId(), f.getUrl()]]);
    });
  }
  sh.getRange(1, 1, 1, CAB_P.length).setValues([CAB_P]);
}
function gravarArquivo(nome, dados, fmt){
  const pasta = subpasta('Dados'), arq = nome + '.json.gz';
  const blob = fmt === 'gz64'
    ? Utilities.newBlob(Utilities.base64Decode(dados), 'application/gzip', arq)
    : Utilities.gzip(Utilities.newBlob(dados, 'application/json', nome + '.json'), arq);
  return pasta.createFile(blob);
}

/* ---------- backup semanal da planilha (segunda-feira, 3h) ---------- */
function backupSemanal(){
  const ss = planilha(), pasta = subpasta('Backups');
  const nome = ss.getName() + ' - backup ' + Utilities.formatDate(new Date(), Session.getScriptTimeZone(), 'yyyy-MM-dd');
  DriveApp.getFileById(ss.getId()).makeCopy(nome, pasta);
  const lista = [], it = pasta.getFiles();
  while(it.hasNext()){ const f = it.next(); if(f.getName().indexOf(' - backup ') > 0) lista.push(f); }
  lista.sort((a, b) => b.getDateCreated() - a.getDateCreated());
  lista.slice(MANTER_BACKUPS).forEach(f => f.setTrashed(true));
}
function instalarBackup(){
  ScriptApp.getProjectTriggers().forEach(t => { if(t.getHandlerFunction() === 'backupSemanal') ScriptApp.deleteTrigger(t); });
  ScriptApp.newTrigger('backupSemanal').timeBased().everyWeeks(1).onWeekDay(ScriptApp.WeekDay.MONDAY).atHour(3).create();
}

/* ---------- API do app ---------- */
function doGet(e){ return saida(rotear((e && e.parameter) || {})); }
function doPost(e){ let p = {}; try{ p = JSON.parse(e.postData.contents); }catch(err){} return saida(rotear(p)); }
function saida(o){ return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }

function rotear(p){
  try{
    garantirAbas();
    switch(p.acao){
      case 'consultores': return {ok:true, versao:2, consultores: consultores().filter(c=>c.ativo).map(c=>({nome:c.nome, codigo:c.codigo}))};
      case 'lista':  autenticar(p); return {ok:true, protocolos: listar(cod(p))};
      case 'abrir':  autenticar(p); return abrir(cod(p), String(p.numero||'').trim(), String(p.gz||'') === '1');
      case 'salvar': autenticar(p); return salvar(p);
    }
    return {ok:false, erro:'Ação inválida'};
  }catch(err){ return {ok:false, erro: String((err && err.message) || err)}; }
}
function cod(p){ return String(p.codigo||'').trim().toUpperCase(); }

function consultores(){
  const sh = planilha().getSheetByName(ABA_C);
  return sh.getDataRange().getDisplayValues().slice(1)
    .filter(r => r[0] && r[1])
    .map(r => ({nome:String(r[0]).trim(), codigo:String(r[1]).trim().toUpperCase(), pin:String(r[2]).trim(), ativo:!/^n/i.test(String(r[3]||'Sim').trim())}));
}
function autenticar(p){
  const c = consultores().find(x => x.codigo === cod(p));
  if(!c || !c.ativo) throw new Error('Consultor não cadastrado ou inativo na planilha');
  if(!c.pin || c.pin !== String(p.pin||'').trim()) throw new Error('PIN inválido');
  return c;
}
function linhas(){
  const sh = planilha().getSheetByName(ABA_P);
  const n = sh.getLastRow(); if(n < 2) return [];
  return sh.getRange(2, 1, n-1, N_INDICE).getDisplayValues().map((r,i) => ({
    row:i+2, numero:r[0], rev:Number(r[1])||0, completo:r[2], consultor:r[3], codigo:r[4], cliente:r[5], propriedade:r[6],
    municipio:r[7], area:r[8], tipo:r[9], data:r[10], salvo:r[11], hash:r[12]}));
}
function ultimaRevisao(L, numero){
  return L.filter(l => l.numero === numero).reduce((a,b) => (!a || b.rev > a.rev) ? b : a, null);
}
function listar(codigo){
  const m = {};
  linhas().filter(l => l.codigo === codigo).forEach(l => { if(!m[l.numero] || l.rev > m[l.numero].rev) m[l.numero] = l; });
  return Object.keys(m).map(k => m[k]).sort((a,b) => String(b.salvo).localeCompare(String(a.salvo)))
    .map(l => ({numero:l.numero, rev:l.rev, cliente:l.cliente, propriedade:l.propriedade, municipio:l.municipio, area:l.area, tipo:l.tipo, data:l.data, salvo:l.salvo}));
}
function abrir(codigo, numero, aceitaGz){
  const u = ultimaRevisao(linhas(), numero);
  if(!u) throw new Error('Protocolo ' + numero + ' não encontrado');
  if(u.codigo !== codigo) throw new Error('Este protocolo pertence a outro consultor');
  const sh = planilha().getSheetByName(ABA_P);
  const arq = String(sh.getRange(u.row, COL_ARQ).getDisplayValue() || '');
  if(arq && arq.charAt(0) !== '{'){
    const blob = DriveApp.getFileById(arq).getBlob();
    if(aceitaGz) return {ok:true, numero:u.numero, rev:u.rev, fmt:'gz64', dados:Utilities.base64Encode(blob.getBytes())};
    return {ok:true, numero:u.numero, rev:u.rev, fmt:'json', dados:Utilities.ungzip(blob.setContentType('application/x-gzip')).getDataAsString('UTF-8')};
  }
  const lc = Math.max(sh.getLastColumn(), COL_ARQ);                      // formato antigo ainda não migrado
  const dados = sh.getRange(u.row, COL_ARQ, 1, lc-COL_ARQ+1).getValues()[0].map(String).join('');
  return {ok:true, numero:u.numero, rev:u.rev, fmt:'json', dados:dados};
}
function salvar(p){
  const lock = LockService.getScriptLock(); lock.waitLock(30000);   // evita número duplicado em envios simultâneos
  try{
    const sh = planilha().getSheetByName(ABA_P), tz = Session.getScriptTimeZone(), L = linhas(), codigo = cod(p);
    let numero = String(p.numero||'').trim(), rev = 0;
    if(numero){
      const u = ultimaRevisao(L, numero);
      if(!u) throw new Error('Protocolo ' + numero + ' não encontrado na planilha');
      if(u.codigo !== codigo) throw new Error('Este protocolo pertence a outro consultor');
      if(u.hash && u.hash === p.hash) return {ok:true, numero:numero, rev:u.rev, igual:true};
      rev = u.rev + 1;
    } else {
      const pref = codigo + '-' + Utilities.formatDate(new Date(), tz, 'yyMM') + '-';
      let max = 0;
      L.forEach(l => { if(l.numero.indexOf(pref) === 0){ const s = parseInt(l.numero.slice(pref.length), 10); if(s > max) max = s; } });
      const seq = String(max + 1); numero = pref + (seq.length < 2 ? '0' + seq : seq);
    }
    const completo = numero + (rev ? ' R' + rev : '');
    const f = gravarArquivo(completo, String(p.dados || ''), p.fmt === 'gz64' ? 'gz64' : 'json');
    const r = p.resumo || {};
    sh.appendRow([numero, String(rev), completo, r.consultor||'', codigo, r.cliente||'', r.propriedade||'',
      r.municipio||'', String(r.area||''), r.tipo||'', r.data||'', Utilities.formatDate(new Date(), tz, 'yyyy-MM-dd HH:mm:ss'), p.hash||'',
      f.getId(), f.getUrl()]);
    return {ok:true, numero:numero, rev:rev};
  } finally { lock.releaseLock(); }
}
