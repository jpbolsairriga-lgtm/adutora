import base64, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('logo perfil branca.png','rb') as f:
    LOGO = base64.b64encode(f.read()).decode()

# ── Dados das tabelas ──────────────────────────────────────────────────────────

import json

SUCCAO = [
    {"min": 5,  "max": 19,  "manifold": "75mm",  "retencao": '3"',  "crivo": '3"'},
    {"min": 19, "max": 28,  "manifold": "90mm",  "retencao": '3"',  "crivo": '3"'},
    {"min": 28, "max": 44,  "manifold": "110mm", "retencao": '4"',  "crivo": '4"'},
    {"min": 44, "max": 92,  "manifold": "160mm", "retencao": '6"',  "crivo": '6"'},
    {"min": 92, "max": 183, "manifold": "225mm", "retencao": '8"',  "crivo": '8"'},
]

CAVALETES = [
    {"min": 5,   "max": 32,  "manifold": "75mm",  "valv": "75-2",   "ventosa": '1"',  "antivacuo": '1/2"-1"', "piloto": "29/200", "saida": "50/75/100mm"},
    {"min": 32,  "max": 41,  "manifold": "90mm",  "valv": "75-3",   "ventosa": '1"',  "antivacuo": '1/2"-1"', "piloto": "29/200", "saida": "75/100/125mm"},
    {"min": 41,  "max": 68,  "manifold": "90mm",  "valv": "96-90",  "ventosa": '1"',  "antivacuo": '1/2"-1"', "piloto": "29/200", "saida": "100/125/150mm"},
    {"min": 68,  "max": 106, "manifold": "110mm", "valv": "96-110", "ventosa": '2"',  "antivacuo": '2"',      "piloto": "29/200", "saida": "125/150mm"},
    {"min": 106, "max": 205, "manifold": "160mm", "valv": "96-160", "ventosa": '2"',  "antivacuo": '2"',      "piloto": "29/200", "saida": "150mm"},
]

SAIDA_BOMBAS = [
    {"min": 10, "max": 28,  "manifold": "75mm",  "valv": "44-2", "hidrometro": '2 1/2"', "alivio": '2"', "filtro": "2x20", "pig": "75mm",  "retencao": '3"', "adutora": "75/100mm (defofo)"},
    {"min": 28, "max": 40,  "manifold": "90mm",  "valv": "47-3", "hidrometro": '3"',     "alivio": '2"', "filtro": "2x24", "pig": "90mm",  "retencao": '3"', "adutora": "100mm (defofo)"},
    {"min": 40, "max": 60,  "manifold": "90mm",  "valv": "47-3", "hidrometro": '3"',     "alivio": '2"', "filtro": "3x24", "pig": "90mm",  "retencao": '3"', "adutora": "100/150mm (defofo)"},
    {"min": 60, "max": 90,  "manifold": "110mm", "valv": "47-4", "hidrometro": '4"',     "alivio": '2"', "filtro": "4x24", "pig": "110mm", "retencao": '4"', "adutora": "150mm (defofo)"},
    {"min": 90, "max": 140, "manifold": "160mm", "valv": "47-6", "hidrometro": '6"',     "alivio": '3"', "filtro": "3x36", "pig": "160mm", "retencao": '6"', "adutora": "150/200mm (defofo)"},
]

JS_SUCCAO       = json.dumps(SUCCAO,       ensure_ascii=False)
JS_CAVALETES    = json.dumps(CAVALETES,    ensure_ascii=False)
JS_SAIDA_BOMBAS = json.dumps(SAIDA_BOMBAS, ensure_ascii=False)

# ── Template HTML ──────────────────────────────────────────────────────────────

HTML = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Casa de Bomba — Bolsa Irriga</title>
<style>
:root{
  --bl:#003d5c;--bl2:#0077b6;--bl3:#00b4d8;--bl4:#e3f2fd;
  --bg:#f4f7fb;--bdr:#d0e4f0;--tx:#1a2535;--mu:#607080;
  --sh:0 2px 16px rgba(0,80,160,.10);
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI',system-ui,sans-serif;background:linear-gradient(135deg,#003d5c 0%,#0077b6 60%,#00b4d8 100%);min-height:100vh;display:flex;flex-direction:column;align-items:center;padding:2rem 1rem}
.logo-wrap{margin-bottom:1.2rem;text-align:center}
.logo-wrap img{height:72px;width:72px;object-fit:contain;background:#fff;border-radius:14px;padding:8px;box-shadow:0 4px 20px rgba(0,0,0,.25)}
h1{color:#fff;font-size:1.6rem;font-weight:900;text-align:center;margin-bottom:.25rem}
.sub{color:rgba(255,255,255,.8);font-size:.88rem;text-align:center;margin-bottom:.4rem}
.dev{color:rgba(255,255,255,.65);font-size:.75rem;text-align:center;margin-bottom:1.8rem}

/* painel entrada */
.input-panel{background:#fff;border-radius:16px;padding:1.6rem 2rem;max-width:580px;width:100%;box-shadow:0 8px 32px rgba(0,0,0,.2);margin-bottom:1.6rem}
.input-panel h2{font-size:1rem;font-weight:800;color:#003d5c;margin-bottom:1rem}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:.8rem}
@media(max-width:480px){.g2{grid-template-columns:1fr}}
.field{display:flex;flex-direction:column;gap:.3rem}
.field label{font-size:.72rem;font-weight:700;color:#607080;text-transform:uppercase;letter-spacing:.04em}
.iu{display:flex}
.iu input{flex:1;border-radius:8px 0 0 8px}
.iu .u{background:#e3f2fd;border:1.5px solid #b0cce8;border-left:none;padding:.48rem .6rem;font-size:.78rem;color:#607080;border-radius:0 8px 8px 0;white-space:nowrap;display:flex;align-items:center}
input[type=number],input[type=text],input[type=date]{padding:.48rem .68rem;border:1.5px solid #b0cce8;border-radius:8px;font-size:.9rem;color:#1a2535;background:#fafeff;outline:none;transition:border-color .18s;width:100%}
input:focus{border-color:#0077b6;box-shadow:0 0 0 3px rgba(0,119,182,.12)}
.btn-calc{width:100%;background:#0077b6;color:#fff;border:none;border-radius:10px;padding:.75rem;font-size:1rem;font-weight:800;cursor:pointer;transition:background .15s;margin-top:.4rem}
.btn-calc:hover{background:#005f94}

/* resultado */
.results{max-width:960px;width:100%;display:grid;grid-template-columns:1fr 1fr 1fr;gap:1.2rem;margin-bottom:1.6rem}
@media(max-width:700px){.results{grid-template-columns:1fr}}
.card{background:#fff;border-radius:14px;padding:1.4rem 1.3rem;box-shadow:0 6px 24px rgba(0,0,0,.15);display:flex;flex-direction:column;gap:.8rem}
.card-header{display:flex;align-items:center;gap:.6rem;border-bottom:2px solid #e3f2fd;padding-bottom:.7rem;margin-bottom:.2rem}
.card-header .icon{font-size:1.6rem}
.card-header .title{font-size:.97rem;font-weight:800;color:#003d5c;line-height:1.2}
.card-header .range{font-size:.72rem;color:#0077b6;font-weight:700;margin-top:.1rem;background:#e3f2fd;border-radius:20px;padding:.1rem .5rem;display:inline-block}
.items{display:flex;flex-direction:column;gap:.5rem}
.item{display:flex;align-items:flex-start;gap:.6rem}
.item-label{font-size:.74rem;color:#607080;font-weight:600;min-width:115px;flex-shrink:0;padding-top:.05rem}
.item-value{font-size:.88rem;font-weight:700;color:#1a2535;line-height:1.35}
.item-value.hi{color:#0077b6}
.warn{background:#fff3cd;border:1.5px solid #ffc107;border-radius:10px;padding:1rem 1.2rem;color:#856404;font-size:.88rem;font-weight:600;text-align:center;max-width:960px;width:100%;margin-bottom:1rem}
.hidden{display:none!important}

/* botão PDF */
.btn-pdf{background:#fff;color:#0077b6;border:2px solid #0077b6;border-radius:10px;padding:.65rem 1.8rem;font-size:.9rem;font-weight:800;cursor:pointer;transition:background .15s,color .15s;margin-bottom:2rem}
.btn-pdf:hover{background:#0077b6;color:#fff}

.footer{color:rgba(255,255,255,.5);font-size:.72rem;text-align:center;line-height:1.8;margin-top:auto;padding-top:1.5rem}
</style>
</head>
<body>

<div class="logo-wrap">
  <img src="logo perfil branca.png" alt="Bolsa Irriga" onerror="this.style.display='none'">
</div>
<h1>Casa de Bomba</h1>
<p class="sub">Sele&ccedil;&atilde;o de Componentes por Vaz&atilde;o</p>
<p class="dev">Jo&atilde;o Paulo de Oliveira &middot; Engenheiro Agr&ocirc;nomo &middot; Especialista em Irriga&ccedil;&atilde;o</p>

<!-- Painel entrada -->
<div class="input-panel">
  <h2>&#9881; Dados do Projeto</h2>
  <div class="g2" style="margin-bottom:.8rem">
    <div class="field">
      <label>Consultor</label>
      <input type="text" id="consultor" placeholder="Nome do consultor">
    </div>
    <div class="field">
      <label>Cliente</label>
      <input type="text" id="cliente" placeholder="Nome do cliente">
    </div>
    <div class="field">
      <label>Propriedade</label>
      <input type="text" id="propriedade" placeholder="Nome da propriedade">
    </div>
    <div class="field">
      <label>Cidade / UF</label>
      <input type="text" id="cidade" placeholder="Ex.: Franca / SP">
    </div>
  </div>
  <div class="g2" style="margin-bottom:.8rem">
    <div class="field">
      <label>Data</label>
      <input type="date" id="data">
    </div>
    <div class="field">
      <label>Vaz&atilde;o do Projeto</label>
      <div class="iu">
        <input type="number" id="vazao" min="1" max="300" step="0.1" placeholder="0,0" oninput="calcular()">
        <span class="u">m³/h</span>
      </div>
    </div>
  </div>
  <button class="btn-calc" onclick="calcular()">Selecionar Componentes</button>
</div>

<!-- Aviso fora de faixa -->
<div class="warn hidden" id="warnBox"></div>

<!-- Resultados -->
<div class="results hidden" id="results">

  <!-- Sucção -->
  <div class="card" id="cardSuccao">
    <div class="card-header">
      <span class="icon">&#129352;</span>
      <div>
        <div class="title">Tubula&ccedil;&atilde;o de Suc&ccedil;&atilde;o</div>
        <span class="range" id="rangeSuccao"></span>
      </div>
    </div>
    <div class="items">
      <div class="item"><span class="item-label">Manifold</span><span class="item-value hi" id="s_manifold">—</span></div>
      <div class="item"><span class="item-label">Reten&ccedil;&atilde;o</span><span class="item-value" id="s_retencao">—</span></div>
      <div class="item"><span class="item-label">Crivo</span><span class="item-value" id="s_crivo">—</span></div>
    </div>
  </div>

  <!-- Cavaletes -->
  <div class="card" id="cardCav">
    <div class="card-header">
      <span class="icon">&#128268;</span>
      <div>
        <div class="title">Cavaletes</div>
        <span class="range" id="rangeCav"></span>
      </div>
    </div>
    <div class="items">
      <div class="item"><span class="item-label">Manifold</span><span class="item-value hi" id="c_manifold">—</span></div>
      <div class="item"><span class="item-label">Válv. Hidráulica</span><span class="item-value" id="c_valv">—</span></div>
      <div class="item"><span class="item-label">Ventosa</span><span class="item-value" id="c_ventosa">—</span></div>
      <div class="item"><span class="item-label">Anti-Vácuo</span><span class="item-value" id="c_antivacuo">—</span></div>
      <div class="item"><span class="item-label">Piloto</span><span class="item-value" id="c_piloto">—</span></div>
      <div class="item"><span class="item-label">PVC Saída</span><span class="item-value" id="c_saida">—</span></div>
    </div>
  </div>

  <!-- Saída de Bombas -->
  <div class="card" id="cardSaida">
    <div class="card-header">
      <span class="icon">&#128161;</span>
      <div>
        <div class="title">Sa&iacute;da de Bombas</div>
        <span class="range" id="rangeSaida"></span>
      </div>
    </div>
    <div class="items">
      <div class="item"><span class="item-label">Manifold</span><span class="item-value hi" id="b_manifold">—</span></div>
      <div class="item"><span class="item-label">Válv. Hidráulica</span><span class="item-value" id="b_valv">—</span></div>
      <div class="item"><span class="item-label">Hidrômetro</span><span class="item-value" id="b_hidrometro">—</span></div>
      <div class="item"><span class="item-label">Alívio</span><span class="item-value" id="b_alivio">—</span></div>
      <div class="item"><span class="item-label">Filtro PIG</span><span class="item-value" id="b_filtro">—</span></div>
      <div class="item"><span class="item-label">PIG Manifold</span><span class="item-value" id="b_pig">—</span></div>
      <div class="item"><span class="item-label">Retenção</span><span class="item-value" id="b_retencao">—</span></div>
      <div class="item"><span class="item-label">Adutora</span><span class="item-value" id="b_adutora">—</span></div>
    </div>
  </div>

</div>

<!-- Botão PDF -->
<button class="btn-pdf hidden" id="btnPdf" onclick="gerarPDF()">&#128438; Gerar Relat&oacute;rio PDF</button>

<div class="footer">
  Bolsa Irriga&reg; &mdash; Av. Elias Abr&atilde;o, n&ordm; 140 &middot; Franca &ndash; SP &middot; (16) 3702-6571 &middot; bolsairriga.com.br<br>
  &copy; 2025 Jo&atilde;o Paulo de Oliveira
</div>

<script>
const SUCCAO      = ##SUCCAO##;
const CAVALETES   = ##CAVALETES##;
const SAIDA_BOMBAS= ##SAIDA_BOMBAS##;
const LOGO_B64    = '##LOGO##';

function $(id){return document.getElementById(id)}
function gv(id){return parseFloat($(id).value)||0}
function gvs(id){return $(id).value.trim()}

function findRow(table,v){
  for(const r of table) if(v>=r.min && v<=r.max) return r;
  return null;
}
function fmt(min,max){return min+'–'+max+' m³/h'}

function calcular(){
  const v=gv('vazao');
  const warn=$('warnBox'), res=$('results'), btn=$('btnPdf');
  if(!v||v<=0){warn.className='warn hidden';res.className='results hidden';btn.className='btn-pdf hidden';return;}

  if(v<5||v>205){
    warn.textContent='⚠ Vazão '+v.toFixed(1)+' m³/h fora da faixa coberta (5–205 m³/h).';
    warn.className='warn';res.className='results hidden';btn.className='btn-pdf hidden';return;
  }
  warn.className='warn hidden';

  const s=findRow(SUCCAO,v), c=findRow(CAVALETES,v), b=findRow(SAIDA_BOMBAS,v);

  let parciais=[];
  if(!s) parciais.push('Sucção (5–183 m³/h)');
  if(!c) parciais.push('Cavaletes (5–205 m³/h)');
  if(!b) parciais.push('Saída de Bombas (10–140 m³/h)');
  if(parciais.length){warn.textContent='⚠ Fora da faixa para: '+parciais.join(', ')+'.';warn.className='warn';}

  function fill(card,rangeId,ids,row){
    if(row){
      $(rangeId).textContent=fmt(row.min,row.max);
      ids.forEach(([id,key])=>$(id).textContent=row[key]||'—');
      $(card).style.opacity='1';
    } else {
      $(rangeId).textContent='Fora da faixa';
      ids.forEach(([id])=>$(id).textContent='—');
      $(card).style.opacity='.45';
    }
  }

  fill('cardSuccao','rangeSuccao',[['s_manifold','manifold'],['s_retencao','retencao'],['s_crivo','crivo']],s);
  fill('cardCav','rangeCav',[['c_manifold','manifold'],['c_valv','valv'],['c_ventosa','ventosa'],['c_antivacuo','antivacuo'],['c_piloto','piloto'],['c_saida','saida']],c);
  fill('cardSaida','rangeSaida',[['b_manifold','manifold'],['b_valv','valv'],['b_hidrometro','hidrometro'],['b_alivio','alivio'],['b_filtro','filtro'],['b_pig','pig'],['b_retencao','retencao'],['b_adutora','adutora']],b);

  res.className='results';
  btn.className='btn-pdf';
}

function gerarPDF(){
  const v=gv('vazao');
  if(!v||v<=0) return;
  const cons=gvs('consultor'), cli=gvs('cliente'), prop=gvs('propriedade'), cid=gvs('cidade');
  const dtRaw=gvs('data');
  const dt=dtRaw?new Date(dtRaw+'T12:00:00').toLocaleDateString('pt-BR'):'—';

  const s=findRow(SUCCAO,v), c=findRow(CAVALETES,v), b=findRow(SAIDA_BOMBAS,v);

  const css=`
*{box-sizing:border-box;margin:0;padding:0;font-family:'Segoe UI',sans-serif}
body{font-size:10pt;color:#1a2535;background:#fff}
.pg{padding:8mm 12mm;page-break-after:always;min-height:270mm}.pg:last-child{page-break-after:avoid}
.hd{background:linear-gradient(135deg,#003d5c,#0077b6,#00b4d8);color:#fff;padding:6px 12px;display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;border-radius:4px}
.hl{display:flex;align-items:center;gap:8px}.hl img{height:40px;width:40px;background:#fff;border-radius:6px;padding:3px;object-fit:contain}
.hb h2{font-size:.95rem;font-weight:800}.hb p{font-size:.65rem;opacity:.85}
.hr2{text-align:right;font-size:.65rem;line-height:1.6}.hr2 b{font-size:.78rem;display:block}
.cli{background:#e3f2fd;border:1px solid #b0cce8;border-radius:4px;padding:5px 10px;display:grid;grid-template-columns:repeat(5,1fr);gap:4px;margin-bottom:8px;font-size:.76rem}
.cf label{font-size:.6rem;font-weight:800;color:#607080;text-transform:uppercase;display:block}
.cf span{font-weight:700;color:#003d5c}
.st{font-size:.72rem;font-weight:900;color:#0077b6;text-transform:uppercase;letter-spacing:.06em;padding:3px 0 4px;border-bottom:1.5px solid #b0cce8;margin:8px 0 5px;display:flex;align-items:center;gap:4px}
.st::before{content:'';width:3px;height:1em;background:#0077b6;border-radius:2px;flex-shrink:0}
.g3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-bottom:10px}
.sec{border:1.5px solid #b0cce8;border-radius:6px;padding:8px 10px;background:#f8fbff}
.sec-title{font-size:.7rem;font-weight:900;color:#003d5c;text-transform:uppercase;letter-spacing:.05em;margin-bottom:6px;padding-bottom:3px;border-bottom:1px solid #d0e4f0}
.row{display:flex;align-items:baseline;gap:4px;margin-bottom:3px}
.row .lbl{font-size:.65rem;color:#607080;font-weight:600;min-width:90px;flex-shrink:0}
.row .val{font-size:.8rem;font-weight:700;color:#1a2535}
.row .val.hi{color:#0077b6;font-size:.88rem}
.range-badge{display:inline-block;background:#0077b6;color:#fff;font-size:.62rem;font-weight:800;border-radius:10px;padding:.1rem .5rem;margin-bottom:5px}
.tbl{width:100%;border-collapse:collapse;font-size:.72rem;margin-top:4px}
.tbl th{padding:3px 5px;font-size:.63rem;font-weight:800;text-transform:uppercase;text-align:center;background:#003d5c;color:#fff;border:1px solid #005f94}
.tbl th.l{text-align:left}
.tbl td{padding:3px 5px;border:1px solid #d0e4f0;text-align:center}
.tbl tr.match{background:#e3f2fd;font-weight:800}
.tbl tr.match td{color:#003d5c;border-color:#90caf9}
.tbl tr:not(.match):nth-child(even) td{background:#f4f8ff}
.faixa{font-size:.68rem;font-weight:700}
.ft{border-top:1px solid #d0e4f0;padding-top:4px;margin-top:8px;display:flex;justify-content:space-between;font-size:.62rem;color:#607080}
.ft img{height:18px;width:18px;object-fit:contain;border-radius:3px;background:#f0f7ff;padding:2px;border:1px solid #d0e4f0;vertical-align:middle;margin-right:3px}
@media print{*{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}body{margin:0}.pg{padding:5mm 9mm}}`;

  const hdr=`<div class="hd"><div class="hl"><img src="data:image/png;base64,${LOGO_B64}" alt=""><div class="hb"><h2>Bolsa Irriga&#174; &#8212; Casa de Bomba</h2><p>Sele&#231;&#227;o de Componentes por Vaz&#227;o</p></div></div><div class="hr2"><b>Jo&#227;o Paulo de Oliveira</b>Eng. Agr&#244;nomo &#183; Esp. Irriga&#231;&#227;o<br>bolsairriga.com.br &#183; (16) 3702-6571</div></div>`;
  const cliHtml=`<div class="cli"><div class="cf"><label>Consultor</label><span>${cons||'&#8212;'}</span></div><div class="cf"><label>Cliente</label><span>${cli||'&#8212;'}</span></div><div class="cf"><label>Propriedade</label><span>${prop||'&#8212;'}</span></div><div class="cf"><label>Cidade/UF</label><span>${cid||'&#8212;'}</span></div><div class="cf"><label>Data</label><span>${dt}</span></div></div>`;
  const foot=`<div class="ft"><div><img src="data:image/png;base64,${LOGO_B64}" alt=""> Bolsa Irriga&#174; &#183; Av. Elias Abr&#227;o, 140 &#183; Franca &#8211; SP</div><div>Jo&#227;o Paulo de Oliveira &#183; Eng. Agr&#244;nomo</div></div>`;

  function secCard(icon,title,row,rows){
    if(!row) return `<div class="sec"><div class="sec-title">${icon} ${title}</div><p style="color:#c62828;font-size:.75rem">Fora da faixa para esta vaz&#227;o.</p></div>`;
    return `<div class="sec">
      <div class="sec-title">${icon} ${title}</div>
      <span class="range-badge">${row.min}&#8211;${row.max} m&#179;/h</span>
      ${rows.map(([lbl,key])=>`<div class="row"><span class="lbl">${lbl}</span><span class="val${key==='manifold'?' hi':''}">${row[key]||'&#8212;'}</span></div>`).join('')}
    </div>`;
  }

  const pg1=`<div class="pg">${hdr}${cliHtml}
  <div class="st">Vaz&#227;o do Projeto: ${v.toFixed(1)} m&#179;/h</div>
  <div class="g3">
    ${secCard('&#129352;','Tubula&#231;&#227;o de Suc&#231;&#227;o',s,[['Manifold','manifold'],['Reten&#231;&#227;o','retencao'],['Crivo','crivo']])}
    ${secCard('&#128268;','Cavaletes',c,[['Manifold','manifold'],['V&#225;lv. Hidr&#225;ulica','valv'],['Ventosa','ventosa'],['Anti-V&#225;cuo','antivacuo'],['Piloto','piloto'],['PVC Sa&#237;da','saida']])}
    ${secCard('&#128161;','Sa&#237;da de Bombas',b,[['Manifold','manifold'],['V&#225;lv. Hidr&#225;ulica','valv'],['Hidr&#244;metro','hidrometro'],['Al&#237;vio','alivio'],['Filtro PIG','filtro'],['PIG Manifold','pig'],['Reten&#231;&#227;o','retencao'],['Adutora','adutora']])}
  </div>
  ${foot}</div>`;

  function buildFullTable(title,headers,data,matchFn,rowMapper){
    let rows='';
    data.forEach(r=>{
      const m=matchFn(r,v);
      rows+=`<tr class="${m?'match':''}">${rowMapper(r).map(c=>`<td>${c}</td>`).join('')}</tr>`;
    });
    return `<div style="margin-bottom:10px">
      <div class="st">${title}</div>
      <table class="tbl"><thead><tr>${headers.map((h,i)=>`<th class="${i===0?'l':''}">${h}</th>`).join('')}</tr></thead>
      <tbody>${rows}</tbody></table></div>`;
  }

  const inRange=(r,v)=>v>=r.min&&v<=r.max;

  const pg2=`<div class="pg">${hdr}${cliHtml}
  <div class="st">Tabelas Completas de Refer&#234;ncia &#8212; Vaz&#227;o: ${v.toFixed(1)} m&#179;/h <span style="font-size:.65rem;background:#e3f2fd;color:#0077b6;border-radius:8px;padding:1px 6px;margin-left:4px">linha destacada = faixa selecionada</span></div>
  ${buildFullTable('Tabela de Suc&#231;&#227;o',['Vaz&#227;o (m&#179;/h)','Manifold','Reten&#231;&#227;o','Crivo'],SUCCAO,inRange,r=>[r.min+'&#8211;'+r.max,r.manifold,r.retencao,r.crivo])}
  ${buildFullTable('Tabela de Cavaletes',['Vaz&#227;o (m&#179;/h)','Manifold','V&#225;lv. Hidr&#225;ulica','Ventosa','Anti-V&#225;cuo','Piloto','PVC Sa&#237;da'],CAVALETES,inRange,r=>[r.min+'&#8211;'+r.max,r.manifold,r.valv,r.ventosa,r.antivacuo,r.piloto,r.saida])}
  ${buildFullTable('Tabela de Sa&#237;da de Bombas',['Vaz&#227;o (m&#179;/h)','Manifold','V&#225;lv. Hidr&#225;ulica','Hidr&#244;metro','Al&#237;vio','Filtro PIG','PIG Manifold','Reten&#231;&#227;o','Adutora'],SAIDA_BOMBAS,inRange,r=>[r.min+'&#8211;'+r.max,r.manifold,r.valv,r.hidrometro,r.alivio,r.filtro,r.pig,r.retencao,r.adutora])}
  ${foot}</div>`;

  const fullHtml=`<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"><title>Casa de Bomba &#8212; Bolsa Irriga</title><style>${css}</style></head><body>${pg1}${pg2}<script>window.addEventListener('load',()=>setTimeout(()=>window.print(),800));<\/script></body></html>`;
  const blob=new Blob([fullHtml],{type:'text/html;charset=utf-8'});
  const url=URL.createObjectURL(blob);
  const win=window.open(url,'_blank');
  if(!win) alert('Permita popups e tente novamente.');
  setTimeout(()=>URL.revokeObjectURL(url),120000);
}

document.getElementById('data').value=new Date().toISOString().split('T')[0];
</script>
</body>
</html>"""

HTML = HTML.replace('##LOGO##', LOGO)
HTML = HTML.replace('##SUCCAO##', JS_SUCCAO)
HTML = HTML.replace('##CAVALETES##', JS_CAVALETES)
HTML = HTML.replace('##SAIDA_BOMBAS##', JS_SAIDA_BOMBAS)

with open('tabelas.html','w',encoding='utf-8') as f:
    f.write(HTML)
print(f'OK - {len(HTML):,} bytes - tabelas.html')
