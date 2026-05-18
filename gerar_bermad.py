import sys, json, shutil, os
sys.stdout.reconfigure(encoding='utf-8')

# ── Índice completo ────────────────────────────────────────────────────────────
# label "X-N-M" = 2 páginas (N a M); "X-N" = 1 página
# pdfPage calculado abaixo

RAW = [
  # A - Accessories
  ("A","PC-Sharp-X-P","A-1","Positioning 3-Way Sharp Mini-Pilot Valve, Plastic"),
  ("A","PC-Sharp-X-M","A-2","Positioning 3-Way Sharp Mini-Pilot Valve, Metal"),
  ("A","PC-S-A-P","A-3","Pressure Reducing Servo 2/3-Way Mini-Pilot Valve, Plastic"),
  ("A","PC-S-A-M","A-4","Pressure Reducing Servo 2/3-Way Mini-Pilot Valve, Metal"),
  ("A","PC-20-A-P","A-5","Pressure Reducing 2-Way Mini-Pilot Valve, Plastic"),
  ("A","PC-20-A-M","A-6","Pressure Reducing 2-Way Mini-Pilot Valve, Metal"),
  ("A","PC-30-A-P","A-7","Pressure Sustaining 2-Way Mini-Pilot Valve, Plastic"),
  ("A","PC-30-A-M","A-8","Pressure Sustaining 2-Way Mini-Pilot Valve, Metal"),
  ("A","PC-3Q-A-P","A-9","Quick Pressure Relief Mini-Pilot Valve, Plastic"),
  ("A","PC-3Q-A-M","A-10","Quick Pressure Relief Mini-Pilot Valve, Metal"),
  ("A","PC-70-A-P","A-11","Paddle Flow Rate Servo Mini-Pilot Valve, Plastic"),
  ("A","PC-70-A-M","A-12","Paddle Flow Rate Servo Mini-Pilot Valve, Metal"),
  ("A","#X","A-13","Positioning 3-Way Pilot Valve"),
  ("A","#2","A-14","Pressure Reducing Pilot Valve"),
  ("A","#3","A-15","Pressure Sustaining Pilot Valve"),
  ("A","#8","A-16","Altitude Positioning Pilot Valve"),
  ("A","3W-SOP","A-17","3-Way Shut-Off Pilot for AMV"),
  ("A","5W-SSOP","A-18","5-Way Sequential Shut-off Pilot for AMV"),
  ("A","3W-SOP-S","A-19","3-Way Shut-Off Pilot Valve with Pump Shut-Off Electrical Switch"),
  ("A","S-390-2W","A-20","2-Way Solenoid Valves (Burkert 5281)"),
  ("A","S-390-3W / S-400-3W","A-21","3-Way Solenoid Valves (Burkert 330)"),
  ("A","S-400-3W (Burkert 6014)","A-22","3-Way Solenoid Valves"),
  ("A","S-392-2W","A-23","2-Way Latching Solenoid Valves"),
  ("A","S-982/985 / S-402","A-24","3-Way Magnetic Latch Solenoid Valves"),
  ("A","In-Line/Y-Strainer","A-25","Control Filters"),
  ("A","2-Way/3-Way Ball Valves","A-26","Ball Valves — Manometer"),
  ("A","4-Way Ball Valves","A-27","Ball Valves — Manual Selector"),
  ("A","50-P/M","A-28","2-Way Hydraulic Relay Valves (2W-HRV)"),
  ("A","54-PZ/M","A-29","3-Way Hydraulic Relay Valves (3W-HRV)"),
  ("A","50-X-P/M","A-30","Shuttle Valves"),
  ("A","Flow Control (One-Way)","A-31","Flow Control Valves — One-Way"),
  ("A","Needle Valve","A-32","Flow Control Valves — Needle/Restriction"),
  ("A","20-P/M","A-33","Check Valves"),
  ("A","#66 / #60-P/M","A-34","Floats"),
  # B - On/Off
  ("B","N05-Z","B-1","Hydraulic Control Valve"),
  ("B","900-DO","B-2","Automatic Metering Valve (AMV)"),
  ("B","900-DD","B-3","Automatic Metering Valve (AMV) for Sequential Irrigation"),
  ("B","N05-54-KX","B-4","Hydraulic Control Valve N.C. with Hydraulic Relay"),
  ("B","N05-54-RXZ","B-5","Hydraulic Control Valve N.C. with Hydraulic Relay"),
  ("B","N10-KX","B-6","Solenoid Controlled Valve"),
  ("B","N10-N1-2W","B-7","Solenoid Controlled Valve with 2-Way Internal Control"),
  ("B","N10-RX","B-8-9","Solenoid Controlled Valve"),
  # C - Pressure Reducing
  ("C","N20-K","C-1","Pressure Reducing 2-Way Valve"),
  ("C","N20-R","C-2-3","Pressure Reducing 2-Way Valve"),
  ("C","N20-50-K","C-4","Pressure Reducing 2-Way Valve with Hydraulic Control"),
  ("C","N20-50-R","C-5-6","Pressure Reducing 2-Way Valve with Hydraulic Control"),
  ("C","N20-54-K","C-7","Pressure Reducing 2-Way Valve N.C. with Hydraulic Relay"),
  ("C","N20-54-R","C-8","Pressure Reducing 2-Way Valve N.C. with Hydraulic Relay"),
  ("C","N20-55-K","C-9","Pressure Reducing 2-Way Valve with Solenoid Control"),
  ("C","N20-55-R","C-10-11","Pressure Reducing 2-Way Valve with Solenoid Control"),
  ("C","920-D2-R","C-12","Pressure Reducing 2-Way Valve — Automatic Metering Valve (AMV)"),
  ("C","N20-KXZ","C-13","Pressure Reducing 3-Way Valve"),
  ("C","N20-RXZ","C-14","Pressure Reducing 3-Way Valve"),
  ("C","N20-50-KXZ","C-15","Pressure Reducing 3-Way Valve with Hydraulic Control"),
  ("C","N20-50-RXZ","C-16","Pressure Reducing 3-Way Valve with Hydraulic Control"),
  ("C","N20-54-KX","C-17","Pressure Reducing 3-Way Valve N.C. with Hydraulic Relay"),
  ("C","N20-54-RXZ","C-18","Pressure Reducing 3-Way Valve N.C. with Hydraulic Relay"),
  ("C","N20-55-KX","C-19","Pressure Reducing 3-Way Valve with Solenoid Control (982/985 Only)"),
  ("C","N20-55-KX","C-20","Pressure Reducing 3-Way Valve with Solenoid Control"),
  ("C","N20-55-RX","C-21","Pressure Reducing 3-Way Valve with Solenoid Control (982/985 Only)"),
  ("C","N20-55-RX","C-22-23","Pressure Reducing 3-Way Valve with Solenoid Control"),
  ("C","920-D0-KX","C-24","Pressure Reducing 3-Way Valve — Automatic Metering Valve (AMV)"),
  ("C","920-D2-RX","C-25","Pressure Reducing 3-Way Valve — Automatic Metering Valve (AMV)"),
  ("C","N20-bKZ","C-26","Pressure Reducing 2/3-Way (Servo) Valve"),
  ("C","N20-50-bKZ","C-27","Pressure Reducing 2/3-Way (Servo) Valve with Hydraulic Control"),
  ("C","N20-54-bK","C-28","Pressure Reducing 2/3-Way (Servo) Valve N.C. with Hydraulic Control"),
  ("C","N20-55-bK","C-29","Pressure Reducing 2/3-Way (Servo) Valve with Solenoid Control (982/985 Only)"),
  ("C","N20-55-bK","C-30","Pressure Reducing 2/3-Way (Servo) Valve with Solenoid Control"),
  # D - PR & Sustaining
  ("D","N23-K","D-1","Pressure Reducing & Sustaining 2-Way Valve"),
  ("D","N23-R","D-2-3","Pressure Reducing & Sustaining 2-Way Valve"),
  ("D","N23-50-K","D-4","Pressure Reducing & Sustaining 2-Way Valve with Hydraulic Control"),
  ("D","N23-50-R","D-5-6","Pressure Reducing & Sustaining 2-Way Valve with Hydraulic Control"),
  ("D","N23-55-K","D-7","Pressure Reducing & Sustaining 2-Way Valve with Solenoid Control"),
  ("D","N23-55-R","D-8-9","Pressure Reducing & Sustaining 2-Way Valve with Solenoid Control"),
  ("D","N23-KXZ","D-10-11","Pressure Reducing & Sustaining 3-Way Valve"),
  ("D","N23-RXZ","D-12","Pressure Reducing & Sustaining 3-Way Valve"),
  ("D","N23-50-KXZ","D-13","Pressure Reducing & Sustaining with Hydraulic Control"),
  ("D","N23-50-RXZ","D-14","Pressure Reducing & Sustaining 3-Way Valve with Hydraulic Control"),
  ("D","N23-54-KX","D-15","Pressure Reducing & Sustaining 3-Way Valve N.C. with Hydraulic Relay"),
  ("D","N23-55-KX","D-16","Pressure Reducing & Sustaining 3-Way Valve with Solenoid Control (982/5 Only)"),
  ("D","N23-55-RXZ","D-17-18","Pressure Reducing & Sustaining 3-Way Valve with Solenoid Control"),
  # E - Pressure Sustaining & Relief
  ("E","N30-K","E-1","Pressure Sustaining 2-Way Valve"),
  ("E","N30-R","E-2-3","Pressure Sustaining 2-Way Valve"),
  ("E","N30-50-K","E-4","Pressure Sustaining 2-Way Valve with Hydraulic Control"),
  ("E","N30-50-R","E-5","Pressure Sustaining 2-Way Valve with Hydraulic Control"),
  ("E","N30-55-K","E-6","Pressure Sustaining 2-Way Valve with Solenoid Control"),
  ("E","N30-55-R","E-7-8","Pressure Sustaining 2-Way Valve with Solenoid Control"),
  ("E","N30-KXZ","E-9","Pressure Sustaining 3-Way Valve"),
  ("E","N30-RXZ","E-10-11","Pressure Sustaining 3-Way Valve"),
  ("E","N30-50-KXZ","E-12","Pressure Sustaining 3-Way Valve with Hydraulic Control"),
  ("E","N30-50-RXZ","E-13","Pressure Sustaining 3-Way Valve with Hydraulic Control"),
  ("E","N30-54-KX","E-14","Pressure Sustaining 3-Way Valve N.C. with Hydraulic Relay"),
  ("E","N30-55-KX","E-15","Pressure Sustaining 3-Way Valve with Solenoid Control (982/985 Only)"),
  ("E","N30-55-KX","E-16","Pressure Sustaining 3-Way Valve with Solenoid Control"),
  ("E","N30-55-RX","E-17","Pressure Sustaining 3-Way Valve with Solenoid Control (982/985 Only)"),
  ("E","N30-55-RX","E-18","Pressure Sustaining 3-Way Valve with Solenoid Control"),
  ("E","930-D0-KX","E-19","Pressure Sustaining 3-Way Valve — Automatic Metering Valve (AMV)"),
  ("E","N3Q-K","E-20","Pressure Relief Valve (Quick Type)"),
  ("E","N3Q-R","E-21","Pressure Relief Valve (Quick Type)"),
  # F - Level Control
  ("F","N50-60-R","F-1","Level Control Valve with Modulating Horizontal Float"),
  ("F","N50-N3-60-K","F-2","Level Control Valve with Modulating Horizontal Float"),
  ("F","450-66-Z","F-3-4","Level Control Valve with Bi-Level Vertical Float"),
  ("F","750-66-B","F-5","Level Control Valve with Bi-Level Vertical Float"),
  ("F","N50-80-XZ","F-6-7","Level Control Valve with Altitude Pilot"),
  ("F","N53-66","F-8","Level Control & Pressure Sustaining Valve with Bi-Level Vertical Float"),
  ("F","N57-66-U","F-9","Level & Flow Control Valve with Bi-Level Vertical Float"),
  # G - Flow Control
  ("G","170-bDZ","G-1","Flow Control Valve (Differential Pressure Duct)"),
  ("G","N70-bKUZ","G-2","Flow Control Valve (Orifice Assembly)"),
  ("G","N70-bRUZ","G-3","Flow Control Valve (Orifice Assembly)"),
  ("G","970-KVZ","G-4","Flow Control Valve (Paddle Pilot)"),
  ("G","970-RVZ","G-5","Flow Control Valve (Paddle Pilot)"),
  ("G","170-50-bDZ","G-6","Flow Control Valve with Hydraulic Control (Differential Pressure Duct)"),
  ("G","N70-50-bKUZ","G-7","Flow Control Valve with Hydraulic Control (Orifice Assembly)"),
  ("G","N70-50-bRUZ","G-8","Flow Control Valve with Hydraulic Control (Orifice Assembly)"),
  ("G","970-50-KVZ","G-9","Flow Control Valve with Hydraulic Control (Paddle Pilot)"),
  ("G","970-50-RVZ","G-10","Flow Control Valve with Hydraulic Control (Paddle Pilot)"),
  ("G","170-55-bD","G-11","Flow Control Valve with Solenoid Control (Diff. Pressure Duct) — 982/985 Only"),
  ("G","170-55-bD","G-12","Flow Control Valve with Solenoid Control (Differential Pressure Duct)"),
  ("G","N70-55-bKU","G-13","Flow Control Valve with Solenoid Control (Orifice Assembly) — 982/985 Only"),
  ("G","N70-55-bKU","G-14","Flow Control Valve with Solenoid Control (Orifice Assembly)"),
  ("G","N70-55-bRU","G-15","Flow Control Valve with Solenoid Control (Orifice Assembly)"),
  ("G","970-55-KV","G-16","Flow Control Valve with Solenoid Control (Paddle Pilot) — 982/985 Only"),
  ("G","970-55-KV","G-17","Flow Control Valve with Solenoid Control (Paddle Pilot)"),
  # H - Flow Control & PR
  ("H","172-bDZ","H-1","Flow Control & Pressure Reducing Valve (Differential Pressure Duct)"),
  ("H","N72-bKUZ","H-2","Flow Control & Pressure Reducing Valve (Orifice Assembly)"),
  ("H","N72-bRU","H-3","Flow Control & Pressure Reducing Valve (Orifice Assembly)"),
  ("H","972-KVZ","H-4","Flow Control & Pressure Reducing Valve (Paddle Pilot)"),
  ("H","972-RV","H-5","Flow Control & Pressure Reducing Valve (Paddle Pilot)"),
  ("H","172-50-bDZ","H-6","Flow Control & Pressure Reducing with Hydraulic Control (Diff. Pressure Duct)"),
  ("H","172-55-bD","H-7","Flow Control & Pressure Reducing with Solenoid Control (Diff. Pressure Duct)"),
  ("H","N72-50-bKUZ","H-8","Flow Control & Pressure Reducing with Hydraulic Control (Orifice Assembly)"),
  ("H","N72-50-bRU","H-9","Flow Control & Pressure Reducing with Hydraulic Control (Orifice Assembly)"),
  ("H","N72-55-bKU","H-10","Flow Control & Pressure Reducing with Solenoid Control (Orifice Assembly)"),
  ("H","N72-55-bKU","H-11","Flow Control & Pressure Reducing with Solenoid Control (Orifice Assembly)"),
  ("H","N72-55-bRU","H-12","Flow Control & Pressure Reducing with Solenoid Control (Orifice Assembly)"),
  ("H","972-50-KV","H-13","Flow Control & Pressure Reducing with Hydraulic Control (Paddle Pilot)"),
  ("H","972-50-RV","H-14","Flow Control & Pressure Reducing with Hydraulic Control (Paddle Pilot)"),
  ("H","972-MO-55-bKV","H-15-16","Flow Control & Pressure Reducing with Hydraulic Control (Paddle Pilot)"),
  ("H","972-MO-55-RV","H-17","Flow Control & Pressure Reducing with Hydraulic Control (Paddle Pilot)"),
]

# Calcular número de páginas PDF de cada entrada
def label_pages(label):
    parts = label.split('-')
    nums = [p for p in parts if p.isdigit()]
    if len(nums) >= 2:
        return int(nums[-1]) - int(nums[-2]) + 1
    return 1

INDEX = []
current_pdf_page = 14  # A-1 está na página 14
for cat, model, label, desc in RAW:
    npages = label_pages(label)
    INDEX.append({"cat":cat,"model":model,"label":label,"desc":desc,"pdfPage":current_pdf_page,"pages":npages})
    current_pdf_page += npages

print(f"Entradas: {len(INDEX)}, última página PDF: {current_pdf_page-1} (total PDF: 170)")

# ── Categorias ────────────────────────────────────────────────────────────────
CATS = {
    "A":{"icon":"&#9881;","label":"Accessories","bg":"#fff3e0","color":"#e65100","border":"#ffcc02"},
    "B":{"icon":"&#9724;","label":"On/Off Control","bg":"#e3f2fd","color":"#0d47a1","border":"#90caf9"},
    "C":{"icon":"&#11015;","label":"Pressure Reducing","bg":"#e8f5e9","color":"#1b5e20","border":"#a5d6a7"},
    "D":{"icon":"&#8597;","label":"PR & Sustaining","bg":"#e0f7fa","color":"#006064","border":"#80deea"},
    "E":{"icon":"&#11014;","label":"Pressure Sustaining & Relief","bg":"#f3e5f5","color":"#4a148c","border":"#ce93d8"},
    "F":{"icon":"&#127786;","label":"Level Control","bg":"#e1f5fe","color":"#01579b","border":"#81d4fa"},
    "G":{"icon":"&#8651;","label":"Flow Control","bg":"#fff8e1","color":"#f57f17","border":"#ffe082"},
    "H":{"icon":"&#8646;","label":"Flow Control & PR","bg":"#fce4ec","color":"#880e4f","border":"#f48fb1"},
}

JS_INDEX = json.dumps(INDEX, ensure_ascii=False)
JS_CATS  = json.dumps(CATS,  ensure_ascii=False)

# ── HTML ───────────────────────────────────────────────────────────────────────
HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>BERMAD Diagrams — Bolsa Irriga</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Segoe UI',system-ui,sans-serif;background:#f0f4f8;color:#1a2535;height:100vh;display:flex;flex-direction:column;overflow:hidden}}
/* header */
.hdr{{background:linear-gradient(135deg,#1a3a5c 0%,#2c5f8a 60%,#3d7eb5 100%);color:#fff;padding:.65rem 1rem;display:flex;align-items:center;gap:.8rem;flex-shrink:0;flex-wrap:wrap}}
.hdr-logo{{display:flex;align-items:center;gap:.6rem}}
.hdr-logo img{{height:40px;width:40px;object-fit:contain;background:#fff;border-radius:8px;padding:4px}}
.hdr-brand h1{{font-size:1rem;font-weight:800;line-height:1.2}}
.hdr-brand p{{font-size:.68rem;opacity:.8;margin-top:.05rem}}
.search-wrap{{flex:1;min-width:160px;max-width:320px}}
.search-wrap input{{width:100%;padding:.38rem .75rem;border-radius:8px;border:none;font-size:.85rem;background:rgba(255,255,255,.18);color:#fff;outline:none;transition:background .15s}}
.search-wrap input::placeholder{{color:rgba(255,255,255,.6)}}
.search-wrap input:focus{{background:rgba(255,255,255,.28)}}
.nav-btns{{display:flex;align-items:center;gap:.4rem;margin-left:auto}}
.nav-btns button{{background:rgba(255,255,255,.18);color:#fff;border:none;border-radius:6px;padding:.35rem .7rem;font-size:.82rem;font-weight:700;cursor:pointer;transition:background .15s}}
.nav-btns button:hover{{background:rgba(255,255,255,.32)}}
#pg-info{{font-size:.75rem;opacity:.85;white-space:nowrap}}
/* filtros categoria */
.filters{{background:#fff;border-bottom:1px solid #d0e4f0;padding:.45rem .8rem;display:flex;gap:.35rem;flex-wrap:wrap;flex-shrink:0;overflow-x:auto}}
.fbtn{{padding:.25rem .65rem;border-radius:16px;font-size:.72rem;font-weight:700;cursor:pointer;border:1.5px solid transparent;transition:all .15s;white-space:nowrap}}
.fbtn.all{{background:#e3f2fd;color:#0077b6;border-color:#90caf9}}
.fbtn.all.active,.fbtn.all:hover{{background:#0077b6;color:#fff}}
/* layout */
.body{{flex:1;display:flex;overflow:hidden}}
/* sidebar */
.sidebar{{width:300px;min-width:220px;background:#fff;border-right:1px solid #d0e4f0;display:flex;flex-direction:column;overflow:hidden;flex-shrink:0}}
.sidebar-scroll{{overflow-y:auto;flex:1}}
.cat-header{{padding:.4rem .8rem .2rem;font-size:.65rem;font-weight:900;text-transform:uppercase;letter-spacing:.08em;display:flex;align-items:center;gap:.4rem;position:sticky;top:0;z-index:1}}
.item{{padding:.45rem .8rem;cursor:pointer;border-left:3px solid transparent;transition:background .1s,border-color .1s;display:flex;flex-direction:column;gap:.1rem}}
.item:hover{{background:#f0f7ff}}
.item.active{{background:#e3f2fd;border-left-color:#0077b6}}
.item-model{{font-size:.8rem;font-weight:800;color:#003d5c}}
.item-label{{font-size:.65rem;font-weight:700;border-radius:8px;padding:.05rem .4rem;display:inline-block;margin-bottom:.05rem}}
.item-desc{{font-size:.7rem;color:#607080;line-height:1.3}}
.no-results{{padding:1.5rem;text-align:center;color:#607080;font-size:.82rem}}
/* main */
.main{{flex:1;display:flex;flex-direction:column;overflow:hidden;background:#e8edf2}}
.main-title{{background:#fff;border-bottom:1px solid #d0e4f0;padding:.5rem 1rem;font-size:.82rem;font-weight:700;color:#003d5c;flex-shrink:0;min-height:2.1rem;display:flex;align-items:center;gap:.6rem}}
.main-title .lbl{{font-size:.68rem;padding:.12rem .5rem;border-radius:10px;font-weight:800}}
iframe{{flex:1;width:100%;border:none}}
.placeholder{{flex:1;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:.8rem;color:#607080}}
.placeholder p{{font-size:.88rem}}
/* mobile */
@media(max-width:700px){{
  .body{{flex-direction:column}}
  .sidebar{{width:100%;max-height:45vh;border-right:none;border-bottom:1px solid #d0e4f0}}
  .main iframe{{display:none}}
  .main-title{{font-size:.75rem}}
  .item.active .item-model::after{{content:' — toque para abrir PDF';font-size:.65rem;color:#0077b6;font-weight:400}}
}}
</style>
</head>
<body>

<div class="hdr">
  <div class="hdr-logo">
    <img src="logo perfil branca.png" alt="Bolsa Irriga" onerror="this.style.display='none'">
    <div class="hdr-brand">
      <h1>BERMAD Diagrams</h1>
      <p>Irrigation Control Circuits &amp; Accessories &mdash; Pocket Guide</p>
    </div>
  </div>
  <div class="search-wrap">
    <input type="text" id="search" placeholder="&#128269; Search model, description..." oninput="filter()">
  </div>
  <div class="nav-btns">
    <button onclick="navStep(-1)">&#8592; Prev</button>
    <span id="pg-info"></span>
    <button onclick="navStep(1)">Next &#8594;</button>
    <button onclick="openInTab()" title="Open in new tab">&#10697;</button>
  </div>
</div>

<div class="filters" id="filters"></div>

<div class="body">
  <div class="sidebar">
    <div class="sidebar-scroll" id="listWrap"></div>
  </div>
  <div class="main" id="main">
    <div class="main-title" id="mainTitle">
      <span>Select a diagram from the list</span>
    </div>
    <div class="placeholder" id="placeholder">
      <span style="font-size:2.5rem">&#128209;</span>
      <p>BERMAD Irrigation Control Circuits &amp; Accessories</p>
      <p style="font-size:.75rem;color:#90a4b4">{len(INDEX)} diagrams in 8 categories (A&ndash;H)</p>
    </div>
    <iframe id="pdfFrame" class="hidden" src="" allow="fullscreen"></iframe>
  </div>
</div>

<script>
const INDEX = {JS_INDEX};
const CATS  = {JS_CATS};
const PDF   = 'BERMAD-Pocket-Guide-English.pdf';

let currentIdx = -1;
let activeCat  = 'all';
let filtered   = INDEX.slice();

function buildFilters(){{
  const wrap = document.getElementById('filters');
  let html = `<button class="fbtn all active" onclick="setCat('all')">All ({len(INDEX)})</button>`;
  Object.entries(CATS).forEach(([k,c])=>{{
    const n = INDEX.filter(e=>e.cat===k).length;
    html += `<button class="fbtn" id="fcat-${{k}}" onclick="setCat('${{k}}')"
      style="background:${{c.bg}};color:${{c.color}};border-color:${{c.border}}">
      ${{c.icon}} ${{k}} — ${{c.label}} (${{n}})</button>`;
  }});
  wrap.innerHTML = html;
}}

function setCat(cat){{
  activeCat = cat;
  document.querySelectorAll('.fbtn').forEach(b=>b.classList.remove('active'));
  const id = cat==='all'?'filters .all':'fcat-'+cat;
  const btn = cat==='all'
    ? document.querySelector('.fbtn.all')
    : document.getElementById('fcat-'+cat);
  if(btn) btn.classList.add('active');
  filter();
}}

function filter(){{
  const q = document.getElementById('search').value.trim().toLowerCase();
  filtered = INDEX.filter(e=>{{
    const catOk = activeCat==='all'||e.cat===activeCat;
    const txtOk = !q||(e.model+' '+e.desc+' '+e.label).toLowerCase().includes(q);
    return catOk&&txtOk;
  }});
  buildList();
}}

function buildList(){{
  const wrap = document.getElementById('listWrap');
  if(!filtered.length){{
    wrap.innerHTML='<div class="no-results">No diagrams found</div>'; return;
  }}
  let lastCat='', html='';
  filtered.forEach((e,i)=>{{
    if(e.cat!==lastCat){{
      lastCat=e.cat;
      const c=CATS[e.cat];
      html+=`<div class="cat-header" style="background:${{c.bg}};color:${{c.color}}">${{c.icon}} ${{e.cat}} — ${{c.label}}</div>`;
    }}
    const realIdx=INDEX.indexOf(e);
    html+=`<div class="item${{realIdx===currentIdx?' active':''}}" onclick="goItem(${{realIdx}})">
      <span class="item-label" style="background:${{CATS[e.cat].bg}};color:${{CATS[e.cat].color}}">${{e.label}}</span>
      <span class="item-model">${{e.model}}</span>
      <span class="item-desc">${{e.desc}}</span>
    </div>`;
  }});
  wrap.innerHTML=html;
}}

function goItem(idx){{
  if(idx<0||idx>=INDEX.length) return;
  currentIdx=idx;
  const e=INDEX[idx];
  const isMobile=window.innerWidth<=700;

  // sidebar highlight
  buildList();
  const items=document.querySelectorAll('.item');
  let fi=filtered.indexOf(e);
  if(fi>=0){{
    // find DOM item by position
    const domItem=document.querySelectorAll('.item')[fi];
    if(domItem) domItem.scrollIntoView({{block:'nearest',behavior:'smooth'}});
  }}

  // title
  const c=CATS[e.cat];
  document.getElementById('mainTitle').innerHTML=
    `<span class="lbl" style="background:${{c.bg}};color:${{c.color}}">${{e.label}}</span>`+
    `<strong>${{e.model}}</strong> — ${{e.desc}}`;
  document.getElementById('pg-info').textContent=`PDF p. ${{e.pdfPage}}`;

  if(isMobile){{
    window.open(`${{PDF}}#page=${{e.pdfPage}}`,'_blank'); return;
  }}
  const frame=document.getElementById('pdfFrame');
  frame.src=`${{PDF}}#page=${{e.pdfPage}}`;
  frame.className='';
  document.getElementById('placeholder').className='placeholder hidden';
}}

function navStep(d){{
  const nextIdx=currentIdx+d;
  if(nextIdx>=0&&nextIdx<INDEX.length) goItem(nextIdx);
}}

function openInTab(){{
  if(currentIdx<0) return;
  window.open(`${{PDF}}#page=${{INDEX[currentIdx].pdfPage}}`,'_blank');
}}

buildFilters();
filter();
</script>
</body>
</html>"""

# Copiar PDF com nome limpo
src = 'BERMAD-Pocket-Guide-English.pdf'
dst = 'bermad.pdf'
if os.path.exists(src) and not os.path.exists(dst):
    shutil.copy2(src, dst)
    print(f"PDF copiado: {dst}")
elif os.path.exists(dst):
    print(f"PDF ja existe: {dst}")

with open('bermad.html','w',encoding='utf-8') as f:
    f.write(HTML)
print(f"OK - {len(HTML):,} bytes - bermad.html ({len(INDEX)} entradas)")
