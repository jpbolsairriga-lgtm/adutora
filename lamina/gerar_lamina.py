import base64, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('logo perfil branca.png','rb') as f:
    LOGO = base64.b64encode(f.read()).decode()

HTML = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lâmina × Vazão — Bolsa Irriga</title>
<style>
:root{
  --bl:#005f8e;--bl2:#0077b6;--bl3:#00b4d8;--bl4:#caf0f8;
  --gn:#1b6e3a;--gn2:#2d9e5a;--gn3:#d4edda;
  --rd:#c62828;--am:#e07b00;--am2:#fff8e1;
  --bg:#f4f7fb;--bdr:#d0e4f0;--tx:#1a2535;--mu:#607080;
  --sh:0 2px 16px rgba(0,80,160,.10);
  --gr1:#2e7d32;--gr2:#388e3c;--gr3:#c8e6c9;
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--tx);font-size:14px}
header{background:linear-gradient(135deg,#1b5e20,var(--gr1),var(--gr2));color:#fff;box-shadow:0 3px 20px rgba(0,0,0,.2)}
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
.ct{font-size:.76rem;font-weight:800;color:var(--gr1);text-transform:uppercase;letter-spacing:.08em;margin-bottom:.8rem;padding-bottom:.48rem;border-bottom:2px solid var(--gr3);display:flex;align-items:center;gap:.45rem}
.ct::before{content:'';width:4px;height:1.1em;background:var(--gr2);border-radius:2px;flex-shrink:0}
.sn{display:inline-flex;width:20px;height:20px;background:var(--gr1);color:#fff;border-radius:50%;align-items:center;justify-content:center;font-size:.72rem;font-weight:900;flex-shrink:0}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
.g3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:.8rem}
.g4{display:grid;grid-template-columns:repeat(4,1fr);gap:.7rem}
.g5{display:grid;grid-template-columns:repeat(5,1fr);gap:.7rem}
@media(max-width:900px){.g2{grid-template-columns:1fr}.g3{grid-template-columns:1fr 1fr}.g4,.g5{grid-template-columns:1fr 1fr}}
@media(max-width:540px){.g3,.g4,.g5{grid-template-columns:1fr}}
.fg{display:flex;flex-direction:column;gap:.2rem}
label{font-size:.72rem;font-weight:700;color:var(--mu);text-transform:uppercase;letter-spacing:.05em}
.fg small{font-size:.67rem;color:var(--mu);margin-top:.08rem}
.iu{display:flex}
.iu input,.iu select{flex:1;border-radius:8px 0 0 8px}
.iu .u{background:var(--bdr);border:1.5px solid var(--bdr);border-left:none;padding:.48rem .55rem;font-size:.77rem;color:var(--mu);border-radius:0 8px 8px 0;white-space:nowrap;display:flex;align-items:center}
input[type=number],input[type=text],input[type=date],select{padding:.48rem .68rem;border:1.5px solid var(--bdr);border-radius:8px;font-size:.9rem;color:var(--tx);background:#fafeff;outline:none;transition:border-color .18s,box-shadow .18s;width:100%}
input:focus,select:focus{border-color:var(--gr2);box-shadow:0 0 0 3px rgba(46,125,50,.13)}
.tile{border-radius:10px;padding:.75rem .9rem}
.tg{background:linear-gradient(135deg,#e8f5e9,#c8e6c9);border:1px solid #a5d6a7}
.tt{background:linear-gradient(135deg,#e0f7fa,#b2ebf2);border:1px solid #80deea}
.tb2{background:linear-gradient(135deg,#e8f4fd,#d0eaf8);border:1px solid #a8d4f0}
.to{background:linear-gradient(135deg,#fff3e0,#ffe0b2);border:1px solid #ffcc80}
.tr{background:linear-gradient(135deg,#ffebee,#ffcdd2);border:1px solid #ef9a9a}
.tl{font-size:.67rem;font-weight:800;color:var(--gr1);text-transform:uppercase;letter-spacing:.06em;margin-bottom:.15rem}
.tv{font-size:1.15rem;font-weight:900;color:#003d5c;line-height:1.1}
.tv.lg{font-size:1.35rem}
.tv small{font-size:.7rem;font-weight:500;color:var(--mu);margin-left:.1rem}
.sbox{padding:.75rem 1rem;border-radius:8px;font-size:.84rem;line-height:1.5}
.sbox.info{background:#e8f5e9;border-left:4px solid var(--gr2);color:#1b4d2e}
.sbox.warn{background:var(--am2);border-left:4px solid #f59e0b;color:#7c4d00}
.sbox.ok{background:var(--gn3);border-left:4px solid var(--gn2);color:#1b4d2e}
.sbox.err{background:#ffebee;border-left:4px solid var(--rd);color:#7f0000}
/* lamina badge */
.lam-badge{display:inline-block;padding:.3rem 1rem;border-radius:16px;font-size:1.1rem;font-weight:900;background:linear-gradient(135deg,#2e7d32,#388e3c);color:#fff;box-shadow:0 2px 10px rgba(46,125,50,.3)}
/* table */
.tbl-wrap{overflow-x:auto}
.ltbl{width:100%;border-collapse:collapse;font-size:.88rem}
.ltbl th{padding:.5rem .8rem;font-size:.7rem;font-weight:800;text-transform:uppercase;text-align:center;background:#e8f5e9;border:1px solid #c8e6c9;color:var(--gr1)}
.ltbl th.lh{text-align:left}
.ltbl td{padding:.42rem .8rem;border:1px solid #e8f0ea;text-align:center;vertical-align:middle}
.ltbl tr:hover td{background:#f1f9f2}
.ltbl .row-avail{background:linear-gradient(90deg,#e8f5e9,#c8e6c9)!important;font-weight:900}
.ltbl .row-avail td{color:#1b5e20!important;border-color:#a5d6a7!important}
.ltbl .row-target{background:linear-gradient(90deg,#e3f2fd,#bbdefb)!important;font-weight:800}
.ltbl .row-target td{color:#0d47a1!important;border-color:#90caf9!important}
.ltbl .row-over{background:#f9fefe}
.ltbl .row-under{background:#fff8f8}
.ltbl td.lam-val{font-weight:800;font-size:.95rem}
.ltbl td.vazao-val{font-weight:700}
.ltbl td.status-ok{color:var(--gr1)}
.ltbl td.status-no{color:var(--rd)}
.ltbl .badge{display:inline-block;padding:.1rem .5rem;border-radius:8px;font-size:.7rem;font-weight:800}
.badge-ok{background:#e8f5e9;color:var(--gr1);border:1px solid #a5d6a7}
.badge-no{background:#ffebee;color:var(--rd);border:1px solid #ef9a9a}
.badge-avail{background:linear-gradient(135deg,#2e7d32,#388e3c);color:#fff;padding:.2rem .6rem}
.badge-tgt{background:linear-gradient(135deg,#0d47a1,#1976d2);color:#fff;padding:.2rem .6rem}
/* canvas */
.cf2{background:#fff;border-radius:10px;border:2px solid #c8e6c9;box-shadow:0 4px 20px rgba(46,125,50,.08);overflow:hidden}
.cl{background:var(--gr3);color:var(--gr1);font-size:.71rem;font-weight:800;text-transform:uppercase;letter-spacing:.07em;padding:.3rem .8rem;text-align:center;border-bottom:1px solid #a5d6a7}
canvas{display:block;max-width:100%}
.btn{padding:.65rem 1.4rem;border:none;border-radius:8px;font-size:.88rem;font-weight:700;cursor:pointer;transition:all .18s;display:inline-flex;align-items:center;gap:.4rem}
.bpdf{background:linear-gradient(135deg,#b71c1c,#880e4f);color:#fff;padding:.72rem 1.8rem}
.bpdf:hover{transform:translateY(-1px);box-shadow:0 4px 16px rgba(183,28,28,.38)}
.bg{background:var(--bdr);color:var(--tx)}.bg:hover{background:#b8d8ee}
.abar{display:flex;justify-content:flex-end;gap:.75rem;padding:.3rem 0 .9rem;flex-wrap:wrap}
footer{background:#fff;border-top:2px solid var(--bdr);padding:1rem 1.5rem;margin-top:.5rem}
.fi{max-width:1320px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem}
.fd{display:flex;align-items:center;gap:.75rem}
.fd img{height:40px;width:40px;object-fit:contain;border-radius:7px;padding:3px;background:#f0f7ff;border:1px solid var(--bdr)}
.fdn .fn{font-weight:800;color:var(--gr1);font-size:.88rem}
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
        <h1>L&#226;mina de Irriga&#231;&#227;o &times; Vaz&#227;o</h1>
        <p>Dimensionamento de L&#226;mina &middot; Turno &middot; &#193;rea &middot; C&#225;lculo Bidirecional &middot; Tabela Interativa</p>
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

<!-- LEFT: INPUTS -->
<div>
  <div class="card">
    <div class="ct"><span class="sn">1</span> Par&#226;metros do Sistema</div>
    <div class="g2">
      <div class="fg"><label>&#193;rea Total a Irrigar</label>
        <div class="iu"><input type="number" id="area" value="" min="0.1" step="0.5" oninput="calc()"><span class="u">ha</span></div></div>
      <div class="fg"><label>Turno de Irriga&#231;&#227;o</label>
        <div class="iu"><input type="number" id="turno" value="" min="1" max="24" step="0.5" oninput="calc()"><span class="u">h/dia</span></div>
        <small>Horas dispon&#237;veis por dia para irrigar</small></div>
      <div class="fg"><label>Vaz&#227;o Dispon&#237;vel</label>
        <div class="iu"><input type="number" id="vazao" value="" min="0" step="1" oninput="calc()"><span class="u">m&#179;/h</span></div>
        <small>Capacidade m&#225;xima do sistema/fonte</small></div>
      <div class="fg"><label>L&#226;mina Alvo (opcional)</label>
        <div class="iu"><input type="number" id="laminaAlvo" value="" min="0" step="0.5" oninput="calc()"><span class="u">mm/dia</span></div>
        <small>Para calcular a vaz&#227;o necess&#225;ria</small></div>
    </div>
  </div>

  <div class="card">
    <div class="ct"><span class="sn">2</span> Par&#226;metros da Tabela</div>
    <div class="g2">
      <div class="fg"><label>L&#226;mina m&#237;nima</label>
        <div class="iu"><input type="number" id="lamMin" value="" min="0.1" max="5" step="0.5" oninput="calc()"><span class="u">mm/dia</span></div></div>
      <div class="fg"><label>L&#226;mina m&#225;xima</label>
        <div class="iu"><input type="number" id="lamMax" value="" min="5" max="50" step="1" oninput="calc()"><span class="u">mm/dia</span></div></div>
      <div class="fg"><label>Incremento</label>
        <div class="iu"><input type="number" id="lamStep" value="" min="0.1" max="2" step="0.1" oninput="calc()"><span class="u">mm/dia</span></div></div>
      <div class="fg"><label>Efici&#234;ncia do Sistema</label>
        <div class="iu"><input type="number" id="efic" value="" min="50" max="100" step="1" oninput="calc()"><span class="u">%</span></div>
        <small>Gotejamento: 90&ndash;95%, Aspersor: 75&ndash;85%</small></div>
    </div>
  </div>

  <div class="card">
    <div class="ct"><span class="sn">3</span> Refer&#234;ncias de L&#226;mina (mm/dia)</div>
    <div style="font-size:.82rem;line-height:1.9;color:var(--tx)">
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:.3rem .8rem">
        <div><span style="font-weight:700;color:var(--gr1)">Gotejamento &mdash; Hortic.</span><br>2&ndash;6 mm/dia</div>
        <div><span style="font-weight:700;color:var(--gr1)">Gotejamento &mdash; Frutif.</span><br>3&ndash;8 mm/dia</div>
        <div><span style="font-weight:700;color:#0077b6">Aspersor &mdash; Pastagem</span><br>4&ndash;8 mm/dia</div>
        <div><span style="font-weight:700;color:#0077b6">Aspersor &mdash; Cana/Milho</span><br>5&ndash;10 mm/dia</div>
        <div><span style="font-weight:700;color:var(--am)">Microaspersor &mdash; C&#237;trus</span><br>3&ndash;6 mm/dia</div>
        <div><span style="font-weight:700;color:var(--am)">Pivô Central &mdash; Gr&#227;os</span><br>5&ndash;12 mm/dia</div>
      </div>
      <div class="sbox info" style="margin-top:.6rem;font-size:.78rem">
        A l&#226;mina necess&#225;ria depende da ETo local, coeficiente da cultura (Kc) e efici&#234;ncia do sistema.<br>
        <strong>L&#226;mina bruta = ETc / Efici&#234;ncia &nbsp;|&nbsp; ETc = ETo &times; Kc</strong>
      </div>
    </div>
  </div>
</div>

<!-- RIGHT: RESULTS -->
<div>
  <div class="card">
    <div class="ct">&#127807; L&#226;mina com Vaz&#227;o Dispon&#237;vel</div>
    <div id="res-lamina"><div class="sbox info">Preencha &#225;rea, turno e vaz&#227;o para calcular.</div></div>
  </div>
  <div class="card">
    <div class="ct">&#128200; Vaz&#227;o para L&#226;mina Alvo</div>
    <div id="res-vazao"><div class="sbox info">Preencha a l&#226;mina alvo para calcular.</div></div>
  </div>
  <div class="card">
    <div class="ct">Volumes por Ciclo</div>
    <div id="res-volumes"><div class="sbox info">Aguardando dados...</div></div>
  </div>
</div>

</div><!-- /g2 -->

<!-- GRÁFICO -->
<div class="card">
  <div class="ct">Gr&#225;fico &mdash; L&#226;mina &times; Vaz&#227;o Necess&#225;ria</div>
  <div class="cl">CURVA DE DEMANDA H&#205;DRICA &middot; L&#194;MINA (mm/dia) &times; VAZ&#195;O (m&#179;/h)</div>
  <div class="cf2"><canvas id="c-graf" width="1260" height="340"></canvas></div>
</div>

<!-- TABELA -->
<div class="card">
  <div class="ct"><span class="sn">T</span> Tabela de L&#226;mina de Irriga&#231;&#227;o &mdash; L&#226;mina &times; Vaz&#227;o Necess&#225;ria</div>
  <div class="tbl-wrap">
    <table class="ltbl" id="ltbl">
      <thead>
        <tr>
          <th class="lh">L&#226;mina</th>
          <th>Vol. Bruto/ha</th>
          <th>Vol. Total (ha)</th>
          <th>Vaz&#227;o Necess&#225;ria</th>
          <th>Status</th>
          <th>Diferen&#231;a</th>
        </tr>
      </thead>
      <tbody id="ltbl-body">
        <tr><td colspan="6" style="text-align:center;color:var(--mu);padding:1rem">Preencha os dados para gerar a tabela.</td></tr>
      </tbody>
    </table>
  </div>
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
    <div class="fc">Bolsa Irriga&#174; &mdash; L&#226;mina &times; Vaz&#227;o v1.0<br>
      Av. Elias Abr&#227;o, n&#186; 140 &middot; Franca &#8211; SP &middot; (16) 3702-6571<br>
      &copy; 2025 Jo&#227;o Paulo de Oliveira</div>
  </div>
</footer>

<script>
const $=id=>document.getElementById(id);
const gv=id=>parseFloat($(id).value)||0;
const fmt=(n,d=2)=>n==null||isNaN(n)||!isFinite(n)?'—':n.toLocaleString('pt-BR',{minimumFractionDigits:d,maximumFractionDigits:d});
const LOGO='##LOGO##';

// ── FÓRMULAS CENTRAIS ─────────────────────────────────────────────────
// Lâmina (mm/dia) = Vazão (m³/h) × Turno (h) / (Área (ha) × 10)
// Vazão (m³/h)   = Lâmina (mm/dia) × Área (ha) × 10 / Turno (h)
// 1 mm × 1 ha   = 0.001 m × 10000 m² = 10 m³
function vazaoParaLamina(vazao, turno, area){
  if(!area||!turno) return null;
  return vazao * turno / (area * 10);
}
function laminaParaVazao(lamina, area, turno){
  if(!turno) return null;
  return lamina * area * 10 / turno;
}
function volTotal(lamina, area){ return lamina * area * 10; }

// ── ESTADO GLOBAL ─────────────────────────────────────────────────────
let _tableData=[];

// ── CALC PRINCIPAL ────────────────────────────────────────────────────
function calc(){
  const area=gv('area'), turno=gv('turno'), vazaoDisp=gv('vazao');
  const laminaAlvo=gv('laminaAlvo'), efic=gv('efic')||90;
  const lamMin=gv('lamMin')||0.5, lamMax=gv('lamMax')||15, lamStep=gv('lamStep')||0.5;

  // Lâmina com vazão disponível
  if(area&&turno&&vazaoDisp){
    const lam=vazaoParaLamina(vazaoDisp,turno,area);
    const lamLiq=lam*(efic/100); // lâmina líquida (efetivamente aplicada)
    const vol=volTotal(lam,area);
    $('res-lamina').innerHTML=`
      <div style="text-align:center;margin-bottom:.8rem">
        <div style="font-size:.72rem;font-weight:800;color:var(--gr1);text-transform:uppercase;margin-bottom:.3rem">L&#226;mina Bruta Aplic&#225;vel</div>
        <span class="lam-badge">${fmt(lam,2)} mm/dia</span>
        <div style="font-size:.75rem;color:var(--mu);margin-top:.4rem">L&#226;mina l&#237;quida: <strong>${fmt(lamLiq,2)} mm/dia</strong> (efic. ${efic}%)</div>
      </div>
      <div class="g3">
        <div class="tile tg"><div class="tl">Vaz&#227;o</div><div class="tv">${fmt(vazaoDisp)} <small>m&#179;/h</small></div></div>
        <div class="tile tg"><div class="tl">Turno</div><div class="tv">${fmt(turno,1)} <small>h/dia</small></div></div>
        <div class="tile tg"><div class="tl">&#193;rea</div><div class="tv">${fmt(area)} <small>ha</small></div></div>
      </div>`;
    $('res-volumes').innerHTML=`
      <div class="g2" style="margin-bottom:.5rem">
        <div class="tile tt"><div class="tl">Volume bruto/ciclo</div><div class="tv">${fmt(vol)} <small>m&#179;</small></div></div>
        <div class="tile tt"><div class="tl">Volume l&#237;q./ciclo</div><div class="tv">${fmt(vol*efic/100)} <small>m&#179;</small></div></div>
      </div>
      <div class="g2">
        <div class="tile tb2"><div class="tl">Vol. bruto/ha</div><div class="tv">${fmt(lam*10)} <small>m&#179;/ha</small></div></div>
        <div class="tile tb2"><div class="tl">Vol. l&#237;q./ha</div><div class="tv">${fmt(lamLiq*10)} <small>m&#179;/ha</small></div></div>
      </div>`;
  } else {
    $('res-lamina').innerHTML='<div class="sbox info">Preencha &#225;rea, turno e vaz&#227;o para calcular.</div>';
    $('res-volumes').innerHTML='<div class="sbox info">Aguardando dados...</div>';
  }

  // Vazão para lâmina alvo
  if(laminaAlvo&&area&&turno){
    const vazNec=laminaParaVazao(laminaAlvo,area,turno);
    const ok=vazaoDisp>0&&vazNec<=vazaoDisp;
    const diff=vazaoDisp>0?vazaoDisp-vazNec:null;
    $('res-vazao').innerHTML=`
      <div style="text-align:center;margin-bottom:.7rem">
        <div style="font-size:.72rem;font-weight:800;color:#0077b6;text-transform:uppercase;margin-bottom:.3rem">Vaz&#227;o Necess&#225;ria</div>
        <span style="display:inline-block;padding:.3rem 1rem;border-radius:16px;font-size:1.1rem;font-weight:900;background:linear-gradient(135deg,#0d47a1,#1976d2);color:#fff;box-shadow:0 2px 10px rgba(13,71,161,.3)">${fmt(vazNec)} m&#179;/h</span>
      </div>
      <div class="g2">
        <div class="tile tb2"><div class="tl">L&#226;mina alvo</div><div class="tv">${fmt(laminaAlvo,1)} <small>mm/dia</small></div></div>
        <div class="tile ${ok?'tg':'tr'}"><div class="tl">${ok?'Sobra de vaz&#227;o':'Deficit de vaz&#227;o'}</div>
          <div class="tv" style="color:${ok?'var(--gr1)':'var(--rd)'}">${diff!=null?fmt(Math.abs(diff)):'-'} <small>m&#179;/h</small></div></div>
      </div>
      ${diff!=null?`<div class="sbox ${ok?'ok':'err'}" style="margin-top:.5rem;font-size:.82rem">${ok?`&#10003; Vaz&#227;o dispon&#237;vel (${fmt(vazaoDisp)} m&#179;/h) <strong>suficiente</strong> para l&#226;mina de ${fmt(laminaAlvo,1)} mm/dia. Sobram ${fmt(diff)} m&#179;/h.`:`&#9888; Vaz&#227;o dispon&#237;vel (${fmt(vazaoDisp)} m&#179;/h) <strong>insuficiente</strong>. Faltam ${fmt(Math.abs(diff))} m&#179;/h para atingir ${fmt(laminaAlvo,1)} mm/dia.`}</div>`:''}`;
  } else {
    $('res-vazao').innerHTML='<div class="sbox info">Preencha a l&#226;mina alvo para calcular a vaz&#227;o necess&#225;ria.</div>';
  }

  // Gerar tabela e gráfico
  if(area&&turno){
    buildTable(area,turno,vazaoDisp,laminaAlvo,efic,lamMin,lamMax,lamStep);
    drawGraf(area,turno,vazaoDisp,laminaAlvo,lamMin,lamMax);
  }
}

// ── TABELA ────────────────────────────────────────────────────────────
function buildTable(area,turno,vazaoDisp,laminaAlvo,efic,lamMin,lamMax,lamStep){
  _tableData=[];
  let html='';
  for(let lam=lamMin;lam<=lamMax+0.001;lam+=lamStep){
    lam=Math.round(lam*10)/10;
    const vNec=laminaParaVazao(lam,area,turno);
    const vol=volTotal(lam,area);
    const volHa=lam*10;
    const ok=vazaoDisp>0&&vNec<=vazaoDisp;
    const diff=vazaoDisp>0?vazaoDisp-vNec:null;
    const isAvail=vazaoDisp>0&&Math.abs(lam-vazaoParaLamina(vazaoDisp,turno,area))<lamStep*0.6;
    const isTgt=laminaAlvo>0&&Math.abs(lam-laminaAlvo)<lamStep*0.6;
    let rowCls=ok?'row-over':'row-under';
    if(isAvail) rowCls='row-avail';
    else if(isTgt) rowCls='row-target';
    const badge=isAvail?'<span class="badge badge-avail">&#9654; Dispon&#237;vel</span>':
                isTgt?'<span class="badge badge-tgt">&#9654; Alvo</span>':
                ok?'<span class="badge badge-ok">&#10003;</span>':'<span class="badge badge-no">&#10005;</span>';
    html+=`<tr class="${rowCls}">
      <td class="lam-val" style="text-align:left;padding-left:.9rem">${fmt(lam,1)} mm/dia</td>
      <td>${fmt(volHa,1)} m&#179;/ha</td>
      <td>${fmt(vol)} m&#179;</td>
      <td class="vazao-val">${fmt(vNec)} m&#179;/h</td>
      <td>${badge}</td>
      <td class="${ok?'status-ok':'status-no'}">${diff!=null?(ok?'+':'')+fmt(diff)+' m&#179;/h':'—'}</td>
    </tr>`;
    _tableData.push({lam,vNec,vol,volHa,ok,isAvail,isTgt});
  }
  $('ltbl-body').innerHTML=html;
}

// ── GRÁFICO ───────────────────────────────────────────────────────────
function drawGraf(area,turno,vazaoDisp,laminaAlvo,lamMin,lamMax){
  const cv=$('c-graf'),ctx=cv.getContext('2d');
  const W=cv.width,H=cv.height;
  ctx.clearRect(0,0,W,H);
  ctx.fillStyle='#f9fdf9';ctx.fillRect(0,0,W,H);

  if(!area||!turno){
    ctx.fillStyle='#9aabbc';ctx.font='16px Segoe UI';ctx.textAlign='center';
    ctx.fillText('Preencha área e turno para ver o gráfico',W/2,H/2);return;
  }

  const mg={t:44,b:58,l:82,r:48};
  const cW=W-mg.l-mg.r,cH=H-mg.t-mg.b;

  // Range
  const lamRange=[lamMin,lamMax];
  const vazMax=laminaParaVazao(lamMax,area,turno)*1.08;
  const px=lam=>mg.l+(lam-lamMin)/(lamMax-lamMin)*cW;
  const py=vaz=>mg.t+cH*(1-vaz/vazMax);

  // Grade
  ctx.strokeStyle='rgba(46,125,50,.08)';ctx.lineWidth=1;
  for(let i=0;i<=6;i++){
    const v=vazMax*i/6,y=py(v);
    ctx.beginPath();ctx.moveTo(mg.l,y);ctx.lineTo(mg.l+cW,y);ctx.stroke();
    ctx.fillStyle='#607080';ctx.font='10px Segoe UI';ctx.textAlign='right';
    ctx.fillText(fmt(v,0)+' m³/h',mg.l-5,y+4);
  }
  for(let i=0;i<=8;i++){
    const l=lamMin+i*(lamMax-lamMin)/8,x=px(l);
    ctx.beginPath();ctx.moveTo(x,mg.t);ctx.lineTo(x,mg.t+cH);ctx.stroke();
    ctx.fillStyle='#607080';ctx.font='10px Segoe UI';ctx.textAlign='center';
    ctx.fillText(fmt(l,1),x,mg.t+cH+16);
  }
  ctx.fillStyle='#607080';ctx.textAlign='center';
  ctx.fillText('Lâmina de Irrigação (mm/dia)',mg.l+cW/2,mg.t+cH+32);
  ctx.save();ctx.translate(14,mg.t+cH/2);ctx.rotate(-Math.PI/2);
  ctx.fillText('Vazão Necessária (m³/h)',0,0);ctx.restore();

  // Área verde (abaixo da linha de disponível)
  if(vazaoDisp>0){
    const y0=py(Math.min(vazaoDisp,vazMax));
    ctx.fillStyle='rgba(46,125,50,.07)';
    ctx.fillRect(mg.l,y0,cW,mg.t+cH-y0);
  }

  // Curva principal
  ctx.beginPath();
  const step=(lamMax-lamMin)/200;
  for(let l=lamMin;l<=lamMax;l+=step){
    const v=laminaParaVazao(l,area,turno);
    const x=px(l),y=py(Math.min(v,vazMax));
    l===lamMin?ctx.moveTo(x,y):ctx.lineTo(x,y);
  }
  ctx.strokeStyle='#2e7d32';ctx.lineWidth=2.5;ctx.stroke();

  // Linha de vazão disponível
  if(vazaoDisp>0&&vazaoDisp<=vazMax){
    const y=py(vazaoDisp);
    ctx.setLineDash([6,4]);ctx.strokeStyle='#0077b6';ctx.lineWidth=2;
    ctx.beginPath();ctx.moveTo(mg.l,y);ctx.lineTo(mg.l+cW,y);ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle='#0077b6';ctx.font='bold 11px Segoe UI';ctx.textAlign='left';
    ctx.fillText(`Vazão disponível: ${fmt(vazaoDisp)} m³/h`,mg.l+6,y-6);
    // Ponto de intersecção
    const lamDisp=vazaoParaLamina(vazaoDisp,turno,area);
    if(lamDisp>=lamMin&&lamDisp<=lamMax){
      const xi=px(lamDisp),yi=py(vazaoDisp);
      ctx.fillStyle='#0077b6';ctx.beginPath();ctx.arc(xi,yi,7,0,Math.PI*2);ctx.fill();
      ctx.fillStyle='#fff';ctx.beginPath();ctx.arc(xi,yi,3,0,Math.PI*2);ctx.fill();
      ctx.fillStyle='#003d5c';ctx.font='bold 11px Segoe UI';ctx.textAlign='center';
      ctx.fillText(`${fmt(lamDisp,2)} mm/dia`,xi,yi-12);
    }
  }

  // Linha de lâmina alvo
  if(laminaAlvo>0&&laminaAlvo>=lamMin&&laminaAlvo<=lamMax){
    const x=px(laminaAlvo);
    const vNecAlvo=laminaParaVazao(laminaAlvo,area,turno);
    ctx.setLineDash([4,4]);ctx.strokeStyle='#e65100';ctx.lineWidth=1.5;
    ctx.beginPath();ctx.moveTo(x,mg.t);ctx.lineTo(x,mg.t+cH);ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle='#e65100';ctx.font='bold 10px Segoe UI';ctx.textAlign='center';
    ctx.fillText(`Alvo: ${fmt(laminaAlvo,1)} mm`,x,mg.t-5);
    if(vNecAlvo<=vazMax){
      const yi=py(vNecAlvo);
      ctx.fillStyle='#e65100';ctx.beginPath();ctx.arc(x,yi,6,0,Math.PI*2);ctx.fill();
      ctx.fillStyle='#fff';ctx.font='bold 9px Segoe UI';ctx.textAlign='center';
      ctx.fillText(fmt(vNecAlvo,0),x,yi+3);
    }
  }

  // Título
  ctx.fillStyle='rgba(27,94,32,.07)';ctx.fillRect(0,0,W,36);
  ctx.fillStyle='#1b5e20';ctx.font='bold 13px Segoe UI';ctx.textAlign='center';
  ctx.fillText('CURVA DE DEMANDA HÍDRICA — LÂMINA × VAZÃO NECESSÁRIA',W/2,23);
  ctx.fillStyle='#2e7d32';ctx.font='10px Segoe UI';ctx.textAlign='right';
  ctx.fillText('João Paulo de Oliveira · Eng. Agrônomo · Bolsa Irriga®',W-9,H-8);
}

// ── RESET ─────────────────────────────────────────────────────────────
function resetForm(){
  ['consultor','cliente','propriedade','cidade','laminaAlvo'].forEach(id=>$(id).value='');
  $('area').value='';$('turno').value='';$('vazao').value='';
  $('efic').value=90;$('lamMin').value=0.5;
  $('data').value=new Date().toISOString().split('T')[0];
  calc();
}

// ── PDF ───────────────────────────────────────────────────────────────
function gerarPDF(){
  if(!gv('area')||!gv('turno')){alert('Preencha área e turno primeiro.');return;}
  requestAnimationFrame(()=>{
    const img=$('c-graf').toDataURL('image/png');
    _popup(img);
  });
}
function _popup(img){
  const area=gv('area'),turno=gv('turno'),vazaoDisp=gv('vazao');
  const laminaAlvo=gv('laminaAlvo'),efic=gv('efic')||90;
  const cons=$('consultor').value||'—',cli=$('cliente').value||'—';
  const prop=$('propriedade').value||'—',cid=$('cidade').value||'—';
  const dt=$('data').value?new Date($('data').value+'T12:00:00').toLocaleDateString('pt-BR'):'—';

  const lamDisp=vazaoDisp>0?vazaoParaLamina(vazaoDisp,turno,area):null;
  const vazNecAlvo=laminaAlvo>0?laminaParaVazao(laminaAlvo,area,turno):null;
  const volCiclo=lamDisp?volTotal(lamDisp,area):null;

  // Tabela PDF
  let tblRows='';
  _tableData.forEach((d,i)=>{
    const bg=d.isAvail?'#e8f5e9':d.isTgt?'#e3f2fd':i%2===0?'#f9fdf9':'#fff';
    const fw=d.isAvail||d.isTgt?'800':'400';
    tblRows+=`<tr style="background:${bg};font-weight:${fw}">
      <td style="text-align:left;padding-left:8px">${fmt(d.lam,1)} mm/dia</td>
      <td style="text-align:center">${fmt(d.volHa,1)} m³/ha</td>
      <td style="text-align:center">${fmt(d.vol)} m³</td>
      <td style="text-align:center;font-weight:700;color:${d.ok?'#1b5e20':'#c62828'}">${fmt(d.vNec)} m³/h</td>
      <td style="text-align:center">${d.isAvail?'◀ Disponível':d.isTgt?'◀ Alvo':d.ok?'✓':'✗'}</td>
    </tr>`;
  });

  const css=`*{box-sizing:border-box;margin:0;padding:0;font-family:'Segoe UI',sans-serif}
body{font-size:10pt;color:#1a2535;background:#fff}
.pg{padding:8mm 12mm;page-break-after:always;min-height:280mm}.pg:last-child{page-break-after:avoid}
.hd{background:linear-gradient(135deg,#1b5e20,#2e7d32,#388e3c);color:#fff;padding:6px 12px;display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;border-radius:4px}
.hl{display:flex;align-items:center;gap:8px}.hl img{height:40px;width:40px;background:#fff;border-radius:6px;padding:3px;object-fit:contain}
.hb h2{font-size:.95rem;font-weight:800}.hb p{font-size:.65rem;opacity:.85}
.hr2{text-align:right;font-size:.65rem;line-height:1.6}.hr2 b{font-size:.78rem;display:block}
.cli{background:#e8f5e9;border:1px solid #c8e6c9;border-radius:4px;padding:5px 10px;display:grid;grid-template-columns:repeat(5,1fr);gap:4px;margin-bottom:6px;font-size:.76rem}
.cf label{font-size:.6rem;font-weight:800;color:#607080;text-transform:uppercase;display:block}
.cf span{font-weight:700;color:#1b5e20}
.st{font-size:.72rem;font-weight:900;color:#2e7d32;text-transform:uppercase;letter-spacing:.06em;padding:3px 0 4px;border-bottom:1.5px solid #c8e6c9;margin:6px 0 4px;display:flex;align-items:center;gap:4px}
.st::before{content:'';width:3px;height:1em;background:#388e3c;border-radius:2px;flex-shrink:0}
.params{display:grid;grid-template-columns:repeat(5,1fr);gap:4px;margin-bottom:6px}
.kv{border-radius:5px;padding:4px 6px;background:#f1faf2;border:1px solid #c8e6c9}
.kv label{font-size:.58rem;font-weight:800;color:#607080;text-transform:uppercase;display:block}
.kv strong{font-size:.9rem;color:#1b5e20}
.res-big{text-align:center;padding:6px;border-radius:6px;margin-bottom:5px}
.g3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:5px;margin-bottom:6px}
.box{border-radius:5px;padding:4px 7px}
.tbl{width:100%;border-collapse:collapse;font-size:.79rem}
.tbl th{padding:4px 6px;font-size:.66rem;font-weight:800;text-transform:uppercase;text-align:center;background:#e8f5e9;border:1px solid #c8e6c9;color:#2e7d32}
.tbl th.l{text-align:left}
.tbl td{padding:3px 6px;border:1px solid #e8f0ea}
.img-box{border:1.5px solid #c8e6c9;border-radius:5px;overflow:hidden;margin-top:4px}
.img-box img{width:100%;display:block}
.ft{border-top:1px solid #d0e4f0;padding-top:4px;margin-top:6px;display:flex;justify-content:space-between;font-size:.62rem;color:#607080}
.ft img{height:18px;width:18px;object-fit:contain;border-radius:3px;background:#f0f7ff;padding:2px;border:1px solid #d0e4f0;vertical-align:middle;margin-right:3px}
@media print{*{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}body{margin:0}.pg{padding:5mm 8mm}}`;

  const hdr=`<div class="hd"><div class="hl"><img src="data:image/png;base64,${LOGO}" alt=""><div class="hb"><h2>Bolsa Irriga&#174; &mdash; L&#226;mina de Irriga&#231;&#227;o &times; Vaz&#227;o</h2><p>Dimensionamento de L&#226;mina &middot; Turno &middot; &#193;rea &middot; C&#225;lculo Bidirecional</p></div></div><div class="hr2"><b>Jo&#227;o Paulo de Oliveira</b>Eng. Agr&#244;nomo &middot; Esp. Irriga&#231;&#227;o<br>bolsairriga.com.br &middot; (16) 3702-6571</div></div>`;
  const cliHtml=`<div class="cli"><div class="cf"><label>Consultor</label><span>${cons}</span></div><div class="cf"><label>Cliente</label><span>${cli}</span></div><div class="cf"><label>Propriedade</label><span>${prop}</span></div><div class="cf"><label>Cidade/UF</label><span>${cid}</span></div><div class="cf"><label>Data</label><span>${dt}</span></div></div>`;
  const foot=`<div class="ft"><div><img src="data:image/png;base64,${LOGO}" alt=""> Bolsa Irriga&#174; &middot; Av. Elias Abr&#227;o, 140 &middot; Franca &ndash; SP</div><div>Jo&#227;o Paulo de Oliveira &middot; Eng. Agr&#244;nomo</div></div>`;

  const pg1=`<div class="pg">${hdr}${cliHtml}
    <div class="st">Par&#226;metros do Sistema</div>
    <div class="params">
      <div class="kv"><label>&#193;rea Total</label><strong>${fmt(area)} ha</strong></div>
      <div class="kv"><label>Turno de Irriga&#231;&#227;o</label><strong>${fmt(turno,1)} h/dia</strong></div>
      <div class="kv"><label>Vaz&#227;o Dispon&#237;vel</label><strong>${vazaoDisp?fmt(vazaoDisp)+' m³/h':'—'}</strong></div>
      <div class="kv"><label>L&#226;mina Alvo</label><strong>${laminaAlvo?fmt(laminaAlvo,1)+' mm/dia':'—'}</strong></div>
      <div class="kv"><label>Efici&#234;ncia</label><strong>${efic}%</strong></div>
    </div>
    ${lamDisp?`<div class="g3">
      <div class="box" style="background:#e8f5e9;border:1.5px solid #2e7d32;text-align:center">
        <div style="font-size:.65rem;font-weight:800;color:#2e7d32;text-transform:uppercase">L&#226;mina Dispon&#237;vel</div>
        <div style="font-size:1.3rem;font-weight:900;color:#1b5e20">${fmt(lamDisp,2)} mm/dia</div>
        <div style="font-size:.72rem;color:#607080">l&#237;q.: ${fmt(lamDisp*efic/100,2)} mm/dia</div>
      </div>
      <div class="box" style="background:#f1faf2;border:1px solid #c8e6c9;text-align:center">
        <div style="font-size:.65rem;font-weight:800;color:#2e7d32;text-transform:uppercase">Vol. Total/ciclo</div>
        <div style="font-size:1.2rem;font-weight:900;color:#1b5e20">${fmt(volCiclo)} m³</div>
        <div style="font-size:.72rem;color:#607080">${fmt(lamDisp*10)} m³/ha</div>
      </div>
      <div class="box" style="background:${vazNecAlvo&&vazaoDisp>=vazNecAlvo?'#e8f5e9':'#ffebee'};border:1.5px solid ${vazNecAlvo&&vazaoDisp>=vazNecAlvo?'#2e7d32':'#ef5350'};text-align:center">
        <div style="font-size:.65rem;font-weight:800;color:${vazNecAlvo&&vazaoDisp>=vazNecAlvo?'#2e7d32':'#c62828'};text-transform:uppercase">Vaz&#227;o p/ Alvo</div>
        <div style="font-size:1.2rem;font-weight:900;color:${vazNecAlvo&&vazaoDisp>=vazNecAlvo?'#1b5e20':'#c62828'}">${vazNecAlvo?fmt(vazNecAlvo)+' m³/h':'—'}</div>
        <div style="font-size:.72rem;color:#607080">${vazNecAlvo&&vazaoDisp>0?(vazaoDisp>=vazNecAlvo?'✓ Suficiente':'✗ Insuficiente'):'—'}</div>
      </div>
    </div>`:''}
    <div class="st">Gr&#225;fico — Curva de Demanda H&#237;drica</div>
    <div class="img-box"><img src="${img}" alt="Curva Lâmina x Vazão"></div>
    ${foot}</div>`;

  const pg2=`<div class="pg">${hdr}${cliHtml}
    <div class="st">Tabela de L&#226;mina de Irriga&#231;&#227;o — L&#226;mina &times; Vaz&#227;o Necess&#225;ria</div>
    <p style="font-size:.72rem;color:#607080;margin-bottom:5px">&#193;rea: <strong>${fmt(area)} ha</strong> &nbsp;|&nbsp; Turno: <strong>${fmt(turno,1)} h/dia</strong> &nbsp;|&nbsp; Vaz&#227;o dispon&#237;vel: <strong>${vazaoDisp?fmt(vazaoDisp)+' m³/h':'—'}</strong></p>
    <table class="tbl">
      <thead><tr>
        <th class="l">L&#226;mina (mm/dia)</th>
        <th>Vol. bruto/ha (m&#179;)</th>
        <th>Vol. total (m&#179;)</th>
        <th>Vaz&#227;o necess&#225;ria (m&#179;/h)</th>
        <th>Status</th>
      </tr></thead>
      <tbody>${tblRows}</tbody>
    </table>
    ${foot}</div>`;

  const fullHtml=`<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"><title>L&#226;mina &times; Vaz&#227;o &mdash; Bolsa Irriga</title><style>${css}</style></head><body>${pg1}${pg2}<script>window.addEventListener('load',()=>setTimeout(()=>window.print(),800));<\/script></body></html>`;
  const blob=new Blob([fullHtml],{type:'text/html;charset=utf-8'});
  const url=URL.createObjectURL(blob);
  const win=window.open(url,'_blank');
  if(!win)alert('Permita popups e tente novamente.');
  setTimeout(()=>URL.revokeObjectURL(url),120000);
}


</script>
</body>
</html>"""

HTML = HTML.replace('##LOGO##', LOGO)
with open('lamina.html','w',encoding='utf-8') as f:
    f.write(HTML)
print(f'OK — {len(HTML):,} bytes')
