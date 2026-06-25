import base64, sys, shutil, os
sys.stdout.reconfigure(encoding='utf-8')

with open('logo perfil branca.png','rb') as f:
    LOGO = base64.b64encode(f.read()).decode()

# ── Calcular página PDF de cada entrada ───────────────────────────────────────
def npages(label):
    parts = label.split('-')
    nums = [p for p in parts if p.isdigit()]
    if len(nums) >= 2:
        return int(nums[-1]) - int(nums[-2]) + 1
    return 1

RAW = [
  # (cat, model, label, desc, type_info)
  # A - Accessories
  ("A","PC-Sharp-X-P","A-1","Positioning 3-Way Sharp Mini-Pilot Valve, Plastic","Plastic"),
  ("A","PC-Sharp-X-M","A-2","Positioning 3-Way Sharp Mini-Pilot Valve, Metal","Metal"),
  ("A","PC-S-A-P","A-3","Pressure Reducing Servo 2/3-Way Mini-Pilot Valve","Plastic"),
  ("A","PC-S-A-M","A-4","Pressure Reducing Servo 2/3-Way Mini-Pilot Valve","Metal"),
  ("A","PC-20-A-P","A-5","Pressure Reducing 2-Way Mini-Pilot Valve","Plastic"),
  ("A","PC-20-A-M","A-6","Pressure Reducing 2-Way Mini-Pilot Valve","Metal"),
  ("A","PC-30-A-P","A-7","Pressure Sustaining 2-Way Mini-Pilot Valve","Plastic"),
  ("A","PC-30-A-M","A-8","Pressure Sustaining 2-Way Mini-Pilot Valve","Metal"),
  ("A","PC-3Q-A-P","A-9","Quick Pressure Relief Mini-Pilot Valve","Plastic"),
  ("A","PC-3Q-A-M","A-10","Quick Pressure Relief Mini-Pilot Valve","Metal"),
  ("A","PC-70-A-P","A-11","Paddle Flow Rate Servo Mini-Pilot Valve","Plastic"),
  ("A","PC-70-A-M","A-12","Paddle Flow Rate Servo Mini-Pilot Valve","Metal"),
  ("A","#X","A-13","Positioning 3-Way Pilot Valve",""),
  ("A","#2","A-14","Pressure Reducing Pilot Valve",""),
  ("A","#3","A-15","Pressure Sustaining Pilot Valve",""),
  ("A","#8","A-16","Altitude Positioning Pilot Valve",""),
  ("A","3W-SOP","A-17","3-Way Shut-Off Pilot for AMV",""),
  ("A","5W-SSOP","A-18","5-Way Sequential Shut-off Pilot for AMV",""),
  ("A","3W-SOP-S","A-19","3-Way Shut-Off Pilot Valve with Pump Shut-Off Switch",""),
  ("A","S-390-2W","A-20","2-Way Solenoid Valves (Burkert 5281)","Solenoid"),
  ("A","S-390-3W/S-400-3W","A-21","3-Way Solenoid Valves (Burkert 330)","Solenoid"),
  ("A","S-400-3W Burkert 6014","A-22","3-Way Solenoid Valves","Solenoid"),
  ("A","S-392-2W","A-23","2-Way Latching Solenoid Valves","Solenoid"),
  ("A","S-982/985 S-402","A-24","3-Way Magnetic Latch Solenoid Valves","Solenoid"),
  ("A","In-Line/Y-Strainer","A-25","Control Filters","Filter"),
  ("A","2-Way/3-Way Ball Valves","A-26","Ball Valves — Manometer","Ball Valve"),
  ("A","4-Way Ball Valves","A-27","Ball Valves — Manual Selector","Ball Valve"),
  ("A","50-P/M","A-28","2-Way Hydraulic Relay Valves (2W-HRV)","Relay"),
  ("A","54-PZ/M","A-29","3-Way Hydraulic Relay Valves (3W-HRV)","Relay"),
  ("A","50-X-P/M","A-30","Shuttle Valves",""),
  ("A","Flow Control (One-Way)","A-31","Flow Control Valves — One-Way",""),
  ("A","Needle Valve","A-32","Flow Control Valves — Needle/Restriction",""),
  ("A","20-P/M","A-33","Check Valves",""),
  ("A","#66 / #60-P/M","A-34","Floats",""),
  # B - On/Off
  ("B","N05-Z","B-1","Hydraulic Control Valve","Hydraulic"),
  ("B","900-DO","B-2","Automatic Metering Valve (AMV)","AMV"),
  ("B","900-DD","B-3","Automatic Metering Valve (AMV) for Sequential Irrigation","AMV"),
  ("B","N05-54-KX","B-4","Hydraulic Control Valve N.C. with Hydraulic Relay","Hydraulic"),
  ("B","N05-54-RXZ","B-5","Hydraulic Control Valve N.C. with Hydraulic Relay","Hydraulic"),
  ("B","N10-KX","B-6","Solenoid Controlled Valve","Solenoid"),
  ("B","N10-N1-2W","B-7","Solenoid Controlled Valve with 2-Way Internal Control","Solenoid"),
  ("B","N10-RX","B-8-9","Solenoid Controlled Valve","Solenoid"),
  # C - Pressure Reducing
  ("C","N20-K","C-1","Pressure Reducing 2-Way Valve","2-Way"),
  ("C","N20-R","C-2-3","Pressure Reducing 2-Way Valve","2-Way"),
  ("C","N20-50-K","C-4","Pressure Reducing 2-Way Valve with Hydraulic Control","2-Way Hydraulic"),
  ("C","N20-50-R","C-5-6","Pressure Reducing 2-Way Valve with Hydraulic Control","2-Way Hydraulic"),
  ("C","N20-54-K","C-7","Pressure Reducing 2-Way Valve N.C. with Hydraulic Relay","2-Way N.C."),
  ("C","N20-54-R","C-8","Pressure Reducing 2-Way Valve N.C. with Hydraulic Relay","2-Way N.C."),
  ("C","N20-55-K","C-9","Pressure Reducing 2-Way Valve with Solenoid Control","2-Way Solenoid"),
  ("C","N20-55-R","C-10-11","Pressure Reducing 2-Way Valve with Solenoid Control","2-Way Solenoid"),
  ("C","920-D2-R","C-12","Pressure Reducing 2-Way Valve — AMV","AMV"),
  ("C","N20-KXZ","C-13","Pressure Reducing 3-Way Valve","3-Way"),
  ("C","N20-RXZ","C-14","Pressure Reducing 3-Way Valve","3-Way"),
  ("C","N20-50-KXZ","C-15","Pressure Reducing 3-Way Valve with Hydraulic Control","3-Way Hydraulic"),
  ("C","N20-50-RXZ","C-16","Pressure Reducing 3-Way Valve with Hydraulic Control","3-Way Hydraulic"),
  ("C","N20-54-KX","C-17","Pressure Reducing 3-Way Valve N.C. with Hydraulic Relay","3-Way N.C."),
  ("C","N20-54-RXZ","C-18","Pressure Reducing 3-Way Valve N.C. with Hydraulic Relay","3-Way N.C."),
  ("C","N20-55-KX","C-19","Pressure Reducing 3-Way Valve with Solenoid Control (982/985 Only)","3-Way Solenoid"),
  ("C","N20-55-KX","C-20","Pressure Reducing 3-Way Valve with Solenoid Control","3-Way Solenoid"),
  ("C","N20-55-RX","C-21","Pressure Reducing 3-Way Valve with Solenoid Control (982/985 Only)","3-Way Solenoid"),
  ("C","N20-55-RX","C-22-23","Pressure Reducing 3-Way Valve with Solenoid Control","3-Way Solenoid"),
  ("C","920-D0-KX","C-24","Pressure Reducing 3-Way Valve — AMV","AMV"),
  ("C","920-D2-RX","C-25","Pressure Reducing 3-Way Valve — AMV","AMV"),
  ("C","N20-bKZ","C-26","Pressure Reducing 2/3-Way (Servo) Valve","Servo"),
  ("C","N20-50-bKZ","C-27","Pressure Reducing 2/3-Way (Servo) Valve with Hydraulic Control","Servo Hydraulic"),
  ("C","N20-54-bK","C-28","Pressure Reducing 2/3-Way (Servo) Valve N.C. with Hydraulic Control","Servo N.C."),
  ("C","N20-55-bK","C-29","Pressure Reducing 2/3-Way (Servo) Valve with Solenoid (982/985 Only)","Servo Solenoid"),
  ("C","N20-55-bK","C-30","Pressure Reducing 2/3-Way (Servo) Valve with Solenoid Control","Servo Solenoid"),
  # D - PR & Sustaining
  ("D","N23-K","D-1","Pressure Reducing & Sustaining 2-Way Valve","2-Way"),
  ("D","N23-R","D-2-3","Pressure Reducing & Sustaining 2-Way Valve","2-Way"),
  ("D","N23-50-K","D-4","Pressure Reducing & Sustaining 2-Way Valve with Hydraulic Control","2-Way Hydraulic"),
  ("D","N23-50-R","D-5-6","Pressure Reducing & Sustaining 2-Way Valve with Hydraulic Control","2-Way Hydraulic"),
  ("D","N23-55-K","D-7","Pressure Reducing & Sustaining 2-Way Valve with Solenoid Control","2-Way Solenoid"),
  ("D","N23-55-R","D-8-9","Pressure Reducing & Sustaining 2-Way Valve with Solenoid Control","2-Way Solenoid"),
  ("D","N23-KXZ","D-10-11","Pressure Reducing & Sustaining 3-Way Valve","3-Way"),
  ("D","N23-RXZ","D-12","Pressure Reducing & Sustaining 3-Way Valve","3-Way"),
  ("D","N23-50-KXZ","D-13","Pressure Reducing & Sustaining 3-Way with Hydraulic Control","3-Way Hydraulic"),
  ("D","N23-50-RXZ","D-14","Pressure Reducing & Sustaining 3-Way Valve with Hydraulic Control","3-Way Hydraulic"),
  ("D","N23-54-KX","D-15","Pressure Reducing & Sustaining 3-Way Valve N.C. with Hydraulic Relay","3-Way N.C."),
  ("D","N23-55-KX","D-16","Pressure Reducing & Sustaining 3-Way Valve with Solenoid (982/5 Only)","3-Way Solenoid"),
  ("D","N23-55-RXZ","D-17-18","Pressure Reducing & Sustaining 3-Way Valve with Solenoid Control","3-Way Solenoid"),
  # E - Pressure Sustaining & Relief
  ("E","N30-K","E-1","Pressure Sustaining 2-Way Valve","2-Way"),
  ("E","N30-R","E-2-3","Pressure Sustaining 2-Way Valve","2-Way"),
  ("E","N30-50-K","E-4","Pressure Sustaining 2-Way Valve with Hydraulic Control","2-Way Hydraulic"),
  ("E","N30-50-R","E-5","Pressure Sustaining 2-Way Valve with Hydraulic Control","2-Way Hydraulic"),
  ("E","N30-55-K","E-6","Pressure Sustaining 2-Way Valve with Solenoid Control","2-Way Solenoid"),
  ("E","N30-55-R","E-7-8","Pressure Sustaining 2-Way Valve with Solenoid Control","2-Way Solenoid"),
  ("E","N30-KXZ","E-9","Pressure Sustaining 3-Way Valve","3-Way"),
  ("E","N30-RXZ","E-10-11","Pressure Sustaining 3-Way Valve","3-Way"),
  ("E","N30-50-KXZ","E-12","Pressure Sustaining 3-Way Valve with Hydraulic Control","3-Way Hydraulic"),
  ("E","N30-50-RXZ","E-13","Pressure Sustaining 3-Way Valve with Hydraulic Control","3-Way Hydraulic"),
  ("E","N30-54-KX","E-14","Pressure Sustaining 3-Way Valve N.C. with Hydraulic Relay","3-Way N.C."),
  ("E","N30-55-KX","E-15","Pressure Sustaining 3-Way Valve with Solenoid (982/985 Only)","3-Way Solenoid"),
  ("E","N30-55-KX","E-16","Pressure Sustaining 3-Way Valve with Solenoid Control","3-Way Solenoid"),
  ("E","N30-55-RX","E-17","Pressure Sustaining 3-Way Valve with Solenoid (982/985 Only)","3-Way Solenoid"),
  ("E","N30-55-RX","E-18","Pressure Sustaining 3-Way Valve with Solenoid Control","3-Way Solenoid"),
  ("E","930-D0-KX","E-19","Pressure Sustaining 3-Way Valve — AMV","AMV"),
  ("E","N3Q-K","E-20","Pressure Relief Valve (Quick Type)","Quick"),
  ("E","N3Q-R","E-21","Pressure Relief Valve (Quick Type)","Quick"),
  # F - Level Control
  ("F","N50-60-R","F-1","Level Control Valve with Modulating Horizontal Float","Horizontal Float"),
  ("F","N50-N3-60-K","F-2","Level Control Valve with Modulating Horizontal Float","Horizontal Float"),
  ("F","450-66-Z","F-3-4","Level Control Valve with Bi-Level Vertical Float","Vertical Float"),
  ("F","750-66-B","F-5","Level Control Valve with Bi-Level Vertical Float","Vertical Float"),
  ("F","N50-80-XZ","F-6-7","Level Control Valve with Altitude Pilot","Altitude"),
  ("F","N53-66","F-8","Level Control & Pressure Sustaining Valve with Bi-Level Float","Bi-Level Float"),
  ("F","N57-66-U","F-9","Level & Flow Control Valve with Bi-Level Vertical Float","Bi-Level Float"),
  # G - Flow Control
  ("G","170-bDZ","G-1","Flow Control Valve (Differential Pressure Duct)","Diff. Pressure"),
  ("G","N70-bKUZ","G-2","Flow Control Valve (Orifice Assembly)","Orifice"),
  ("G","N70-bRUZ","G-3","Flow Control Valve (Orifice Assembly)","Orifice"),
  ("G","970-KVZ","G-4","Flow Control Valve (Paddle Pilot)","Paddle Pilot"),
  ("G","970-RVZ","G-5","Flow Control Valve (Paddle Pilot)","Paddle Pilot"),
  ("G","170-50-bDZ","G-6","Flow Control Valve with Hydraulic Control (Diff. Pressure Duct)","Hydraulic"),
  ("G","N70-50-bKUZ","G-7","Flow Control Valve with Hydraulic Control (Orifice Assembly)","Hydraulic"),
  ("G","N70-50-bRUZ","G-8","Flow Control Valve with Hydraulic Control (Orifice Assembly)","Hydraulic"),
  ("G","970-50-KVZ","G-9","Flow Control Valve with Hydraulic Control (Paddle Pilot)","Hydraulic"),
  ("G","970-50-RVZ","G-10","Flow Control Valve with Hydraulic Control (Paddle Pilot)","Hydraulic"),
  ("G","170-55-bD","G-11","Flow Control Valve with Solenoid Control (Diff. Pressure) — 982/985","Solenoid"),
  ("G","170-55-bD","G-12","Flow Control Valve with Solenoid Control (Differential Pressure Duct)","Solenoid"),
  ("G","N70-55-bKU","G-13","Flow Control Valve with Solenoid Control (Orifice) — 982/985 Only","Solenoid"),
  ("G","N70-55-bKU","G-14","Flow Control Valve with Solenoid Control (Orifice Assembly)","Solenoid"),
  ("G","N70-55-bRU","G-15","Flow Control Valve with Solenoid Control (Orifice Assembly)","Solenoid"),
  ("G","970-55-KV","G-16","Flow Control Valve with Solenoid Control (Paddle Pilot) — 982/985","Solenoid"),
  ("G","970-55-KV","G-17","Flow Control Valve with Solenoid Control (Paddle Pilot)","Solenoid"),
  # H - Flow Control & PR
  ("H","172-bDZ","H-1","Flow Control & Pressure Reducing Valve (Differential Pressure Duct)","Diff. Pressure"),
  ("H","N72-bKUZ","H-2","Flow Control & Pressure Reducing Valve (Orifice Assembly)","Orifice"),
  ("H","N72-bRU","H-3","Flow Control & Pressure Reducing Valve (Orifice Assembly)","Orifice"),
  ("H","972-KVZ","H-4","Flow Control & Pressure Reducing Valve (Paddle Pilot)","Paddle Pilot"),
  ("H","972-RV","H-5","Flow Control & Pressure Reducing Valve (Paddle Pilot)","Paddle Pilot"),
  ("H","172-50-bDZ","H-6","Flow Control & Pressure Reducing with Hydraulic Control (Diff. Pressure)","Hydraulic"),
  ("H","172-55-bD","H-7","Flow Control & Pressure Reducing with Solenoid Control (Diff. Pressure)","Solenoid"),
  ("H","N72-50-bKUZ","H-8","Flow Control & Pressure Reducing with Hydraulic Control (Orifice)","Hydraulic"),
  ("H","N72-50-bRU","H-9","Flow Control & Pressure Reducing with Hydraulic Control (Orifice)","Hydraulic"),
  ("H","N72-55-bKU","H-10","Flow Control & Pressure Reducing with Solenoid Control (Orifice)","Solenoid"),
  ("H","N72-55-bKU","H-11","Flow Control & Pressure Reducing with Solenoid Control (Orifice)","Solenoid"),
  ("H","N72-55-bRU","H-12","Flow Control & Pressure Reducing with Solenoid Control (Orifice)","Solenoid"),
  ("H","972-50-KV","H-13","Flow Control & Pressure Reducing with Hydraulic Control (Paddle Pilot)","Hydraulic"),
  ("H","972-50-RV","H-14","Flow Control & Pressure Reducing with Hydraulic Control (Paddle Pilot)","Hydraulic"),
  ("H","972-MO-55-bKV","H-15-16","Flow Control & Pressure Reducing with Hydraulic Control (Paddle Pilot)","Hydraulic"),
  ("H","972-MO-55-RV","H-17","Flow Control & Pressure Reducing with Hydraulic Control (Paddle Pilot)","Hydraulic"),
]

# Intro pages (1-13)
INTRO = [
  ('', 1,  'intro', 'Cover — BERMAD Irrigation Control Circuits & Accessories Pocket Guide', ''),
  ('', 2,  'intro', 'How to Use this Pocket Guide', ''),
  ('', 3,  'intro', 'Introduction — BERMAD IR Pocket Guide', ''),
  ('', 4,  'intro', 'Valve Type Identification According to Series (100/200/300/400)', ''),
  ('', 5,  'intro', 'Index — Category A: Accessories (A-1 to A-17)', ''),
  ('', 6,  'intro', 'Index — Category A: Accessories (A-18 to A-34)', ''),
  ('', 7,  'intro', 'Index — Categories B (On/Off) and C (Pressure Reducing, C-1 to C-9)', ''),
  ('', 8,  'intro', 'Index — Category C: Pressure Reducing (C-10 to C-28)', ''),
  ('', 9,  'intro', 'Index — Categories C (C-29/C-30) and D (Pressure Reducing & Sustaining)', ''),
  ('', 10, 'intro', 'Index — Categories D (continued) and E (Pressure Sustaining & Relief)', ''),
  ('', 11, 'intro', 'Index — Categories E (continued) and F (Level Control)', ''),
  ('', 12, 'intro', 'Index — Category G: Flow Control Valves', ''),
  ('', 13, 'intro', 'Index — Category H: Flow Control & Pressure Reducing Valves', ''),
]

# Calcular páginas dos diagramas
diagram_page = 14
INDEX_DIAG = []
for cat, model, label, desc, info in RAW:
    INDEX_DIAG.append((model, diagram_page, cat.lower(), desc, info))
    diagram_page += npages(label)

MAX_PAGE = diagram_page - 1  # última página com conteúdo
INDEX = INTRO + INDEX_DIAG
print(f"Entradas: {len(INDEX)} ({len(INTRO)} intro + {len(INDEX_DIAG)} diagramas), última pág: {MAX_PAGE}/170")

# ── Categorias ────────────────────────────────────────────────────────────────
CATS = {
  'intro': ('📄', 'Introduction / Index',          '#607080', '#f4f8fb', '#d0e4f0'),
  'a':     ('⚙️',  'A — Accessories',               '#e65100', '#fff3e0', '#ffcc80'),
  'b':     ('⬛', 'B — On/Off Control',             '#0d47a1', '#e3f2fd', '#90caf9'),
  'c':     ('🔴', 'C — Pressure Reducing',          '#b71c1c', '#ffebee', '#ef9a9a'),
  'd':     ('🟠', 'D — PR & Sustaining',            '#e65100', '#fff3e0', '#ffcc80'),
  'e':     ('🟣', 'E — Pressure Sustaining & Relief','#4a148c','#f3e5f5', '#ce93d8'),
  'f':     ('🌊', 'F — Level Control',              '#0277bd', '#e1f5fe', '#81d4fa'),
  'g':     ('💧', 'G — Flow Control',               '#00695c', '#e0f2f1', '#80cbc4'),
  'h':     ('🔗', 'H — Flow Control & PR',          '#880e4f', '#fce4ec', '#f48fb1'),
}

HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BERMAD Diagrams — Bolsa Irriga</title>
<style>
:root{{
  --bl:#005f8e;--bl2:#0077b6;--tx:#1a2535;--mu:#607080;--bg:#f4f7fb;--bdr:#d0e4f0;
  --sh:0 2px 12px rgba(0,80,160,.10);
}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--tx);font-size:14px;height:100vh;display:flex;flex-direction:column}}
header{{background:linear-gradient(135deg,#1a3a5c,#1565c0,#1976d2);color:#fff;flex-shrink:0;box-shadow:0 3px 16px rgba(0,0,0,.2)}}
.hdr{{padding:.6rem 1rem;display:flex;justify-content:space-between;align-items:center;gap:.8rem;flex-wrap:wrap}}
.hdr-logo{{display:flex;align-items:center;gap:.7rem}}
.hdr-logo img{{height:52px;width:52px;object-fit:contain;background:#fff;border-radius:8px;padding:5px}}
.hdr-brand h1{{font-size:1.1rem;font-weight:800}}
.hdr-brand p{{font-size:.72rem;opacity:.85}}
.hdr-dev{{font-size:.68rem;line-height:1.6;opacity:.9;text-align:right}}
.hdr-dev b{{font-size:.78rem}}
.main{{display:flex;flex:1;overflow:hidden}}
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
.item .model{{font-size:.78rem;font-weight:800;min-width:50px;flex-shrink:0}}
.item .desc{{font-size:.78rem;line-height:1.25;color:var(--tx)}}
.item .pilot{{font-size:.67rem;color:var(--mu);margin-top:.05rem}}
.item .pg{{font-size:.67rem;font-weight:700;color:var(--mu);margin-left:auto;flex-shrink:0;padding-left:.4rem}}
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
        <h1>BERMAD — Control Circuits &amp; Accessories</h1>
        <p>Irrigation Pocket Guide &middot; {len(INDEX_DIAG)} diagrams &middot; 8 categories (A&ndash;H) &middot; 170 pages</p>
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
      <h2>&#128269; Search Diagram</h2>
      <div class="search-wrap">
        <input type="text" id="search" placeholder="Model, type or description..." oninput="filter()">
      </div>
      <div class="cat-filters" id="cat-filters"></div>
    </div>
    <div class="sb-list" id="sb-list"></div>
  </aside>

  <div class="viewer">
    <div class="viewer-bar">
      <button class="btn-nav" onclick="navPage(-1)">&#9664;</button>
      <input class="pg-input" type="number" id="pg-input" min="1" max="170" value="1" onchange="goPage(this.value)">
      <span class="pg-info">/ 170</span>
      <button class="btn-nav" onclick="navPage(1)">&#9654;</button>
      <span class="pg-info" id="pg-title" style="flex:1;color:var(--tx);font-size:.8rem"></span>
      <button class="btn-open" onclick="openPDF()">&#128196; Open full PDF</button>
    </div>
    <div class="viewer-frame">
      <iframe id="pdf-frame" src="bermad.pdf#page=1" title="BERMAD Diagrams"></iframe>
      <div class="mobile-msg">
        <p>&#128241; On mobile, tap an item to open the diagram:</p>
        <p style="margin-top:.5rem"><a href="bermad.pdf" target="_blank">&#128196; Open full PDF &#8594;</a></p>
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
  btn('all','All','#005f8e','#e8f4fd');
  Object.entries(CATS).forEach(([k,v])=>btn(k,v[0]+' '+v[1].split(' ').slice(2).join(' ').split('(')[0].trim(),v[2],v[3]));
}}

function buildList(items){{
  const d=document.getElementById('sb-list');
  d.innerHTML='';
  let lastCat='';
  items.forEach(item=>{{
    const [model,page,cat,desc,info]=item;
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
    a.innerHTML=`${{modelHtml}}<div><div class="desc">${{desc}}</div>${{info?`<div class="pilot">${{info}}</div>`:''}}</div><span class="pg">p.${{page}}</span>`;
    a.onclick=e=>{{e.preventDefault();goPage(page);}};
    a.dataset.page=page;
    d.appendChild(a);
  }});
  if(!items.length) d.innerHTML='<p style="padding:1rem;color:var(--mu);text-align:center;font-size:.83rem">No results found.</p>';
}}

function filter(){{
  const q=document.getElementById('search').value.toLowerCase().trim();
  let items=INDEX;
  if(activeCat!=='all') items=items.filter(x=>x[2]===activeCat);
  if(q) items=items.filter(x=>x[0].toLowerCase().includes(q)||x[3].toLowerCase().includes(q)||x[4].toLowerCase().includes(q));
  buildList(items);
  document.querySelectorAll('.item').forEach(el=>{{
    el.classList.toggle('active',parseInt(el.dataset.page)===currentPage);
  }});
}}

function goPage(n){{
  n=Math.max(1,Math.min(170,parseInt(n)||1));
  currentPage=n;
  document.getElementById('pg-input').value=n;
  document.getElementById('pdf-frame').src='bermad.pdf#page='+n;
  const item=INDEX.find(x=>x[1]===n);
  const title=item?(item[0]?item[0]+' — ':'')+item[3]:'';
  document.getElementById('pg-title').textContent=title;
  document.querySelectorAll('.item').forEach(el=>{{
    const active=parseInt(el.dataset.page)===n;
    el.classList.toggle('active',active);
    if(active) el.scrollIntoView({{block:'nearest',behavior:'smooth'}});
  }});
  if(window.innerWidth<=700) window.open('bermad.pdf#page='+n,'_blank');
}}

function navPage(d){{goPage(currentPage+d);}}
function openPDF(){{window.open('bermad.pdf','_blank');}}

buildFilters();
buildList(INDEX);
goPage(1);
</script>
</body>
</html>"""

# Copiar PDF se necessário
if os.path.exists('BERMAD-Pocket-Guide-English.pdf') and not os.path.exists('bermad.pdf'):
    shutil.copy2('BERMAD-Pocket-Guide-English.pdf','bermad.pdf')
    print("PDF copiado: bermad.pdf")

with open('bermad.html','w',encoding='utf-8') as f:
    f.write(HTML)
print(f"OK - {len(HTML):,} bytes - bermad.html ({len(INDEX)} entradas)")
