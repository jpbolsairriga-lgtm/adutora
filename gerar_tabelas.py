#!/usr/bin/env python3
# gerar_tabelas.py → tabelas.html  (Seleção de Componentes — Casa de Bomba)

OUT = "tabelas.html"

# ── Dados das tabelas ──────────────────────────────────────────────────────────

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

import json

JS_SUCCAO      = json.dumps(SUCCAO,      ensure_ascii=False)
JS_CAVALETES   = json.dumps(CAVALETES,   ensure_ascii=False)
JS_SAIDA_BOMBAS = json.dumps(SAIDA_BOMBAS, ensure_ascii=False)

# ── Template HTML ──────────────────────────────────────────────────────────────

HTML = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Casa de Bomba — Bolsa Irriga</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Segoe UI',system-ui,sans-serif;background:linear-gradient(135deg,#003d5c 0%,#0077b6 60%,#00b4d8 100%);min-height:100vh;display:flex;flex-direction:column;align-items:center;padding:2rem 1rem}}
.logo-wrap{{margin-bottom:1.2rem;text-align:center}}
.logo-wrap img{{height:72px;width:72px;object-fit:contain;background:#fff;border-radius:14px;padding:8px;box-shadow:0 4px 20px rgba(0,0,0,.25)}}
h1{{color:#fff;font-size:1.6rem;font-weight:900;text-align:center;margin-bottom:.25rem}}
.sub{{color:rgba(255,255,255,.8);font-size:.88rem;text-align:center;margin-bottom:.4rem}}
.dev{{color:rgba(255,255,255,.65);font-size:.75rem;text-align:center;margin-bottom:1.8rem}}

/* painel entrada */
.input-panel{{background:#fff;border-radius:16px;padding:1.6rem 2rem;max-width:520px;width:100%;box-shadow:0 8px 32px rgba(0,0,0,.2);margin-bottom:1.6rem}}
.input-panel h2{{font-size:1rem;font-weight:800;color:#003d5c;margin-bottom:1rem;display:flex;align-items:center;gap:.5rem}}
.field{{display:flex;flex-direction:column;gap:.35rem;margin-bottom:1rem}}
.field label{{font-size:.8rem;font-weight:600;color:#607080}}
.field-row{{display:flex;align-items:center;gap:.6rem}}
.field input[type=number]{{flex:1;border:1.5px solid #b0cce8;border-radius:8px;padding:.55rem .8rem;font-size:1.1rem;font-weight:700;color:#003d5c;outline:none;transition:border-color .15s}}
.field input[type=number]:focus{{border-color:#0077b6}}
.unit{{font-size:.82rem;color:#607080;white-space:nowrap}}
.field input[type=text]{{flex:1;border:1.5px solid #b0cce8;border-radius:8px;padding:.5rem .8rem;font-size:.9rem;color:#1a2535;outline:none;transition:border-color .15s}}
.field input[type=text]:focus{{border-color:#0077b6}}
.btn-calc{{width:100%;background:#0077b6;color:#fff;border:none;border-radius:10px;padding:.75rem;font-size:1rem;font-weight:800;cursor:pointer;transition:background .15s}}
.btn-calc:hover{{background:#005f94}}

/* resultado */
.results{{max-width:960px;width:100%;display:grid;grid-template-columns:1fr 1fr 1fr;gap:1.2rem;margin-bottom:1.6rem}}
@media(max-width:700px){{.results{{grid-template-columns:1fr}}}}
.card{{background:#fff;border-radius:14px;padding:1.4rem 1.3rem;box-shadow:0 6px 24px rgba(0,0,0,.15);display:flex;flex-direction:column;gap:.8rem}}
.card-header{{display:flex;align-items:center;gap:.6rem;border-bottom:2px solid #e3f2fd;padding-bottom:.7rem;margin-bottom:.2rem}}
.card-header .icon{{font-size:1.6rem}}
.card-header .title{{font-size:.97rem;font-weight:800;color:#003d5c;line-height:1.2}}
.card-header .range{{font-size:.72rem;color:#0077b6;font-weight:700;margin-top:.1rem;background:#e3f2fd;border-radius:20px;padding:.1rem .5rem;display:inline-block}}
.items{{display:flex;flex-direction:column;gap:.55rem}}
.item{{display:flex;align-items:flex-start;gap:.6rem}}
.item-label{{font-size:.74rem;color:#607080;font-weight:600;min-width:110px;flex-shrink:0;padding-top:.05rem}}
.item-value{{font-size:.88rem;font-weight:700;color:#1a2535;line-height:1.35}}
.item-value.highlight{{color:#0077b6}}
.warn{{background:#fff3cd;border:1.5px solid #ffc107;border-radius:10px;padding:1rem 1.2rem;color:#856404;font-size:.88rem;font-weight:600;text-align:center;max-width:960px;width:100%;margin-bottom:1rem}}
.warn.hidden{{display:none}}
.results.hidden{{display:none}}

/* botão PDF */
.btn-pdf{{background:#fff;color:#0077b6;border:2px solid #0077b6;border-radius:10px;padding:.65rem 1.8rem;font-size:.9rem;font-weight:800;cursor:pointer;transition:background .15s,color .15s;margin-bottom:2rem}}
.btn-pdf:hover{{background:#0077b6;color:#fff}}
.btn-pdf.hidden{{display:none}}

/* footer tela */
.footer{{color:rgba(255,255,255,.5);font-size:.72rem;text-align:center;line-height:1.8;margin-top:auto;padding-top:1.5rem}}

/* ── PRINT ─────────────────────────────────────────────────────────────── */
@media print{{
  body{{background:#fff!important;padding:0;align-items:flex-start}}
  .logo-wrap,.input-panel,.btn-pdf,.footer{{display:none!important}}
  h1,.sub,.dev{{color:#003d5c!important}}
  h1{{font-size:1.2rem;margin-top:.5rem}}
  .sub{{font-size:.8rem}}
  .dev{{font-size:.7rem;margin-bottom:.8rem}}
  .results{{grid-template-columns:1fr 1fr 1fr;gap:.8rem;max-width:100%;margin-bottom:1rem;page-break-inside:avoid}}
  .card{{box-shadow:none;border:1.5px solid #b0cce8;padding:1rem .9rem}}
  .warn.hidden{{display:none}}
  .print-header{{display:block!important}}
}}
.print-header{{display:none;font-size:.8rem;color:#607080;text-align:center;margin-bottom:.5rem}}
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
  <div class="field">
    <label>Nome / Identificação do Projeto</label>
    <input type="text" id="nomeProjeto" placeholder="Ex.: Fazenda Santa Clara — Pivô 3">
  </div>
  <div class="field">
    <label>Vaz&atilde;o do Projeto</label>
    <div class="field-row">
      <input type="number" id="vazao" min="1" max="300" step="0.1" placeholder="0,0" oninput="calcular()">
      <span class="unit">m³/h</span>
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
      <div class="item"><span class="item-label">Manifold</span><span class="item-value highlight" id="s_manifold">—</span></div>
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
      <div class="item"><span class="item-label">Manifold</span><span class="item-value highlight" id="c_manifold">—</span></div>
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
      <div class="item"><span class="item-label">Manifold</span><span class="item-value highlight" id="b_manifold">—</span></div>
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

<!-- Cabeçalho visível apenas no print -->
<div class="print-header" id="printHeader"></div>

<div class="footer">
  Bolsa Irriga&reg; &mdash; Av. Elias Abr&atilde;o, n&ordm; 140 &middot; Franca &ndash; SP &middot; (16) 3702-6571 &middot; bolsairriga.com.br<br>
  &copy; 2025 Jo&atilde;o Paulo de Oliveira
</div>

<!-- Tabelas completas (visíveis apenas no PDF) -->
<div id="tabelasCompletas" style="display:none;max-width:960px;width:100%;margin-top:1.5rem"></div>

<script>
const SUCCAO = {JS_SUCCAO};
const CAVALETES = {JS_CAVALETES};
const SAIDA_BOMBAS = {JS_SAIDA_BOMBAS};

function findRow(table, v) {{
  for (const r of table) {{
    if (v >= r.min && v <= r.max) return r;
  }}
  return null;
}}

function fmt(min, max) {{
  return min + '–' + max + ' m³/h';
}}

function calcular() {{
  const v = parseFloat(document.getElementById('vazao').value);
  const warn = document.getElementById('warnBox');
  const res  = document.getElementById('results');
  const btn  = document.getElementById('btnPdf');

  if (!v || v <= 0) {{
    warn.className = 'warn hidden'; res.className = 'results hidden'; btn.className = 'btn-pdf hidden'; return;
  }}

  // Verificar cobertura (a mais restritiva é Saída de Bombas: 10-140)
  const minGlobal = 5, maxGlobal = 205;
  if (v < minGlobal || v > maxGlobal) {{
    warn.textContent = '⚠ Vazão ' + v.toFixed(1) + ' m³/h fora da faixa coberta pelas tabelas (' + minGlobal + '–' + maxGlobal + ' m³/h).';
    warn.className = 'warn';
    res.className = 'results hidden'; btn.className = 'btn-pdf hidden'; return;
  }}
  warn.className = 'warn hidden';

  const s = findRow(SUCCAO, v);
  const c = findRow(CAVALETES, v);
  const b = findRow(SAIDA_BOMBAS, v);

  // Avisos parciais
  let parciais = [];
  if (!s) parciais.push('Sucção (faixa 5–183 m³/h)');
  if (!c) parciais.push('Cavaletes (faixa 5–205 m³/h)');
  if (!b) parciais.push('Saída de Bombas (faixa 10–140 m³/h)');
  if (parciais.length) {{
    warn.textContent = '⚠ Vazão ' + v.toFixed(1) + ' m³/h fora da faixa para: ' + parciais.join(', ') + '.';
    warn.className = 'warn';
  }}

  // Sucção
  if (s) {{
    document.getElementById('rangeSuccao').textContent = fmt(s.min, s.max);
    document.getElementById('s_manifold').textContent = s.manifold;
    document.getElementById('s_retencao').textContent = s.retencao;
    document.getElementById('s_crivo').textContent    = s.crivo;
    document.getElementById('cardSuccao').style.opacity = '1';
  }} else {{
    document.getElementById('rangeSuccao').textContent = 'Fora da faixa';
    ['s_manifold','s_retencao','s_crivo'].forEach(id => document.getElementById(id).textContent = '—');
    document.getElementById('cardSuccao').style.opacity = '.45';
  }}

  // Cavaletes
  if (c) {{
    document.getElementById('rangeCav').textContent = fmt(c.min, c.max);
    document.getElementById('c_manifold').textContent = c.manifold;
    document.getElementById('c_valv').textContent     = c.valv;
    document.getElementById('c_ventosa').textContent  = c.ventosa;
    document.getElementById('c_antivacuo').textContent= c.antivacuo;
    document.getElementById('c_piloto').textContent   = c.piloto;
    document.getElementById('c_saida').textContent    = c.saida;
    document.getElementById('cardCav').style.opacity = '1';
  }} else {{
    document.getElementById('rangeCav').textContent = 'Fora da faixa';
    ['c_manifold','c_valv','c_ventosa','c_antivacuo','c_piloto','c_saida'].forEach(id => document.getElementById(id).textContent = '—');
    document.getElementById('cardCav').style.opacity = '.45';
  }}

  // Saída de Bombas
  if (b) {{
    document.getElementById('rangeSaida').textContent  = fmt(b.min, b.max);
    document.getElementById('b_manifold').textContent  = b.manifold;
    document.getElementById('b_valv').textContent      = b.valv;
    document.getElementById('b_hidrometro').textContent= b.hidrometro;
    document.getElementById('b_alivio').textContent    = b.alivio;
    document.getElementById('b_filtro').textContent    = b.filtro;
    document.getElementById('b_pig').textContent       = b.pig;
    document.getElementById('b_retencao').textContent  = b.retencao;
    document.getElementById('b_adutora').textContent   = b.adutora;
    document.getElementById('cardSaida').style.opacity = '1';
  }} else {{
    document.getElementById('rangeSaida').textContent = 'Fora da faixa';
    ['b_manifold','b_valv','b_hidrometro','b_alivio','b_filtro','b_pig','b_retencao','b_adutora'].forEach(id => document.getElementById(id).textContent = '—');
    document.getElementById('cardSaida').style.opacity = '.45';
  }}

  res.className = 'results';
  btn.className = 'btn-pdf';
}}

function gerarPDF() {{
  const v    = parseFloat(document.getElementById('vazao').value);
  const nome = document.getElementById('nomeProjeto').value.trim();
  const ph   = document.getElementById('printHeader');
  const data = new Date().toLocaleDateString('pt-BR', {{day:'2-digit',month:'2-digit',year:'numeric'}});
  let txt = 'Vaz&atilde;o do projeto: <b>' + v.toFixed(1) + ' m³/h</b>';
  if (nome) txt = '<b>' + nome + '</b> &nbsp;|&nbsp; ' + txt;
  txt += ' &nbsp;|&nbsp; Data: ' + data;
  ph.innerHTML = txt;

  // Montar tabelas completas
  buildTabelasCompletas(v);
  document.getElementById('tabelasCompletas').style.display = 'block';

  window.print();

  setTimeout(() => {{
    document.getElementById('tabelasCompletas').style.display = 'none';
  }}, 500);
}}

function buildTabelasCompletas(v) {{
  const wrap = document.getElementById('tabelasCompletas');

  const styleTab = `border-collapse:collapse;width:100%;font-size:.75rem;margin-top:.4rem`;
  const styleTh  = `background:#003d5c;color:#fff;padding:.3rem .5rem;text-align:left;font-size:.7rem`;
  const styleTd  = `padding:.3rem .5rem;border-bottom:1px solid #e0e0e0`;
  const styleHl  = `background:#e3f2fd;font-weight:700`;

  function buildTable(title, headers, rows, matchFn, rowMapper) {{
    let html = `<div style="margin-bottom:1rem">
      <div style="font-size:.8rem;font-weight:800;color:#003d5c;margin-bottom:.3rem">${{title}}</div>
      <table style="${{styleTab}}"><thead><tr>`;
    headers.forEach(h => html += `<th style="${{styleTh}}">${{h}}</th>`);
    html += `</tr></thead><tbody>`;
    rows.forEach(r => {{
      const isMatch = matchFn(r, v);
      const tr = `style="${{isMatch ? styleHl : ''}}`;
      html += `<tr ${{tr}}>`;
      rowMapper(r).forEach(cell => html += `<td style="${{styleTd}}${{isMatch ? ';font-weight:700' : ''}}">${{cell}}</td>`);
      html += `</tr>`;
    }});
    html += `</tbody></table></div>`;
    return html;
  }}

  const inRange = (r, v) => v >= r.min && v <= r.max;

  let html = `<div style="font-size:.78rem;font-weight:700;color:#003d5c;border-top:2px solid #003d5c;padding-top:.6rem;margin-bottom:.8rem">Tabelas Completas de Referência</div>`;

  html += buildTable('Tabela de Sucção',
    ['Vazão (m³/h)', 'Manifold', 'Retenção', 'Crivo'],
    SUCCAO, inRange,
    r => [r.min + '–' + r.max, r.manifold, r.retencao, r.crivo]
  );

  html += buildTable('Tabela de Cavaletes',
    ['Vazão (m³/h)', 'Manifold', 'Válv. Hidráulica', 'Ventosa', 'Anti-Vácuo', 'Piloto', 'PVC Saída'],
    CAVALETES, inRange,
    r => [r.min + '–' + r.max, r.manifold, r.valv, r.ventosa, r.antivacuo, r.piloto, r.saida]
  );

  html += buildTable('Tabela de Saída de Bombas',
    ['Vazão (m³/h)', 'Manifold', 'Válv. Hidráulica', 'Hidrômetro', 'Alívio', 'Filtro PIG', 'PIG Manifold', 'Retenção', 'Adutora'],
    SAIDA_BOMBAS, inRange,
    r => [r.min + '–' + r.max, r.manifold, r.valv, r.hidrometro, r.alivio, r.filtro, r.pig, r.retencao, r.adutora]
  );

  wrap.innerHTML = html;
}}
</script>
</body>
</html>
"""

with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)

size = len(HTML)
print(f"OK - {size:,} bytes - {OUT}")
