import base64, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('logo perfil branca.png','rb') as f:
    LOGO = base64.b64encode(f.read()).decode()

HTML = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cloração — Irrigação por Gotejamento — Bolsa Irriga</title>
<style>
:root{
  --bl:#005f8e;--bl2:#0077b6;--bl3:#00b4d8;--bl4:#caf0f8;
  --gn:#1b6e3a;--gn2:#2d9e5a;--gn3:#d4edda;
  --rd:#c62828;--am:#e07b00;--am2:#fff8e1;
  --bg:#f4f7fb;--bdr:#d0e4f0;--tx:#1a2535;--mu:#607080;
  --sh:0 2px 16px rgba(0,80,160,.10);
  --cl1:#006064;--cl2:#00838f;--cl3:#b2ebf2;
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--tx);font-size:14px}
header{background:linear-gradient(135deg,#003d5c,var(--cl1),var(--cl2));color:#fff;box-shadow:0 3px 20px rgba(0,0,0,.2)}
.hdr{max-width:1320px;margin:0 auto;padding:1rem 1.5rem;display:flex;justify-content:space-between;align-items:center;gap:1rem;flex-wrap:wrap}
.hdr-logo{display:flex;align-items:center;gap:1rem}
.hdr-logo img{height:70px;width:70px;object-fit:contain;background:#fff;border-radius:10px;padding:7px;box-shadow:0 2px 10px rgba(0,0,0,.18)}
.hdr-brand h1{font-size:1.45rem;font-weight:800;letter-spacing:-.3px}
.hdr-brand p{opacity:.85;font-size:.82rem;margin-top:.1rem}
.hdr-dev{text-align:right;font-size:.78rem;line-height:1.7;opacity:.92;border-left:2px solid rgba(255,255,255,.25);padding-left:1.2rem}
.hdr-dev .dn{font-size:.95rem;font-weight:800}
.hdr-co{font-size:.7rem;opacity:.75;margin-top:.15rem}
.page{max-width:1320px;margin:1.4rem auto;padding:0 1rem}
.card{background:#fff;border-radius:12px;padding:1.2rem 1.4rem;margin-bottom:1rem;box-shadow:var(--sh);border:1px solid var(--bdr)}
.ct{font-size:.76rem;font-weight:800;color:var(--cl1);text-transform:uppercase;letter-spacing:.08em;margin-bottom:.8rem;padding-bottom:.48rem;border-bottom:2px solid var(--cl3);display:flex;align-items:center;gap:.45rem}
.ct::before{content:'';width:4px;height:1.1em;background:var(--cl2);border-radius:2px;flex-shrink:0}
.sn{display:inline-flex;width:20px;height:20px;background:var(--cl1);color:#fff;border-radius:50%;align-items:center;justify-content:center;font-size:.72rem;font-weight:900;flex-shrink:0}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
.g3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:.8rem}
.g4{display:grid;grid-template-columns:repeat(4,1fr);gap:.7rem}
@media(max-width:900px){.g2{grid-template-columns:1fr}.g3{grid-template-columns:1fr 1fr}.g4{grid-template-columns:1fr 1fr}}
@media(max-width:540px){.g3,.g4{grid-template-columns:1fr}}
.fg{display:flex;flex-direction:column;gap:.2rem}
label{font-size:.72rem;font-weight:700;color:var(--mu);text-transform:uppercase;letter-spacing:.05em}
.fg small{font-size:.67rem;color:var(--mu);margin-top:.08rem}
.iu{display:flex}
.iu input,.iu select{flex:1;border-radius:8px 0 0 8px}
.iu .u{background:var(--bdr);border:1.5px solid var(--bdr);border-left:none;padding:.48rem .55rem;font-size:.77rem;color:var(--mu);border-radius:0 8px 8px 0;white-space:nowrap;display:flex;align-items:center}
input[type=number],input[type=text],input[type=date],select,textarea{padding:.48rem .68rem;border:1.5px solid var(--bdr);border-radius:8px;font-size:.9rem;color:var(--tx);background:#fafeff;outline:none;transition:border-color .18s,box-shadow .18s;width:100%}
input:focus,select:focus,textarea:focus{border-color:var(--cl2);box-shadow:0 0 0 3px rgba(0,131,143,.13)}
.tile{border-radius:10px;padding:.75rem .9rem}
.tg{background:linear-gradient(135deg,#e8f5e9,#c8e6c9);border:1px solid #a5d6a7}
.tt{background:linear-gradient(135deg,#e0f7fa,#b2ebf2);border:1px solid #80deea}
.tb2{background:linear-gradient(135deg,#e8f4fd,#d0eaf8);border:1px solid #a8d4f0}
.to{background:linear-gradient(135deg,#fff3e0,#ffe0b2);border:1px solid #ffcc80}
.tl{font-size:.67rem;font-weight:800;color:var(--cl1);text-transform:uppercase;letter-spacing:.06em;margin-bottom:.15rem}
.tv{font-size:1.15rem;font-weight:900;color:#003d5c;line-height:1.1}
.tv.lg{font-size:1.35rem}
.tv small{font-size:.7rem;font-weight:500;color:var(--mu);margin-left:.1rem}
.sbox{padding:.75rem 1rem;border-radius:8px;font-size:.84rem;line-height:1.5}
.sbox.info{background:#e0f7fa;border-left:4px solid var(--cl2);color:#003d5c}
.sbox.warn{background:var(--am2);border-left:4px solid #f59e0b;color:#7c4d00}
.sbox.ok{background:var(--gn3);border-left:4px solid var(--gn2);color:#1b4d2e}
.sbox.err{background:#ffebee;border-left:4px solid var(--rd);color:#7f0000}
/* Operations table */
.ops-wrap{overflow-x:auto}
.ops-tbl{width:100%;border-collapse:collapse;font-size:.88rem;min-width:700px}
.ops-tbl th{padding:.5rem .7rem;font-size:.7rem;font-weight:800;text-transform:uppercase;letter-spacing:.05em;text-align:center;background:#e0f7fa;border:1px solid #b2ebf2;color:var(--cl1)}
.ops-tbl th.lh{text-align:left}
.ops-tbl td{padding:.35rem .5rem;border:1px solid #e0f0f5;vertical-align:middle;text-align:center}
.ops-tbl td.num{color:var(--mu);font-size:.8rem;font-weight:700;background:#f4f8fb}
.ops-tbl td input{border:1px solid #d0e8f0;border-radius:6px;padding:.3rem .5rem;font-size:.88rem;background:#fff;text-align:right;width:100%;min-width:80px}
.ops-tbl td input:focus{border-color:var(--cl2);outline:none;box-shadow:0 0 0 2px rgba(0,131,143,.15)}
.ops-tbl td input.desc{text-align:left}
.ops-tbl .res{background:#f0fbfc;font-weight:700;color:var(--cl1)}
.ops-tbl .res-pump{background:#fff8e1;font-weight:700;color:#7c4d00}
.ops-tbl .del-btn{background:none;border:none;cursor:pointer;color:#ef5350;font-size:1rem;padding:.2rem .4rem;border-radius:4px;line-height:1}
.ops-tbl .del-btn:hover{background:#ffebee}
.ops-tbl tr:hover td:not(.num){background:#f8fdfe}
.add-btn{background:var(--cl1);color:#fff;border:none;border-radius:8px;padding:.5rem 1.1rem;font-size:.84rem;font-weight:700;cursor:pointer;display:inline-flex;align-items:center;gap:.35rem;margin-top:.6rem;transition:background .15s}
.add-btn:hover{background:var(--cl2)}
/* totals */
.tot-row td{background:#e0f7fa!important;font-weight:800;color:#003d5c!important;border-top:2px solid var(--cl2)!important}
/* pump badge */
.pump-badge{display:inline-block;padding:.3rem .9rem;border-radius:14px;font-size:.88rem;font-weight:800;background:linear-gradient(135deg,#e65100,#f57c00);color:#fff;box-shadow:0 2px 8px rgba(230,81,0,.3)}
/* info box */
.info-grid{display:grid;grid-template-columns:1fr 1fr;gap:.6rem;margin-top:.5rem}
@media(max-width:600px){.info-grid{grid-template-columns:1fr}}
.info-item{background:#f0fbfc;border-radius:8px;padding:.6rem .8rem;border-left:3px solid var(--cl2)}
.info-item h4{font-size:.72rem;font-weight:800;color:var(--cl1);text-transform:uppercase;margin-bottom:.2rem}
.info-item p{font-size:.8rem;color:var(--tx);line-height:1.4}
/* action bar */
.abar{display:flex;justify-content:flex-end;gap:.75rem;padding:.3rem 0 .9rem;flex-wrap:wrap}
.btn{padding:.65rem 1.4rem;border:none;border-radius:8px;font-size:.88rem;font-weight:700;cursor:pointer;transition:all .18s;display:inline-flex;align-items:center;gap:.4rem}
.bpdf{background:linear-gradient(135deg,#b71c1c,#880e4f);color:#fff;padding:.72rem 1.8rem}
.bpdf:hover{transform:translateY(-1px);box-shadow:0 4px 16px rgba(183,28,28,.38)}
.bg{background:var(--bdr);color:var(--tx)}.bg:hover{background:#b8d8ee}
footer{background:#fff;border-top:2px solid var(--bdr);padding:1rem 1.5rem;margin-top:.5rem}
.fi{max-width:1320px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem}
.fd{display:flex;align-items:center;gap:.75rem}
.fd img{height:40px;width:40px;object-fit:contain;border-radius:7px;padding:3px;background:#f0f7ff;border:1px solid var(--bdr)}
.fdn .fn{font-weight:800;color:var(--cl1);font-size:.88rem}
.fdn .fr{font-size:.74rem;color:var(--mu);line-height:1.5}
.fc{font-size:.71rem;color:var(--mu);text-align:right;line-height:1.7}
</style>
</head>
<body>
<header>
  <div class="hdr">
    <div class="hdr-logo">
      <img src="data:image/png;base64,##LOGO##" alt="Bolsa Irriga">
      <div class="hdr-brand">
        <h1>Cloração — Irriga&#231;&#227;o por Gotejamento</h1>
        <p>Dimensionamento de Clorador &middot; Bomba Injetora &middot; Controle de Biofilme</p>
      </div>
    </div>
    <div class="hdr-dev">
      <div class="dn">Jo&#227;o Paulo de Oliveira</div>
      <div style="font-size:.78rem;opacity:.88">Engenheiro Agr&#244;nomo &middot; Especialista em Irriga&#231;&#227;o</div>
      <div class="hdr-co">Av. Elias Abr&#227;o, n&#186; 140 &middot; Franca &#8211; SP &middot; (16) 3702-6571 &middot; bolsairriga.com.br</div>
    </div>
  </div>
</header>

<div class="page">

<!-- CLIENTE -->
<div class="card">
  <div class="ct">Dados do Cliente / Projeto</div>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:.9rem">
    <div class="fg"><label>Consultor</label><input type="text" id="consultor" placeholder="Jo&#227;o Paulo de Oliveira"></div>
    <div class="fg"><label>Cliente</label><input type="text" id="cliente" placeholder="Nome do cliente"></div>
    <div class="fg"><label>Propriedade</label><input type="text" id="propriedade" placeholder="Fazenda Boa Vista"></div>
    <div class="fg"><label>Cidade / UF</label><input type="text" id="cidade" placeholder="Orl&#226;ndia / SP"></div>
    <div class="fg"><label>Data</label><input type="date" id="data"></div>
  </div>
</div>

<div class="g2" style="align-items:start">

<!-- LEFT: PARÂMETROS -->
<div>
  <div class="card">
    <div class="ct"><span class="sn">1</span> Par&#226;metros da Clora&#231;&#227;o</div>
    <div class="g2">
      <div class="fg"><label>Tipo de Clora&#231;&#227;o</label>
        <select id="tipo" onchange="onTipo()">
          <option value="prev">Preventiva — Controle de Biofilme</option>
          <option value="cur">Curativa — Desentupimento de Emissores</option>
          <option value="choque">Choque — Limpeza Inicial do Sistema</option>
          <option value="custom">Personalizada</option>
        </select>
        <small id="tipo-hint">Manuten&#231;&#227;o regular: 5&ndash;10 ppm na &#225;gua de irriga&#231;&#227;o</small></div>
      <div class="fg"><label>Concentra&#231;&#227;o Alvo na &#193;gua</label>
        <div class="iu"><input type="number" id="conc" value="" min="1" max="200" step="1" oninput="calc()"><span class="u">ppm</span></div>
        <small>ppm = mg/L = g/m&#179;</small></div>
      <div class="fg"><label>Produto Clorador</label>
        <select id="produto" onchange="onProduto()">
          <option value="12">Hipoclorito de S&#243;dio 12% (l&#237;quido)</option>
          <option value="10">Hipoclorito de S&#243;dio 10% (l&#237;quido)</option>
          <option value="60" selected>Hipoclorito de C&#225;lcio 60% (p&#243; / granulado)</option>
          <option value="65">Hipoclorito de C&#225;lcio 65% (p&#243; / granulado)</option>
          <option value="70">Hipoclorito de C&#225;lcio 70% (p&#243; / granulado)</option>
          <option value="100">Cloro Gasoso 100%</option>
          <option value="custom">Outro (digitar concentra&#231;&#227;o)</option>
        </select></div>
      <div class="fg"><label>Concentra&#231;&#227;o do Produto (%)</label>
        <div class="iu"><input type="number" id="concProd" value="" min="1" max="100" step="0.5" oninput="calc()"><span class="u">%</span></div>
        <small>Cloro ativo no produto comercial</small></div>
      <div class="fg"><label>Estado F&#237;sico do Produto</label>
        <select id="estado" onchange="calc()">
          <option value="L">L&#237;quido (resultado em Litros)</option>
          <option value="S">S&#243;lido / P&#243; (resultado em kg)</option>
        </select></div>
      <div class="fg"><label>Densidade do produto (l&#237;quido)</label>
        <div class="iu"><input type="number" id="dens" value="" min="0.9" max="1.5" step="0.01" oninput="calc()"><span class="u">kg/L</span></div>
        <small>Apenas para produto l&#237;quido. Hipoclorito de S&#243;dio &#8776; 1,15 kg/L</small></div>
    </div>
  </div>

  <div class="card">
    <div class="ct"><span class="sn">2</span> Refer&#234;ncias de Concentra&#231;&#227;o (ppm)</div>
    <div class="info-grid">
      <div class="info-item">
        <h4>&#128308; Preventiva (Biofilme)</h4>
        <p><strong>5&ndash;10 ppm</strong> na &#225;gua de irriga&#231;&#227;o. Aplicar periodicamente para evitar forma&#231;&#227;o de biofilme nos emissores.</p>
      </div>
      <div class="info-item">
        <h4>&#128992; Curativa (Desentupimento)</h4>
        <p><strong>20&ndash;50 ppm</strong> por 30&ndash;60 min. Para eliminar obstrui&#231;&#245;es biol&#243;gicas existentes nos gotejadores.</p>
      </div>
      <div class="info-item">
        <h4>&#128534; Choque (Limpeza inicial)</h4>
        <p><strong>100&ndash;200 ppm</strong> por 30 min. Desinfec&#231;&#227;o completa do sistema antes da primeira irriga&#231;&#227;o ou ap&#243;s reparo.</p>
      </div>
      <div class="info-item">
        <h4>&#9888;&#65039; Aten&#231;&#227;o</h4>
        <p>pH ideal: <strong>6,0&ndash;7,0</strong> para m&#225;xima efici&#234;ncia do cloro. Acima de pH 8 a efici&#234;ncia cai drasticamente.</p>
      </div>
    </div>
  </div>
</div>

<!-- RIGHT: RESUMO -->
<div>
  <div class="card">
    <div class="ct">Resumo Geral</div>
    <div id="resumo"><div class="sbox info">Preencha a tabela de opera&#231;&#245;es para calcular.</div></div>
  </div>
  <div class="card">
    <div class="ct">Bomba Injetora / Clorador</div>
    <div id="bomba-info"><div class="sbox info">Aguardando c&#225;lculo...</div></div>
  </div>
  <div class="card">
    <div class="ct">Procedimento de Aplica&#231;&#227;o</div>
    <div id="procedimento" class="sbox info" style="font-size:.82rem;line-height:1.7">Selecione o tipo de clora&#231;&#227;o para ver o procedimento recomendado.</div>
  </div>
</div>

</div><!-- /g2 -->

<!-- TABELA DE OPERAÇÕES -->
<div class="card">
  <div class="ct"><span class="sn">3</span> Opera&#231;&#245;es de Irriga&#231;&#227;o &mdash; Setores / Turnos</div>
  <div class="ops-wrap">
    <table class="ops-tbl" id="ops-tbl">
      <thead>
        <tr>
          <th class="lh" style="width:30px">#</th>
          <th class="lh" style="min-width:130px">Descri&#231;&#227;o</th>
          <th style="min-width:90px">Vaz&#227;o Q<br><small>(m&#179;/h)</small></th>
          <th style="min-width:90px">Tempo<br><small>(min)</small></th>
          <th style="min-width:90px">Volume Irrig.<br><small>(m&#179;)</small></th>
          <th style="min-width:100px">Produto<br><small id="hdr-unidade">(L ou kg)</small></th>
          <th style="min-width:110px">Taxa Inje&#231;&#227;o<br><small>(mL/min)</small></th>
          <th style="width:32px"></th>
        </tr>
      </thead>
      <tbody id="ops-body"></tbody>
      <tfoot>
        <tr class="tot-row" id="tot-row">
          <td colspan="2" style="text-align:left;padding-left:.6rem">TOTAL</td>
          <td id="tot-q">—</td>
          <td id="tot-t">—</td>
          <td id="tot-vol">—</td>
          <td id="tot-prod">—</td>
          <td id="tot-pump">M&#225;x.</td>
          <td></td>
        </tr>
      </tfoot>
    </table>
  </div>
  <button class="add-btn" onclick="addRow()">&#43; Adicionar Setor / Opera&#231;&#227;o</button>
</div>

<div class="abar">
  <button class="btn bg" onclick="resetForm()">&#8635; Limpar</button>
  <button class="btn bpdf" onclick="gerarPDF()">&#128196; Gerar Relat&#243;rio PDF</button>
</div>

</div><!-- /page -->

<footer>
  <div class="fi">
    <div class="fd">
      <img src="data:image/png;base64,##LOGO##" alt="Logo">
      <div class="fdn">
        <div class="fn">Jo&#227;o Paulo de Oliveira</div>
        <div class="fr">Engenheiro Agr&#244;nomo &middot; Especialista em Irriga&#231;&#227;o &middot; bolsairriga.com.br</div>
      </div>
    </div>
    <div class="fc">Bolsa Irriga&#174; &mdash; Clora&#231;&#227;o para Gotejamento v1.0<br>
      Av. Elias Abr&#227;o, n&#186; 140 &middot; Franca &#8211; SP &middot; (16) 3702-6571<br>
      &copy; 2025 Jo&#227;o Paulo de Oliveira</div>
  </div>
</footer>

<script>
const $=id=>document.getElementById(id);
const gv=id=>parseFloat($(id).value)||0;
const fmt=(n,d=2)=>n==null||isNaN(n)||!isFinite(n)?'—':n.toLocaleString('pt-BR',{minimumFractionDigits:d,maximumFractionDigits:d});
const fmtR=n=>n.toLocaleString('pt-BR',{style:'currency',currency:'BRL'});
const LOGO='##LOGO##';

// ── TIPOS E PROCEDIMENTOS ────────────────────────────────────────────
const TIPOS={
  prev:{conc:10,hint:'Manutenção regular: 5–10 ppm na água de irrigação',
    proc:`<b>1. Antes da irrigação:</b> Verifique o pH da água (ideal 6,0–7,0).<br>
<b>2. Durante:</b> Injete o cloro no início da irrigação, mantendo a concentração constante.<br>
<b>3. Tempo de contato:</b> O cloro deve chegar até os emissores com pelo menos 5 ppm residuais.<br>
<b>4. Frequência recomendada:</b> A cada 7–15 dias, dependendo da qualidade da água.<br>
<b>5. Monitoramento:</b> Use kit colorimétrico ou eletrodo de cloro livre.`},
  cur:{conc:30,hint:'Desentupimento: 20–50 ppm por 30–60 min',
    proc:`<b>1. Pré-lavagem:</b> Irrigue por 10 min com água limpa antes de injetar o cloro.<br>
<b>2. Injeção:</b> Aplique a solução clorada na concentração calculada.<br>
<b>3. Tempo de contato:</b> Mantenha o sistema fechado por 30–60 minutos (depende do entupimento).<br>
<b>4. Abrir finais de linha:</b> Abra os drenos dos finais de linha para liberar resíduos.<br>
<b>5. Pós-lavagem:</b> Irrigue por 15 min com água limpa para eliminar o cloro residual.<br>
<b>6. Verificação:</b> Confira a vazão dos emissores após o procedimento.`},
  choque:{conc:150,hint:'Choque: 100–200 ppm por 30 min — apenas para limpeza inicial',
    proc:`<b>⚠️ ATENÇÃO:</b> Concentrações acima de 100 ppm podem danificar culturas. Aplique somente com sistema SEM plantas irrigadas.<br><br>
<b>1. Pré-condição:</b> Sistema vazio ou com espaço para enchimento total.<br>
<b>2. Enchimento:</b> Preencha toda a rede com a solução clorada.<br>
<b>3. Tempo de contato:</b> Aguarde 30 minutos com sistema pressurizado.<br>
<b>4. Descarte:</b> Abra todos os drenos e descarregue a solução com segurança.<br>
<b>5. Lavagem tripla:</b> Passe três ciclos completos de água limpa antes de irrigar.`},
  custom:{conc:10,hint:'Digite a concentração desejada',
    proc:'Configure os parâmetros conforme o protocolo técnico da sua propriedade.'}
};

// ── PRODUTOS ────────────────────────────────────────────────────────
const PRODUTOS={
  '12':{conc:12,estado:'L',dens:1.20,label:'Hipoclorito de Sódio 12%'},
  '10':{conc:10,estado:'L',dens:1.15,label:'Hipoclorito de Sódio 10%'},
  '60':{conc:60,estado:'S',dens:1.0, label:'Hipoclorito de Cálcio 60%'},
  '65':{conc:65,estado:'S',dens:1.0, label:'Hipoclorito de Cálcio 65%'},
  '70':{conc:70,estado:'S',dens:1.0, label:'Hipoclorito de Cálcio 70%'},
  '100':{conc:100,estado:'L',dens:1.56,label:'Cloro Gasoso'},
  'custom':null
};

function onTipo(){
  const t=TIPOS[$('tipo').value];
  if(!t) return;
  $('conc').value=t.conc;
  $('tipo-hint').textContent=t.hint;
  $('procedimento').innerHTML=t.proc;
  calc();
}
function onProduto(){
  const p=PRODUTOS[$('produto').value];
  if(p){
    $('concProd').value=p.conc;
    $('estado').value=p.estado;
    if(p.dens) $('dens').value=p.dens;
  }
  calc();
}

// ── CÁLCULO POR OPERAÇÃO ─────────────────────────────────────────────
// Produto (L ou kg) = Q(m³/h) × T(h) × C_agua(ppm) / (C_prod(%) × 10)
// Para líquido: resultado já em litros (assumindo densidade 1 na fórmula base)
// Para sólido: resultado em kg (densidade irrelevante)
// Taxa injeção (mL/min) = volume_produto_L / T_h × 1000 / 60
function calcOp(Q, T_min, C_agua, C_prod){
  if(!Q||!T_min||!C_agua||!C_prod) return null;
  const T_h=T_min/60;
  const volIrrig=Q*T_h; // m³
  const prod_base=Q*T_h*C_agua/(C_prod*10); // litros base (assumindo dens=1)
  const estado=$('estado').value;
  const dens=estado==='L'?gv('dens'):1.0;
  // Para líquido: corrigir pela densidade real → prod_L = prod_base / dens
  // (a fórmula base assume que 1L = 1kg; corrigindo: L = kg / dens)
  const prod_final=estado==='L'?prod_base/dens:prod_base; // L ou kg
  const taxa_mLmin=estado==='L'?(prod_final/T_h*1000/60):null; // mL/min só para líquido
  return{Q,T_min,T_h,volIrrig,prod_final,taxa_mLmin};
}

// ── LINHAS DA TABELA ──────────────────────────────────────────────────
let rowCount=0;
function addRow(Q='',T='',desc=''){
  rowCount++;
  const n=rowCount;
  const tr=document.createElement('tr');
  tr.id=`row-${n}`;
  tr.innerHTML=`
    <td class="num">${n}</td>
    <td><input class="desc" type="text" id="d-${n}" placeholder="Setor ${n}" value="${desc}" oninput="calc()"></td>
    <td><input type="number" id="q-${n}" value="${Q}" min="0" step="0.1" placeholder="0.0" oninput="calc()"></td>
    <td><input type="number" id="t-${n}" value="${T}" min="0" step="5" placeholder="0" oninput="calc()"></td>
    <td class="res" id="vi-${n}">—</td>
    <td class="res" id="pr-${n}">—</td>
    <td class="res-pump" id="tx-${n}">—</td>
    <td><button class="del-btn" onclick="delRow(${n})">&#10005;</button></td>`;
  $('ops-body').appendChild(tr);
  calc();
}
function delRow(n){
  const el=$(`row-${n}`);
  if(el) el.remove();
  calc();
}

// ── CALC PRINCIPAL ────────────────────────────────────────────────────
function calc(){
  const C_agua=gv('conc'), C_prod=gv('concProd');
  const estado=$('estado').value;
  const unidade=estado==='L'?'L':'kg';
  $('hdr-unidade').textContent=`(${unidade})`;

  const rows=[...$('ops-body').querySelectorAll('tr')];
  let totalQ=0,totalT=0,totalVol=0,totalProd=0,maxTaxa=0;
  const opResults=[];

  for(const tr of rows){
    const n=tr.id.replace('row-','');
    const Q=gv(`q-${n}`),T=gv(`t-${n}`);
    const r=calcOp(Q,T,C_agua,C_prod);
    opResults.push({n,Q,T,desc:$(`d-${n}`)?.value||`Setor ${n}`,r});
    if(r){
      totalQ+=Q; totalT+=T;
      totalVol+=r.volIrrig; totalProd+=r.prod_final;
      if(r.taxa_mLmin&&r.taxa_mLmin>maxTaxa) maxTaxa=r.taxa_mLmin;
      $(`vi-${n}`).textContent=fmt(r.volIrrig)+' m³';
      $(`pr-${n}`).textContent=fmt(r.prod_final)+' '+unidade;
      $(`tx-${n}`).textContent=r.taxa_mLmin?fmt(r.taxa_mLmin)+' mL/min':'—';
    } else {
      $(`vi-${n}`).textContent='—';
      $(`pr-${n}`).textContent='—';
      $(`tx-${n}`).textContent='—';
    }
  }

  // Totais
  if(totalProd>0){
    $('tot-q').textContent=fmt(totalQ/rows.length||0)+' m³/h';
    $('tot-t').textContent=fmt(totalT)+' min';
    $('tot-vol').textContent=fmt(totalVol)+' m³';
    $('tot-prod').textContent=fmt(totalProd)+' '+unidade;
    $('tot-pump').textContent=estado==='L'?fmt(maxTaxa)+' mL/min':'—';
  }

  // Resumo
  if(totalProd>0){
    const maxTaxaLh=maxTaxa*60/1000;
    $('resumo').innerHTML=`
      <div class="g4" style="margin-bottom:.6rem">
        <div class="tile tt"><div class="tl">N&#186; Opera&#231;&#245;es</div><div class="tv lg">${rows.length}</div></div>
        <div class="tile tt"><div class="tl">Vol. Total Irrigado</div><div class="tv">${fmt(totalVol)} <small>m&#179;</small></div></div>
        <div class="tile tg"><div class="tl">Produto Total / ciclo</div><div class="tv lg">${fmt(totalProd)} <small>${unidade}</small></div></div>
        <div class="tile to"><div class="tl">Taxa M&#225;x. Inje&#231;&#227;o</div><div class="tv">${estado==='L'?fmt(maxTaxa)+' <small>mL/min</small>':'—'}</div></div>
      </div>
      <div class="sbox ok" style="font-size:.82rem">
        &#10003; Concentra&#231;&#227;o alvo: <strong>${fmt(C_agua,0)} ppm</strong> &nbsp;|&nbsp;
        Produto: <strong>${$('produto').options[$('produto').selectedIndex].text.split('(')[0].trim()}</strong> a <strong>${fmt(C_prod,0)}%</strong>
      </div>`;

    // Bomba injetora
    const maxTaxaLhDisp=estado==='L'?maxTaxaLh:null;
    let bombaTipo='', bombaObs='';
    if(estado==='S'){
      bombaTipo='Tanque de Diluição + Venturi ou Bomba Dosadora';
      bombaObs='Para produtos sólidos (pó), dilua em água antes de injetar. Prepare solução estoque e injete como líquido.';
    } else if(maxTaxaLh<=3){
      bombaTipo='Válvula Venturi';
      bombaObs='Capacidade ≤ 3 L/h — adequado para injetores Venturi simples.';
    } else if(maxTaxaLh<=60){
      bombaTipo='Bomba Dosadora Elétrica ou de Pistão';
      bombaObs=`Capacidade mínima: <strong>${fmt(maxTaxaLh,1)} L/h</strong>. Bomba dosadora elétrica (diafragma ou pistão).`;
    } else {
      bombaTipo='Bomba Dosadora de Alta Capacidade';
      bombaObs=`Capacidade mínima: <strong>${fmt(maxTaxaLh,1)} L/h</strong>. Avalie bomba centrífuga com by-pass ou tanque pressurizado.`;
    }
    $('bomba-info').innerHTML=`
      <div style="margin-bottom:.6rem">
        <div class="tl" style="margin-bottom:.3rem">Tipo Recomendado</div>
        <span class="pump-badge">${bombaTipo}</span>
      </div>
      ${maxTaxaLhDisp?`<div class="g2" style="margin-bottom:.5rem">
        <div class="tile to"><div class="tl">Vaz&#227;o m&#225;x. necess&#225;ria</div><div class="tv">${fmt(maxTaxa,1)} <small>mL/min</small></div></div>
        <div class="tile to"><div class="tl">Vaz&#227;o m&#225;x. necess&#225;ria</div><div class="tv">${fmt(maxTaxaLh,2)} <small>L/h</small></div></div>
      </div>`:''}
      <div class="sbox info" style="font-size:.8rem">${bombaObs}</div>`;
  } else {
    $('resumo').innerHTML='<div class="sbox info">Preencha a tabela de operações para calcular.</div>';
    $('bomba-info').innerHTML='<div class="sbox info">Aguardando cálculo...</div>';
  }
}

// ── RESET ─────────────────────────────────────────────────────────────
function resetForm(){
  ['consultor','cliente','propriedade','cidade'].forEach(id=>$(id).value='');
  onTipo();
  onProduto();
  $('ops-body').innerHTML=''; rowCount=0;
  }

// ── PDF ───────────────────────────────────────────────────────────────
function gerarPDF(){
  const C_agua=gv('conc'), C_prod=gv('concProd');
  const estado=$('estado').value, unidade=estado==='L'?'L':'kg';
  const cons=$('consultor').value||'—', cli=$('cliente').value||'—';
  const prop=$('propriedade').value||'—', cid=$('cidade').value||'—';
  const dt=$('data').value?new Date($('data').value+'T12:00:00').toLocaleDateString('pt-BR'):'—';
  const prodLabel=$('produto').options[$('produto').selectedIndex].text;
  const tipoLabel=$('tipo').options[$('tipo').selectedIndex].text;

  const rows=[...$('ops-body').querySelectorAll('tr')];
  let totalVol=0,totalProd=0,maxTaxa=0;
  let tblRows='';
  rows.forEach((tr,i)=>{
    const n=tr.id.replace('row-','');
    const Q=gv(`q-${n}`),T=gv(`t-${n}`);
    const desc=$(`d-${n}`)?.value||`Setor ${n+1}`;
    const r=calcOp(Q,T,C_agua,C_prod);
    if(r){
      totalVol+=r.volIrrig; totalProd+=r.prod_final;
      if(r.taxa_mLmin&&r.taxa_mLmin>maxTaxa) maxTaxa=r.taxa_mLmin;
    }
    tblRows+=`<tr style="${i%2===0?'background:#f8fbfc':''}">
      <td style="text-align:center;color:#607080">${i+1}</td>
      <td>${desc}</td>
      <td style="text-align:center">${Q||'—'}</td>
      <td style="text-align:center">${T||'—'}</td>
      <td style="text-align:center">${r?fmt(r.volIrrig):'—'}</td>
      <td style="text-align:center;font-weight:700;color:#006064">${r?fmt(r.prod_final)+' '+unidade:'—'}</td>
      <td style="text-align:center;color:#e65100">${r&&r.taxa_mLmin?fmt(r.taxa_mLmin)+' mL/min':'—'}</td>
    </tr>`;
  });

  const maxTaxaLh=maxTaxa*60/1000;
  let bombaTipo='';
  if(estado==='S') bombaTipo='Tanque de Diluição + Bomba Dosadora';
  else if(maxTaxaLh<=3) bombaTipo='Válvula Venturi';
  else if(maxTaxaLh<=60) bombaTipo='Bomba Dosadora Elétrica (diafragma/pistão)';
  else bombaTipo='Bomba Dosadora de Alta Capacidade';

  const proc=TIPOS[$('tipo').value]?.proc?.replace(/<br>/g,'\n').replace(/<[^>]+>/g,'')||'';

  const css=`*{box-sizing:border-box;margin:0;padding:0;font-family:'Segoe UI',sans-serif}
body{font-size:10pt;color:#1a2535;background:#fff}
.pg{padding:8mm 12mm;page-break-after:always;min-height:280mm}.pg:last-child{page-break-after:avoid}
.hd{background:linear-gradient(135deg,#003d5c,#006064,#00838f);color:#fff;padding:6px 12px;display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;border-radius:4px}
.hl{display:flex;align-items:center;gap:8px}.hl img{height:40px;width:40px;background:#fff;border-radius:6px;padding:3px;object-fit:contain}
.hb h2{font-size:.95rem;font-weight:800}.hb p{font-size:.65rem;opacity:.85}
.hr2{text-align:right;font-size:.65rem;line-height:1.6}.hr2 b{font-size:.78rem;display:block}
.cli{background:#e0f7fa;border:1px solid #b2ebf2;border-radius:4px;padding:5px 10px;display:grid;grid-template-columns:repeat(5,1fr);gap:4px;margin-bottom:6px;font-size:.76rem}
.cf label{font-size:.6rem;font-weight:800;color:#607080;text-transform:uppercase;display:block}
.cf span{font-weight:700;color:#003d5c}
.st{font-size:.72rem;font-weight:900;color:#006064;text-transform:uppercase;letter-spacing:.06em;padding:3px 0 4px;border-bottom:1.5px solid #b2ebf2;margin:6px 0 4px;display:flex;align-items:center;gap:4px}
.st::before{content:'';width:3px;height:1em;background:#00838f;border-radius:2px;flex-shrink:0}
.params{display:grid;grid-template-columns:repeat(4,1fr);gap:4px;margin-bottom:6px}
.kv{border-radius:5px;padding:4px 6px;background:#f0fbfc;border:1px solid #b2ebf2}
.kv label{font-size:.58rem;font-weight:800;color:#607080;text-transform:uppercase;display:block}
.kv strong{font-size:.9rem;color:#003d5c}
.tbl{width:100%;border-collapse:collapse;font-size:.8rem;margin-bottom:6px}
.tbl th{padding:4px 6px;font-size:.67rem;font-weight:800;text-transform:uppercase;text-align:center;background:#e0f7fa;border:1px solid #b2ebf2;color:#006064}
.tbl th.l{text-align:left}
.tbl td{padding:3px 6px;border:1px solid #e0f0f5}
.tot{background:#e0f7fa!important;font-weight:800;color:#003d5c!important;border-top:2px solid #00838f!important}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-bottom:6px}
.g3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;margin-bottom:6px}
.res-box{border-radius:5px;padding:5px 8px;border:1px solid}
.bomba-box{background:#fff3e0;border:1.5px solid #f57c00;border-radius:6px;padding:6px 10px;margin-bottom:6px}
.bomba-box h4{font-size:.8rem;font-weight:800;color:#e65100;margin-bottom:3px}
.proc-box{background:#f0fbfc;border:1px solid #b2ebf2;border-radius:6px;padding:6px 10px;font-size:.77rem;line-height:1.7}
.proc-box h4{font-size:.78rem;font-weight:800;color:#006064;margin-bottom:4px}
.ft{border-top:1px solid #d0e4f0;padding-top:4px;margin-top:6px;display:flex;justify-content:space-between;font-size:.62rem;color:#607080}
.ft img{height:18px;width:18px;object-fit:contain;border-radius:3px;background:#f0f7ff;padding:2px;border:1px solid #d0e4f0;vertical-align:middle;margin-right:3px}
@media print{*{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}body{margin:0}.pg{padding:5mm 8mm}}`;

  const hdr=`<div class="hd"><div class="hl"><img src="data:image/png;base64,${LOGO}" alt=""><div class="hb"><h2>Bolsa Irriga&#174; &mdash; Clora&#231;&#227;o para Irriga&#231;&#227;o por Gotejamento</h2><p>Dimensionamento de Clorador &middot; Bomba Injetora &middot; Controle de Biofilme</p></div></div><div class="hr2"><b>Jo&#227;o Paulo de Oliveira</b>Eng. Agr&#244;nomo &middot; Esp. Irriga&#231;&#227;o<br>bolsairriga.com.br &middot; (16) 3702-6571</div></div>`;
  const cliHtml=`<div class="cli"><div class="cf"><label>Consultor</label><span>${cons}</span></div><div class="cf"><label>Cliente</label><span>${cli}</span></div><div class="cf"><label>Propriedade</label><span>${prop}</span></div><div class="cf"><label>Cidade/UF</label><span>${cid}</span></div><div class="cf"><label>Data</label><span>${dt}</span></div></div>`;
  const foot=`<div class="ft"><div><img src="data:image/png;base64,${LOGO}" alt=""> Bolsa Irriga&#174; &middot; Av. Elias Abr&#227;o, 140 &middot; Franca &ndash; SP</div><div>Jo&#227;o Paulo de Oliveira &middot; Eng. Agr&#244;nomo</div></div>`;

  const pg1=`<div class="pg">${hdr}${cliHtml}
    <div class="st">Par&#226;metros de Clora&#231;&#227;o</div>
    <div class="params">
      <div class="kv"><label>Tipo de Cloração</label><strong>${tipoLabel.split('—')[0].trim()}</strong></div>
      <div class="kv"><label>Conc. Alvo na Água</label><strong>${fmt(C_agua,0)} ppm</strong></div>
      <div class="kv"><label>Produto Clorador</label><strong>${prodLabel.split('(')[0].trim()}</strong></div>
      <div class="kv"><label>Conc. do Produto</label><strong>${fmt(C_prod,0)}%</strong></div>
    </div>
    <div class="st">Opera&#231;&#245;es de Irriga&#231;&#227;o</div>
    <table class="tbl">
      <thead><tr>
        <th>#</th><th class="l">Descri&#231;&#227;o</th>
        <th>Q (m&#179;/h)</th><th>Tempo (min)</th>
        <th>Vol. Irrig. (m&#179;)</th>
        <th>Produto (${unidade})</th>
        <th>Taxa Inje&#231;&#227;o (mL/min)</th>
      </tr></thead>
      <tbody>${tblRows}</tbody>
      <tfoot><tr class="tot">
        <td colspan="2">TOTAL</td>
        <td style="text-align:center">—</td>
        <td style="text-align:center">—</td>
        <td style="text-align:center;font-weight:800">${fmt(totalVol)} m&#179;</td>
        <td style="text-align:center;font-weight:800;color:#006064">${fmt(totalProd)} ${unidade}</td>
        <td style="text-align:center;color:#e65100">M&#225;x. ${fmt(maxTaxa,1)} mL/min</td>
      </tr></tfoot>
    </table>
    <div class="g3">
      <div class="res-box" style="background:#e0f7fa;border-color:#00838f">
        <div style="font-size:.65rem;font-weight:800;color:#006064;text-transform:uppercase">Total de Produto / Ciclo</div>
        <div style="font-size:1.3rem;font-weight:900;color:#003d5c;margin-top:2px">${fmt(totalProd)} ${unidade}</div>
      </div>
      <div class="res-box" style="background:#fff3e0;border-color:#f57c00">
        <div style="font-size:.65rem;font-weight:800;color:#e65100;text-transform:uppercase">Taxa M&#225;x. de Inje&#231;&#227;o</div>
        <div style="font-size:1.3rem;font-weight:900;color:#003d5c;margin-top:2px">${estado==='L'?fmt(maxTaxa,1)+' mL/min':'—'}</div>
        <div style="font-size:.72rem;color:#607080">${estado==='L'?fmt(maxTaxaLh,2)+' L/h':''}</div>
      </div>
      <div class="res-box" style="background:#f3e5f5;border-color:#8e24aa">
        <div style="font-size:.65rem;font-weight:800;color:#6a1b9a;text-transform:uppercase">Bomba Injetora</div>
        <div style="font-size:.88rem;font-weight:800;color:#003d5c;margin-top:2px">${bombaTipo}</div>
      </div>
    </div>
    <div class="proc-box">
      <h4>&#128203; Procedimento de Aplica&#231;&#227;o &mdash; ${tipoLabel.split('—')[0].trim()}</h4>
      ${proc.split('\n').map(l=>`<div>${l}</div>`).join('')}
    </div>
    ${foot}</div>`;

  const fullHtml=`<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"><title>Clora&#231;&#227;o &mdash; Bolsa Irriga</title><style>${css}</style></head><body>${pg1}<script>window.addEventListener('load',()=>setTimeout(()=>window.print(),800));<\/script></body></html>`;
  const blob=new Blob([fullHtml],{type:'text/html;charset=utf-8'});
  const url=URL.createObjectURL(blob);
  const win=window.open(url,'_blank');
  if(!win)alert('Permita popups e tente novamente.');
  setTimeout(()=>URL.revokeObjectURL(url),120000);
}

// ── INIT ──────────────────────────────────────────────────────────────
$('data').value=new Date().toISOString().split('T')[0];
onTipo(); onProduto();
// Carregar com linhas padrão da planilha
const defaultOps=[
  ['Setor 1','98.07','120'],['Setor 2','93.33','120'],['Setor 3','86.35','120'],
  ['Setor 4','89.88','120'],['Setor 5','85.05','120'],['Setor 6','96.82','120'],
  ['Setor 7','90.27','120'],['Setor 8','93.58','120'],['Setor 9','96.89','120'],
  ['Setor 10','100.20','120'],['Setor 11','103.51','120'],['Setor 12','106.82','120'],
];
defaultOps.forEach(([d,q,t])=>addRow(q,t,d));
</script>
</body>
</html>"""

HTML = HTML.replace('##LOGO##', LOGO)
with open('cloracao.html','w',encoding='utf-8') as f:
    f.write(HTML)
print(f'OK — {len(HTML):,} bytes')
