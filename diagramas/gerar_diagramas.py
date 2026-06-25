import base64, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('logo perfil branca.png','rb') as f:
    LOGO = base64.b64encode(f.read()).decode()

# Índice completo — (modelo, página PDF, categoria, descrição, piloto)
INDEX = [
  # ── INTRODUÇÃO ────────────────────────────────────────────────
  ('',    1, 'intro',  'Capa — Connection Diagrams (Dorot Control Valves)', ''),
  ('',    2, 'intro',  'Índice — Página 1 (P1–P11)', ''),
  ('',    3, 'intro',  'Índice — Página 2 (PR1–PR13)', ''),
  ('',    4, 'intro',  'Índice — Página 3 (PS1–PS6, QR1, FR1–FR5)', ''),
  ('',    5, 'intro',  'Índice — Página 4 (AL1–AL5, CO1–CO5)', ''),
  ('',    6, 'intro',  'Índice — Página 5 (MS1–MS13)', ''),
  # ── ACESSÓRIOS DE CONTROLE ───────────────────────────────────
  ('',    7, 'acess',  'Acessórios de Controle — Geral (Pilotos 3 vias, 2 vias, Seletor Manual)', ''),
  ('',    8, 'acess',  'Acessórios de Controle — Geral (continuação — Válvula Agulha, Filtro)', ''),
  ('',    9, 'acess',  'Relés Elétricos (Solenóides) — 3 vias (N.O. e N.C.)', ''),
  ('',   10, 'acess',  'Relés Hidráulicos — 28-200 2 vias / 25-300 3 vias / Galit 3 vias', ''),
  ('',   11, 'acess',  'Relés Hidráulicos (continuação)', ''),
  # ── PILOTOS P1–P11 ────────────────────────────────────────────
  ('P1',  12, 'pilot', '3 vias — Redução e Sustentação de Pressão', '31-310 / 29-200'),
  ('P2',  13, 'pilot', '3 vias — Redução de Pressão', '29-100'),
  ('P3',  14, 'pilot', '3 vias — Pressão Diferencial e Controle de Vazão', '76-200 / 29-300'),
  ('P4',  15, 'pilot', '3 vias — Sustentação de Pressão com Relé 3 vias', '66-310 / 68-710'),
  ('P5',  16, 'pilot', '3 vias — Redução de Pressão / Controle de Vazão', '31-100 / 31-10D'),
  ('P6',  17, 'pilot', '2 vias — Redução de Pressão', '68-410'),
  ('P7',  18, 'pilot', '2 vias — Sustentação de Pressão', '68-500'),
  ('P8',  19, 'pilot', '2 vias — Alívio Rápido', '68-220'),
  ('P9',  20, 'pilot', '2 vias — Redução de Pressão', 'CXPR'),
  ('P10', 21, 'pilot', '2 vias — Sustentação de Pressão', 'CXPS / CXSD'),
  ('P11', 22, 'pilot', '2 vias — Controle de Vazão', 'CXRS'),
  # ── REDUÇÃO DE PRESSÃO — PR ───────────────────────────────────
  ('PR1',  23, 'pr', 'Válvula Redutora de Pressão (PR)', '29-100 Mini Pilot (Black)'),
  ('PR2',  24, 'pr', 'Válvula Redutora Elétrica (PR/EL)', '29-100 Mini Pilot (Black)'),
  ('PR3',  25, 'pr', 'Válvula Redutora de Pressão (PR)', '29-200 Mini Pilot (Blue)'),
  ('PR4',  26, 'pr', 'Válvula Redutora Elétrica (PR/EL)', '29-200 Mini Pilot (Blue)'),
  ('PR5',  27, 'pr', 'Válvula Redutora de Pressão (PR)', '31-100 Mini Pilot (3w-brass)'),
  ('PR6',  28, 'pr', 'Válvula Redutora de Pressão (PR)', '31-310 Pilot (Brass)'),
  ('PR7',  29, 'pr', 'Válvula Redutora Elétrica (PR/EL)', '31-310 Pilot (Brass)'),
  ('PR8',  30, 'pr', 'Redutora / Controle Remoto (PR/RC)', '29-100 Mini Pilot (Black) + Galit'),
  ('PR9',  31, 'pr', 'Redutora / Controle Remoto (PR/RC)', '31-310 Pilot (Brass) + Galit'),
  ('PR10', 32, 'pr', 'Válvula Redutora de Pressão (PR)', '68-410 Pilot (2w-brass)'),
  ('PR11', 33, 'pr', 'Válvula Redutora Elétrica (PR/EL)', '68-410 Pilot (2w-brass)'),
  ('PR12', 34, 'pr', 'Válvula Redutora de Pressão (PR)', 'CXPR Pilot (2w-brass)'),
  ('PR13', 35, 'pr', 'Válvula Redutora de Pressão Proporcional (PRD)', ''),
  # ── SUSTENTAÇÃO DE PRESSÃO — PS ──────────────────────────────
  ('PS1', 36, 'ps', 'Válvula Sustentadora de Pressão (PS)', '29-200 Mini Pilot (Blue)'),
  ('PS2', 37, 'ps', 'Sustentadora Elétrica (PS/EL)', '29-200 Mini Pilot (Blue)'),
  ('PS3', 38, 'ps', 'Válvula Sustentadora de Pressão (PS)', '31-310 Pilot'),
  ('PS4', 39, 'ps', 'Sustentadora Elétrica (PS/EL)', '31-310 Pilot'),
  ('PS5', 40, 'ps', 'Válvula Sustentadora de Pressão (PS)', '68-500 Pilot (2-way)'),
  ('PS6', 41, 'ps', 'Válvula Sustentadora de Pressão (PS)', 'CXPS Pilot (2-way)'),
  # ── ALÍVIO RÁPIDO — QR ───────────────────────────────────────
  ('QR1', 42, 'qr', 'Válvula de Alívio Rápido (QR)', '68-220 Pilot (2-way)'),
  # ── CONTROLE DE VAZÃO — FR ───────────────────────────────────
  ('FR1', 43, 'fr', 'Válvula de Controle de Vazão (FR)', '31-10D Mini Pilot (3w-brass)'),
  ('FR2', 44, 'fr', 'Válvula de Controle de Vazão (FR)', '76-200 Differential Pilot'),
  ('FR3', 45, 'fr', 'Válvula de Controle de Vazão (FR)', '29-300 Differential Pilot'),
  ('FR4', 46, 'fr', 'Válvula de Bloqueio por Excesso de Vazão (FE)', '76-200 Differential Pilot'),
  ('FR5', 47, 'fr', 'Válvula de Controle de Vazão (FR)', 'CXRS Differential Pilot'),
  # ── CONTROLE DE NÍVEL — AL ───────────────────────────────────
  ('AL1', 48, 'al', 'Válvula de Controle de Nível Alto (AL)', '70-110 Pilot'),
  ('AL2', 49, 'al', 'Controle de Nível FLDI — Válvulas Grandes', '70-550 Diff. Float Pilot + 28-300 Relays'),
  ('AL3', 50, 'al', 'Válvula de Controle de Nível (FLDI)', '70-550 Differential Float Pilot'),
  ('AL4', 51, 'al', 'Válvula de Controle de Nível (FLDI)', '70-610 Differential Float Pilot'),
  ('AL5', 52, 'al', 'Válvula de Controle de Nível (FL)', '70-400 Float Pilot'),
  # ── APLICAÇÕES COMBINADAS — CO ────────────────────────────────
  ('CO1', 53, 'co', 'Redutora + Válvula de Retenção (PR/CV)', '68-410 Pilot (2-way)'),
  ('CO2', 54, 'co', 'Redutora + Sustentadora (PR/PS)', 'Dois 29-200 Mini Pilots (Blue)'),
  ('CO3', 55, 'co', 'Redutora + Sustentadora (PR/PS)', '29-100 (Black) + 29-200 (Blue)'),
  ('CO4', 56, 'co', 'Redutora + Sustentadora (PR/PS)', 'Dois 31-310 Pilots'),
  ('CO5', 57, 'co', 'Redutora + Sustentadora (PR/PS)', 'CXPS + CXPR Pilots'),
  # ── APLICAÇÕES DIVERSAS — MS ──────────────────────────────────
  ('MS1',  58, 'ms', 'Válvula Elétrica N.A. (EL)', ''),
  ('MS2',  59, 'ms', 'Válvula Elétrica N.F. (EL)', ''),
  ('MS3',  60, 'ms', 'Controle Remoto com Compensação Topográfica (RC)', '25-100 Mini Pilot (Blue)'),
  ('MS4',  61, 'ms', 'Abertura em Dois Estágios (TO)', '29-200 Mini Pilot (Blue)'),
  ('MS5',  62, 'ms', 'Abertura em Dois Estágios (TO)', '31-310 Pilot (Brass)'),
  ('MS6',  63, 'ms', 'Válvula Elétrica N.F. com Acelerador (EL)', '66-210 Accelerator Relay'),
  ('MS7',  64, 'ms', 'Controle Remoto (RC)', 'Galit'),
  ('MS8',  65, 'ms', 'Válvula de Controle de Bomba (BC)', 'S-100'),
  ('MS9',  66, 'ms', 'Válvula de Controle de Bomba (BC)', 'S-300'),
  ('MS10', 67, 'ms', 'Válvula de Pressão Diferencial (DI)', '76-200 Differential Pilot'),
  ('MS11', 68, 'ms', 'Válvula de Controle Remoto (RC)', 'Tubo de Comando'),
  ('MS12', 69, 'ms', 'Válvula de Pressão Diferencial (DI)', 'CXSD Differential Pilot'),
  ('MS13', 70, 'ms', 'Válvula Sustentadora de Pressão Diferencial (DI)', '76-200 Differential Pilot'),
  # ── CONTRACAPA ────────────────────────────────────────────────
  ('',    71, 'intro', 'Contracapa — Dorot Control Valves (www.dorot.com)', ''),
]

CATS = {
  'intro': ('📄', 'Introdução / Índice',      '#607080', '#f4f8fb', '#d0e4f0'),
  'acess': ('⚙️',  'Acessórios de Controle',   '#005f8e', '#e8f4fd', '#a8d4f0'),
  'pilot': ('🔵', 'Pilotos P1–P11',            '#1565c0', '#e3f2fd', '#90caf9'),
  'pr':    ('🔴', 'Redução de Pressão (PR)',   '#b71c1c', '#ffebee', '#ef9a9a'),
  'ps':    ('🟠', 'Sustentação de Pressão (PS)','#e65100','#fff3e0', '#ffcc80'),
  'qr':    ('⚡', 'Alívio Rápido (QR)',        '#f9a825', '#fffde7', '#fff176'),
  'fr':    ('💧', 'Controle de Vazão (FR)',    '#00695c', '#e0f2f1', '#80cbc4'),
  'al':    ('🌊', 'Controle de Nível (AL)',    '#0277bd', '#e1f5fe', '#81d4fa'),
  'co':    ('🔗', 'Aplicações Combinadas (CO)','#6a1b9a', '#f3e5f5', '#ce93d8'),
  'ms':    ('🔧', 'Diversas (MS)',             '#2e7d32', '#e8f5e9', '#a5d6a7'),
}

HTML = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Diagramas de Ligações de Válvulas — Dorot — Bolsa Irriga</title>
<style>
:root{{
  --bl:#005f8e;--bl2:#0077b6;--tx:#1a2535;--mu:#607080;--bg:#f4f7fb;--bdr:#d0e4f0;
  --sh:0 2px 12px rgba(0,80,160,.10);
}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--tx);font-size:14px;height:100vh;display:flex;flex-direction:column}}
header{{background:linear-gradient(135deg,#003d5c,#0077b6,#00b4d8);color:#fff;flex-shrink:0;box-shadow:0 3px 16px rgba(0,0,0,.2)}}
.hdr{{padding:.6rem 1rem;display:flex;justify-content:space-between;align-items:center;gap:.8rem;flex-wrap:wrap}}
.hdr-logo{{display:flex;align-items:center;gap:.7rem}}
.hdr-logo img{{height:52px;width:52px;object-fit:contain;background:#fff;border-radius:8px;padding:5px}}
.hdr-brand h1{{font-size:1.1rem;font-weight:800}}
.hdr-brand p{{font-size:.72rem;opacity:.85}}
.hdr-dev{{font-size:.68rem;line-height:1.6;opacity:.9;text-align:right}}
.hdr-dev b{{font-size:.78rem}}
/* layout */
.main{{display:flex;flex:1;overflow:hidden}}
/* sidebar */
.sidebar{{width:320px;flex-shrink:0;background:#fff;border-right:2px solid var(--bdr);display:flex;flex-direction:column;overflow:hidden}}
.sb-top{{padding:.6rem .8rem;border-bottom:1px solid var(--bdr);flex-shrink:0}}
.sb-top h2{{font-size:.78rem;font-weight:800;color:var(--bl2);text-transform:uppercase;letter-spacing:.06em;margin-bottom:.45rem}}
.search-wrap{{position:relative}}
.search-wrap input{{width:100%;padding:.4rem .8rem .4rem 2rem;border:1.5px solid var(--bdr);border-radius:8px;font-size:.85rem;outline:none}}
.search-wrap input:focus{{border-color:#0077b6;box-shadow:0 0 0 2px rgba(0,119,182,.12)}}
.search-wrap::before{{content:'🔍';position:absolute;left:.5rem;top:50%;transform:translateY(-50%);font-size:.8rem;pointer-events:none}}
.cat-filters{{display:flex;flex-wrap:wrap;gap:.3rem;margin-top:.45rem}}
.cat-btn{{padding:.2rem .55rem;border-radius:10px;border:1.5px solid;font-size:.68rem;font-weight:700;cursor:pointer;transition:all .15s;background:#fff}}
.cat-btn.active{{color:#fff!important;border-color:transparent!important}}
.sb-list{{flex:1;overflow-y:auto;padding:.4rem 0}}
.cat-header{{padding:.35rem .8rem .2rem;font-size:.67rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;position:sticky;top:0;z-index:1;display:flex;align-items:center;gap:.3rem}}
.item{{display:flex;align-items:center;gap:.5rem;padding:.38rem .8rem;cursor:pointer;border-left:3px solid transparent;transition:all .12s;text-decoration:none}}
.item:hover{{background:var(--bg)}}
.item.active{{font-weight:700;border-left-width:3px}}
.item .model{{font-size:.78rem;font-weight:800;min-width:40px;flex-shrink:0}}
.item .desc{{font-size:.78rem;line-height:1.25;color:var(--tx)}}
.item .pilot{{font-size:.67rem;color:var(--mu);margin-top:.05rem}}
.item .pg{{font-size:.67rem;font-weight:700;color:var(--mu);margin-left:auto;flex-shrink:0;padding-left:.4rem}}
/* viewer */
.viewer{{flex:1;display:flex;flex-direction:column;overflow:hidden}}
.viewer-bar{{background:#fff;border-bottom:1px solid var(--bdr);padding:.4rem .8rem;display:flex;align-items:center;gap:.6rem;flex-shrink:0;flex-wrap:wrap}}
.viewer-bar .pg-info{{font-size:.82rem;color:var(--mu);font-weight:600}}
.viewer-bar .pg-input{{width:52px;padding:.25rem .4rem;border:1.5px solid var(--bdr);border-radius:6px;font-size:.85rem;text-align:center;outline:none}}
.viewer-bar .pg-input:focus{{border-color:#0077b6}}
.btn-nav{{background:#f4f7fb;border:1.5px solid var(--bdr);border-radius:6px;padding:.28rem .6rem;font-size:.82rem;cursor:pointer;font-weight:700;color:var(--bl2)}}
.btn-nav:hover{{background:#e0edf8}}
.btn-open{{background:var(--bl2);color:#fff;border:none;border-radius:6px;padding:.3rem .8rem;font-size:.8rem;font-weight:700;cursor:pointer;margin-left:auto}}
.btn-open:hover{{background:#004f75}}
.viewer-frame{{flex:1;position:relative}}
.viewer-frame iframe{{width:100%;height:100%;border:none;display:block}}
.mobile-msg{{display:none;padding:1.5rem;text-align:center;font-size:.9rem;color:var(--mu)}}
.mobile-msg a{{color:var(--bl2);font-weight:700}}
/* mobile */
@media(max-width:700px){{
  .main{{flex-direction:column}}
  .sidebar{{width:100%;max-height:45vh;border-right:none;border-bottom:2px solid var(--bdr)}}
  .viewer-frame iframe{{display:none}}
  .mobile-msg{{display:block}}
  .hdr-dev{{display:none}}
}}
</style>
</head>
<body>
<header>
  <div class="hdr">
    <div class="hdr-logo">
      <img src="data:image/png;base64,{LOGO}" alt="Bolsa Irriga">
      <div class="hdr-brand">
        <h1>Diagramas de Liga&#231;&#245;es de V&#225;lvulas</h1>
        <p>Dorot Control Valves &mdash; Miya Group &middot; 71 p&#225;ginas &middot; Referência técnica</p>
      </div>
    </div>
    <div class="hdr-dev">
      <b>Jo&#227;o Paulo de Oliveira</b><br>
      Engenheiro Agr&#244;nomo &middot; Especialista em Irriga&#231;&#227;o<br>
      bolsairriga.com.br &middot; (16) 3702-6571
    </div>
  </div>
</header>

<div class="main">
  <aside class="sidebar">
    <div class="sb-top">
      <h2>&#128269; Buscar Diagrama</h2>
      <div class="search-wrap">
        <input type="text" id="search" placeholder="Modelo, piloto ou descrição..." oninput="filter()">
      </div>
      <div class="cat-filters" id="cat-filters"></div>
    </div>
    <div class="sb-list" id="sb-list"></div>
  </aside>

  <div class="viewer">
    <div class="viewer-bar">
      <button class="btn-nav" onclick="navPage(-1)">&#9664;</button>
      <input class="pg-input" type="number" id="pg-input" min="1" max="71" value="1" onchange="goPage(this.value)">
      <span class="pg-info">/ 71</span>
      <button class="btn-nav" onclick="navPage(1)">&#9654;</button>
      <span class="pg-info" id="pg-title" style="flex:1;color:var(--tx);font-size:.8rem"></span>
      <button class="btn-open" onclick="openPDF()">&#128196; Abrir PDF completo</button>
    </div>
    <div class="viewer-frame">
      <iframe id="pdf-frame" src="diagramas-valvulas.pdf#page=1" title="Diagrama de Válvulas"></iframe>
      <div class="mobile-msg">
        <p>&#128241; No celular, clique no item do &#237;ndice para abrir o diagrama:</p>
        <p style="margin-top:.5rem"><a href="diagramas-valvulas.pdf" target="_blank">&#128196; Abrir PDF completo &#8594;</a></p>
      </div>
    </div>
  </div>
</div>

<script>
const CATS={{{','.join([f"'{k}':['{v[0]}','{v[1]}','{v[2]}','{v[3]}','{v[4]}']" for k,v in CATS.items()])}}}
const INDEX={repr([list(x) for x in INDEX])};
let currentPage=1, activeCat='all';

function buildFilters(){{
  const d=document.getElementById('cat-filters');
  const btn=(k,label,color,bg)=>{{
    const b=document.createElement('button');
    b.className='cat-btn'+(k==='all'?' active':'');
    b.textContent=label;b.dataset.cat=k;
    b.style.color=color;b.style.borderColor=color;b.style.background=bg;
    b.onclick=()=>{{activeCat=k;d.querySelectorAll('.cat-btn').forEach(x=>{{x.classList.remove('active');x.style.color=x.dataset.colOrig;x.style.background=x.dataset.bgOrig;}});b.classList.add('active');b.style.color='#fff';b.style.background=color;filter();}};
    b.dataset.colOrig=color;b.dataset.bgOrig=bg;
    d.appendChild(b);
  }};
  btn('all','Todos','#005f8e','#e8f4fd');
  Object.entries(CATS).forEach(([k,v])=>btn(k,v[0]+' '+v[1].split(' ')[0],v[2],v[3]));
}}

function buildList(items){{
  const d=document.getElementById('sb-list');
  d.innerHTML='';
  let lastCat='';
  items.forEach(item=>{{
    const [model,page,cat,desc,pilot]=item;
    const c=CATS[cat];
    if(cat!==lastCat){{
      lastCat=cat;
      const h=document.createElement('div');
      h.className='cat-header';
      h.style.background=c[3];h.style.color=c[2];h.style.borderBottom='1px solid '+c[4];
      h.innerHTML=`${{c[0]}} ${{c[1]}}`;
      d.appendChild(h);
    }}
    const a=document.createElement('a');
    a.className='item';a.href='#';
    a.style.borderLeftColor=c[2];
    const modelHtml=model?`<span class="model" style="color:${{c[2]}}">${{model}}</span>`:'<span class="model" style="color:#aaa">—</span>';
    a.innerHTML=`${{modelHtml}}<div><div class="desc">${{desc}}</div>${{pilot?`<div class="pilot">Piloto: ${{pilot}}</div>`:''}}</div><span class="pg">p.${{page}}</span>`;
    a.onclick=e=>{{e.preventDefault();goPage(page);}};
    a.dataset.page=page;
    d.appendChild(a);
  }});
  if(!items.length) d.innerHTML='<p style="padding:1rem;color:var(--mu);text-align:center;font-size:.83rem">Nenhum resultado encontrado.</p>';
}}

function filter(){{
  const q=document.getElementById('search').value.toLowerCase().trim();
  let items=INDEX;
  if(activeCat!=='all') items=items.filter(x=>x[2]===activeCat);
  if(q) items=items.filter(x=>x[0].toLowerCase().includes(q)||x[3].toLowerCase().includes(q)||x[4].toLowerCase().includes(q));
  buildList(items);
  // Sync active item
  document.querySelectorAll('.item').forEach(el=>{{
    el.classList.toggle('active',parseInt(el.dataset.page)===currentPage);
  }});
}}

function goPage(n){{
  n=Math.max(1,Math.min(71,parseInt(n)||1));
  currentPage=n;
  document.getElementById('pg-input').value=n;
  document.getElementById('pdf-frame').src='diagramas-valvulas.pdf#page='+n;
  // find title
  const item=INDEX.find(x=>x[1]===n);
  const title=item?(item[0]?item[0]+' — ':'')+item[3]:'';
  document.getElementById('pg-title').textContent=title;
  // highlight
  document.querySelectorAll('.item').forEach(el=>{{
    const active=parseInt(el.dataset.page)===n;
    el.classList.toggle('active',active);
    if(active) el.scrollIntoView({{block:'nearest',behavior:'smooth'}});
  }});
  // mobile: open PDF directly
  if(window.innerWidth<=700) window.open('diagramas-valvulas.pdf#page='+n,'_blank');
}}

function navPage(d){{goPage(currentPage+d);}}

function openPDF(){{window.open('diagramas-valvulas.pdf','_blank');}}

// init
buildFilters();
buildList(INDEX);
goPage(1);
</script>
</body>
</html>"""

with open('diagramas.html','w',encoding='utf-8') as f:
    f.write(HTML)
print(f'OK — {len(HTML):,} bytes ({len(INDEX)} entradas no índice)')
