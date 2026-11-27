/**
 * Protocolo de Projetos — Bolsa Irriga
 * Planilha online: numeração única de protocolos + histórico de revisões.
 *
 * NÚMERO:  CÓDIGO-AAMM-SEQ   ex.: JP-2611-07
 *          CÓDIGO = código do consultor (aba Consultores) · AAMM = ano/mês · SEQ = sequência do consultor no mês
 * REVISÃO: alterações reenviadas mantêm o número e ganham revisão: JP-2611-07 R1, R2…
 *
 * INSTALAÇÃO (uma vez só, pelo gestor):
 *  1. Crie uma planilha Google nova (ex.: "Protocolos Bolsa Irriga").
 *  2. Menu Extensões → Apps Script. Apague o conteúdo e cole ESTE arquivo inteiro. Salve.
 *  3. SALVE (Ctrl+S). Depois escolha a função "configurar" e clique em Executar (autorize o acesso à planilha).
 *     Se o script foi criado solto (fora da planilha), ele cria a planilha "Protocolos Bolsa Irriga" no seu Drive.
 *     → cria as abas "Protocolos" e "Consultores".
 *  4. Na aba Consultores, cadastre cada consultor: Nome, Código (2 letras, único), PIN (4 a 6 dígitos), Ativo (Sim/Não).
 *  5. Implantar → Nova implantação → tipo "App da Web":
 *       Executar como: Eu  ·  Quem pode acessar: Qualquer pessoa  → Implantar.
 *  6. Copie a URL do App da Web (termina em /exec) e envie para colocar no app (constante PLANILHA_PADRAO).
 *  Ao alterar este script depois: Implantar → Gerenciar implantações → editar → Nova versão (a URL continua a mesma).
 */
const ABA_P = 'Protocolos', ABA_C = 'Consultores';
const CAB_P = ['Número','Revisão','Número completo','Consultor','Código','Cliente','Propriedade','Município','Área (ha)','Tipo','Data do protocolo','Salvo em','Hash','Dados (JSON)'];
const CAB_C = ['Nome','Código','PIN','Ativo','E-mail'];
const TAM = 45000;           // limite seguro por célula (Google: 50.000 caracteres)

/* planilha usada: a do próprio script (Extensões → Apps Script) ou, se o script foi criado solto,
   uma planilha "Protocolos Bolsa Irriga" criada automaticamente no seu Drive (o endereço aparece no registo de execução). */
function planilha(){
  const a = SpreadsheetApp.getActive(); if(a) return a;
  const props = PropertiesService.getScriptProperties(), id = props.getProperty('PLANILHA_ID');
  if(id){ try{ return SpreadsheetApp.openById(id); }catch(e){} }
  const ss = SpreadsheetApp.create('Protocolos Bolsa Irriga'); props.setProperty('PLANILHA_ID', ss.getId()); return ss;
}

function configurar(){
  const ss = planilha();
  let c = ss.getSheetByName(ABA_C);
  if(!c){ c = ss.insertSheet(ABA_C); }
  if(c.getLastRow() === 0){
    c.getRange('A:E').setNumberFormat('@');
    c.appendRow(CAB_C); c.appendRow(['Nome do Consultor','JP','1234','Sim','']); c.setFrozenRows(1);
  }
  let p = ss.getSheetByName(ABA_P);
  if(!p){ p = ss.insertSheet(ABA_P); }
  if(p.getLastRow() === 0){
    p.getRange('A:M').setNumberFormat('@');
    p.appendRow(CAB_P); p.setFrozenRows(1);
  }
  Logger.log('Planilha pronta: ' + ss.getUrl());
}

function doGet(e){ return saida(rotear((e && e.parameter) || {})); }
function doPost(e){ let p = {}; try{ p = JSON.parse(e.postData.contents); }catch(err){} return saida(rotear(p)); }
function saida(o){ return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }

function rotear(p){
  try{
    configurar();
    switch(p.acao){
      case 'consultores': return {ok:true, consultores: consultores().filter(c=>c.ativo).map(c=>({nome:c.nome, codigo:c.codigo}))};
      case 'lista':  autenticar(p); return {ok:true, protocolos: listar(cod(p))};
      case 'abrir':  autenticar(p); return abrir(cod(p), String(p.numero||'').trim());
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
  return sh.getRange(2, 1, n-1, CAB_P.length-1).getDisplayValues().map((r,i) => ({
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
function abrir(codigo, numero){
  const u = ultimaRevisao(linhas(), numero);
  if(!u) throw new Error('Protocolo ' + numero + ' não encontrado');
  if(u.codigo !== codigo) throw new Error('Este protocolo pertence a outro consultor');
  const sh = planilha().getSheetByName(ABA_P);
  const ini = CAB_P.length, n = Math.max(1, sh.getLastColumn() - ini + 1);
  const dados = sh.getRange(u.row, ini, 1, n).getValues()[0].map(String).join('');
  return {ok:true, numero:u.numero, rev:u.rev, dados:dados};
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
    const r = p.resumo || {}, dados = String(p.dados || ''), partes = [];
    for(let i = 0; i < dados.length; i += TAM) partes.push(dados.slice(i, i + TAM));
    sh.appendRow([numero, String(rev), numero + (rev ? ' R' + rev : ''), r.consultor||'', codigo, r.cliente||'', r.propriedade||'',
      r.municipio||'', String(r.area||''), r.tipo||'', r.data||'', Utilities.formatDate(new Date(), tz, 'yyyy-MM-dd HH:mm:ss'), p.hash||''].concat(partes));
    return {ok:true, numero:numero, rev:rev};
  } finally { lock.releaseLock(); }
}
