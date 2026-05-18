import base64, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('logo perfil branca.png','rb') as f:
    LOGO = base64.b64encode(f.read()).decode()

HTML = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Cabos Elétricos — Bolsa Irriga</title>
<style>
:root{
  --bl:#003d5c;--bl2:#0077b6;--bl3:#00b4d8;--bl4:#e3f2fd;
  --am:#e07b00;--am2:#fff8e1;--am3:#ffe0b2;
  --gn:#1b6e3a;--gn2:#2d9e5a;--gn3:#d4edda;
  --rd:#c62828;--rd2:#ffebee;
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

/* painel */
.panel{background:#fff;border-radius:16px;padding:1.6rem 2rem;max-width:640px;width:100%;box-shadow:0 8px 32px rgba(0,0,0,.2);margin-bottom:1.4rem}
.panel h2{font-size:1rem;font-weight:800;color:#003d5c;margin-bottom:1rem}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:.8rem}
.g3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:.8rem}
@media(max-width:500px){.g2,.g3{grid-template-columns:1fr}}
.field{display:flex;flex-direction:column;gap:.3rem}
.field label{font-size:.72rem;font-weight:700;color:#607080;text-transform:uppercase;letter-spacing:.04em}
.field small{font-size:.67rem;color:#607080;margin-top:.05rem}
.iu{display:flex}
.iu input,.iu select{flex:1;border-radius:8px 0 0 8px!important}
.iu .u{background:#e3f2fd;border:1.5px solid #b0cce8;border-left:none;padding:.48rem .6rem;font-size:.78rem;color:#607080;border-radius:0 8px 8px 0;white-space:nowrap;display:flex;align-items:center}
input[type=number],input[type=text],input[type=date],select{padding:.48rem .68rem;border:1.5px solid #b0cce8;border-radius:8px;font-size:.9rem;color:#1a2535;background:#fafeff;outline:none;transition:border-color .18s;width:100%}
input:focus,select:focus{border-color:#0077b6;box-shadow:0 0 0 3px rgba(0,119,182,.12)}
.seg{display:flex;gap:.5rem;flex-wrap:wrap}
.seg button{flex:1;padding:.5rem .8rem;border:2px solid #b0cce8;border-radius:8px;font-size:.85rem;font-weight:700;cursor:pointer;background:#fff;color:#607080;transition:all .15s;white-space:nowrap}
.seg button.active{background:#0077b6;border-color:#0077b6;color:#fff}
.btn-calc{width:100%;background:#0077b6;color:#fff;border:none;border-radius:10px;padding:.75rem;font-size:1rem;font-weight:800;cursor:pointer;transition:background .15s;margin-top:.5rem}
.btn-calc:hover{background:#005f94}

/* resultados */
.results{max-width:640px;width:100%;margin-bottom:1.4rem}
.res-card{background:#fff;border-radius:14px;padding:1.4rem 1.6rem;box-shadow:0 6px 24px rgba(0,0,0,.15);margin-bottom:1rem}
.res-card h3{font-size:.8rem;font-weight:800;color:#003d5c;text-transform:uppercase;letter-spacing:.06em;margin-bottom:.9rem;padding-bottom:.5rem;border-bottom:2px solid #e3f2fd;display:flex;align-items:center;gap:.4rem}
.res-card h3::before{content:'';width:4px;height:1.1em;background:#0077b6;border-radius:2px;flex-shrink:0}
.kv-grid{display:grid;grid-template-columns:1fr 1fr;gap:.7rem}
@media(max-width:400px){.kv-grid{grid-template-columns:1fr}}
.kv{border-radius:8px;padding:.65rem .8rem}
.kv.cu{background:linear-gradient(135deg,#e8f4fd,#d0eaf8);border:1px solid #a8d4f0}
.kv.al{background:linear-gradient(135deg,#f3f3f3,#e8e8e8);border:1px solid #c0c0c0}
.kv.warn{background:linear-gradient(135deg,#fff8e1,#ffe0b2);border:1px solid #ffcc80}
.kv.ok{background:linear-gradient(135deg,#e8f5e9,#c8e6c9);border:1px solid #a5d6a7}
.kv.info{background:linear-gradient(135deg,#e8f4fd,#d0eaf8);border:1px solid #a8d4f0}
.kv label{font-size:.62rem;font-weight:800;color:#607080;text-transform:uppercase;letter-spacing:.05em;display:block;margin-bottom:.15rem}
.kv .val{font-size:1.25rem;font-weight:900;color:#003d5c;line-height:1.1}
.kv .val.lg{font-size:1.5rem}
.kv .val small{font-size:.7rem;font-weight:500;color:#607080;margin-left:.2rem}
.kv .sub-val{font-size:.72rem;color:#607080;margin-top:.1rem}
.kv .sub-val.red{color:#c62828}
.kv .sub-val.green{color:#1b6e3a}
.kv .sub-val.amber{color:#e07b00}
.badge{display:inline-block;padding:.15rem .55rem;border-radius:10px;font-size:.7rem;font-weight:800}
.badge-ok{background:#e8f5e9;color:#1b6e3a;border:1px solid #a5d6a7}
.badge-warn{background:#fff8e1;color:#e07b00;border:1px solid #ffcc80}
.badge-err{background:#ffebee;color:#c62828;border:1px solid #ef9a9a}
.note{font-size:.77rem;color:#607080;background:#f4f7fb;border-radius:8px;padding:.7rem .9rem;border-left:3px solid #b0cce8;margin-top:.8rem;line-height:1.5}
.hidden{display:none!important}
.btn-pdf{background:#fff;color:#0077b6;border:2px solid #0077b6;border-radius:10px;padding:.65rem 1.8rem;font-size:.9rem;font-weight:800;cursor:pointer;transition:background .15s,color .15s;margin-bottom:2rem}
.btn-pdf:hover{background:#0077b6;color:#fff}
.footer{color:rgba(255,255,255,.5);font-size:.72rem;text-align:center;line-height:1.8;margin-top:auto;padding-top:1.5rem}

/* campos adicionais do projeto (para PDF) */
.proj-fields{display:grid;grid-template-columns:1fr 1fr;gap:.8rem;margin-bottom:1rem}
@media(max-width:500px){.proj-fields{grid-template-columns:1fr}}
</style>
</head>
<body>

<div class="logo-wrap">
  <img src="logo perfil branca.png" alt="Bolsa Irriga" onerror="this.style.display='none'">
</div>
<h1>Cabos El&eacute;tricos</h1>
<p class="sub">Sele&ccedil;&atilde;o de Cabo — Cobre e Alum&iacute;nio</p>
<p class="dev">Jo&atilde;o Paulo de Oliveira &middot; Engenheiro Agr&ocirc;nomo &middot; Especialista em Irriga&ccedil;&atilde;o</p>

<!-- Painel -->
<div class="panel">
  <h2>&#9889; Dados do Projeto</h2>
  <div class="proj-fields">
    <div class="field"><label>Consultor</label><input type="text" id="consultor" placeholder="Nome do consultor"></div>
    <div class="field"><label>Cliente</label><input type="text" id="cliente" placeholder="Nome do cliente"></div>
    <div class="field"><label>Propriedade</label><input type="text" id="propriedade" placeholder="Nome da propriedade"></div>
    <div class="field"><label>Cidade / UF</label><input type="text" id="cidade" placeholder="Ex.: Franca / SP"></div>
  </div>

  <h2 style="margin-bottom:.8rem">&#9881; Par&acirc;metros El&eacute;tricos</h2>

  <div class="field" style="margin-bottom:.8rem">
    <label>Sistema El&eacute;trico</label>
    <div class="seg">
      <button id="btn-mono" class="active" onclick="setFase('mono')">Monof&aacute;sico</button>
      <button id="btn-tri" onclick="setFase('tri')">Trif&aacute;sico</button>
    </div>
  </div>

  <div class="g2" style="margin-bottom:.8rem">
    <div class="field">
      <label>Tens&atilde;o</label>
      <select id="tensao" onchange="updateVoltOptions()">
        <option value="127">127 V</option>
        <option value="220" selected>220 V</option>
        <option value="380">380 V</option>
        <option value="440">440 V</option>
      </select>
    </div>
    <div class="field">
      <label>Tipo de Motor</label>
      <select id="tipoMotor">
        <option value="IP55">IP-55 (Fechado)</option>
        <option value="IP21">IP-21 (Aberto)</option>
        <option value="sub">Submerso</option>
      </select>
    </div>
  </div>

  <div class="g3" style="margin-bottom:.8rem">
    <div class="field">
      <label>Pot&ecirc;ncia da Bomba</label>
      <div class="iu">
        <input type="number" id="potencia" min="0.25" max="500" step="0.25" placeholder="0,0" oninput="calcular()">
        <span class="u">CV</span>
      </div>
    </div>
    <div class="field">
      <label>Dist&acirc;ncia</label>
      <div class="iu">
        <input type="number" id="distancia" min="1" max="2000" step="1" placeholder="0" oninput="calcular()">
        <span class="u">m</span>
      </div>
    </div>
    <div class="field">
      <label>Queda de Tens&atilde;o m&aacute;x.</label>
      <div class="iu">
        <input type="number" id="qdtensao" min="0.5" max="10" step="0.5" value="4" oninput="calcular()">
        <span class="u">%</span>
      </div>
      <small>Tabela Thebe: 4%</small>
    </div>
  </div>

  <div class="field" style="margin-bottom:1rem">
    <label>Data</label>
    <input type="date" id="data" style="max-width:200px">
  </div>

  <button class="btn-calc" onclick="calcular()">&#9889; Calcular Cabo</button>
</div>

<!-- Resultados -->
<div class="results hidden" id="results">

  <div class="res-card">
    <h3>Corrente do Motor</h3>
    <div class="kv-grid">
      <div class="kv info">
        <label>Corrente Nominal</label>
        <div class="val lg" id="r_iNom">—</div>
        <div class="sub-val" id="r_iNomNote">—</div>
      </div>
      <div class="kv info">
        <label>Pot&ecirc;ncia</label>
        <div class="val" id="r_pot">—</div>
        <div class="sub-val" id="r_potSub">—</div>
      </div>
    </div>
  </div>

  <div class="res-card">
    <h3>Cabo de Cobre</h3>
    <div class="kv-grid">
      <div class="kv cu">
        <label>Bitola &mdash; Queda de Tens&atilde;o</label>
        <div class="val lg" id="r_cuSec">—</div>
        <div class="sub-val" id="r_cuDrop">—</div>
      </div>
      <div class="kv cu">
        <label>Verifica&ccedil;&atilde;o de Ampacidade</label>
        <div class="val" id="r_cuAmp">—</div>
        <div class="sub-val" id="r_cuAmpNote">—</div>
      </div>
    </div>
    <div id="r_cuWarn" class="note hidden"></div>
  </div>

  <div class="res-card">
    <h3>Cabo de Alum&iacute;nio</h3>
    <div class="kv-grid">
      <div class="kv al">
        <label>Bitola &mdash; Queda de Tens&atilde;o</label>
        <div class="val lg" id="r_alSec">—</div>
        <div class="sub-val" id="r_alDrop">—</div>
      </div>
      <div class="kv al">
        <label>Verifica&ccedil;&atilde;o de Ampacidade</label>
        <div class="val" id="r_alAmp">—</div>
        <div class="sub-val" id="r_alAmpNote">—</div>
      </div>
    </div>
    <div id="r_alWarn" class="note hidden"></div>
  </div>

  <div class="res-card">
    <h3>Notas T&eacute;cnicas</h3>
    <div class="note" style="margin-top:0">
      &#9888; Tabela orientativa conforme ABNT NBR 5410. Temperatura do condutor m&aacute;x. 70&deg;C, temperatura ambiente 30&deg;C, instalado em eletroduto.<br>
      &#9888; Alum&iacute;nio: NBR 5410 n&atilde;o indica bitola abaixo de 16mm&sup2; — substituir por cobre nesses casos.<br>
      &#9888; <strong>A consulta a um profissional eletricista &eacute; obrigat&oacute;ria para a sele&ccedil;&atilde;o final dos cabos.</strong><br>
      Ref.: Tabela Thebe (ABNT NBR 5410) &middot; Cobre: Prysmian &middot; Alum&iacute;nio: Phelpsdodge
    </div>
  </div>

</div>

<button class="btn-pdf hidden" id="btnPdf" onclick="gerarPDF()">&#128438; Gerar Relat&oacute;rio PDF</button>

<div class="footer">
  Bolsa Irriga&reg; &mdash; Av. Elias Abr&atilde;o, n&ordm; 140 &middot; Franca &ndash; SP &middot; (16) 3702-6571 &middot; bolsairriga.com.br<br>
  &copy; 2025 Jo&atilde;o Paulo de Oliveira
</div>

<script>
const LOGO_B64 = '##LOGO##';

// ── Constantes ────────────────────────────────────────────────────────────────
const SIGMA_CU = 44;   // m/(Ω·mm²) a 70°C  (ABNT/SENAI)
const SIGMA_AL = 27;   // m/(Ω·mm²) a 70°C
const COS_PHI  = 0.85; // fator de potência típico motor indu
const ETA      = 0.88; // rendimento típico motor

// Bitolas comerciais (mm²)
const SECOES = [1.5,2.5,4,6,10,16,25,35,50,70,95,120,150,185,240,300,400,500];
const MIN_AL = 16; // NBR 5410: mínimo para alumínio

// Ampacidade (A) — eletroduto, temp amb 30°C, 3 condutores carregados (NBR 5410 Tabela 37)
const AMP_CU = {1.5:15,2.5:21,4:28,6:36,10:50,16:68,25:89,35:111,50:134,70:171,95:207,120:239,150:275,185:314,240:368,300:419,400:485,500:550};
const AMP_AL = {16:52,25:68,35:85,50:103,70:132,95:160,120:185,150:213,185:243,240:285,300:324,400:376,500:427};

let fase = 'mono';

function setFase(f){
  fase = f;
  document.getElementById('btn-mono').className = f==='mono'?'active':'';
  document.getElementById('btn-tri').className  = f==='tri' ?'active':'';
  updateVoltOptions();
  calcular();
}

function updateVoltOptions(){
  const v = document.getElementById('tensao');
  const cur = v.value;
  // Monofásico: 127, 220, 440 | Trifásico: 220, 380, 440
  const opts_mono = [{v:'127',l:'127 V'},{v:'220',l:'220 V'},{v:'440',l:'440 V'}];
  const opts_tri  = [{v:'220',l:'220 V'},{v:'380',l:'380 V'},{v:'440',l:'440 V'}];
  const opts = fase==='mono'?opts_mono:opts_tri;
  v.innerHTML = opts.map(o=>`<option value="${o.v}"${o.v===cur?' selected':''}>${o.l}</option>`).join('');
  calcular();
}

function nextSec(sMin, material){
  if(material==='al' && sMin < MIN_AL) sMin = MIN_AL;
  for(const s of SECOES) if(s>=sMin) return s;
  return null;
}

function fmt1(n){return isNaN(n)?'—':n.toFixed(1)}
function fmt2(n){return isNaN(n)?'—':n.toFixed(2)}

function calcular(){
  const P_cv = parseFloat(document.getElementById('potencia').value);
  const L    = parseFloat(document.getElementById('distancia').value);
  const dqt  = parseFloat(document.getElementById('qdtensao').value)||4;
  const V    = parseFloat(document.getElementById('tensao').value);

  const res   = document.getElementById('results');
  const btnPdf= document.getElementById('btnPdf');

  if(!P_cv||P_cv<=0||!L||L<=0){
    res.className='results hidden'; btnPdf.className='btn-pdf hidden'; return;
  }

  const P_w = P_cv * 735.5;  // CV → W
  const k   = fase==='tri' ? Math.sqrt(3) : 2;

  // Corrente nominal
  const I_nom = fase==='tri'
    ? P_w / (Math.sqrt(3) * V * COS_PHI * ETA)
    : P_w / (V * COS_PHI * ETA);

  // Seção mínima por queda de tensão
  // S = (k × P × L) / (V² × (ΔU/100) × σ)
  const duFrac = dqt / 100;
  const sDenCu = V * V * duFrac * SIGMA_CU;
  const sDenAl = V * V * duFrac * SIGMA_AL;
  const sMinCu_qdt = (k * P_w * L) / sDenCu;
  const sMinAl_qdt = (k * P_w * L) / sDenAl;

  // Seção mínima por ampacidade (I_nom × 1.25)
  const I_prot = I_nom * 1.25;
  let sMinCu_amp = null, sMinAl_amp = null;
  for(const s of SECOES){ if((AMP_CU[s]||0) >= I_prot){ sMinCu_amp = s; break; } }
  for(const s of SECOES){ if(s>=MIN_AL && (AMP_AL[s]||0) >= I_prot){ sMinAl_amp = s; break; } }

  // Maior entre queda de tensão e ampacidade
  const sCalcCu = Math.max(sMinCu_qdt, sMinCu_amp||0);
  const sCalcAl = Math.max(sMinAl_qdt, sMinAl_amp||MIN_AL);

  const secCu = nextSec(sCalcCu,'cu');
  const secAl = nextSec(sCalcAl,'al');

  // Queda de tensão real no cabo escolhido
  // ΔU% = (k × P × L) / (V² × S × σ) × 100
  const dropCu = secCu ? (k * P_w * L) / (V * V * secCu * SIGMA_CU) * 100 : null;
  const dropAl = secAl ? (k * P_w * L) / (V * V * secAl * SIGMA_AL) * 100 : null;

  // Preencher resultados — Corrente
  document.getElementById('r_iNom').textContent    = fmt1(I_nom) + ' A';
  document.getElementById('r_iNomNote').textContent = `Proteção mín: ${fmt1(I_prot)} A`;
  document.getElementById('r_pot').textContent     = fmt1(P_cv) + ' CV';
  document.getElementById('r_potSub').textContent  = fmt1(P_w/1000) + ' kW  |  ' + (fase==='tri'?'Trifásico':'Monofásico') + '  |  ' + V + ' V';

  // Cobre
  const cuOk = secCu !== null;
  const cuAmpOk = cuOk && (AMP_CU[secCu]||0) >= I_prot;
  document.getElementById('r_cuSec').textContent  = cuOk ? secCu + ' mm²' : 'Fora da tabela';
  document.getElementById('r_cuDrop').textContent = cuOk ? 'Queda real: ' + fmt2(dropCu) + '%' : '';
  document.getElementById('r_cuAmp').textContent  = cuOk ? (AMP_CU[secCu]||'-') + ' A' : '—';
  const cuAmpNote = document.getElementById('r_cuAmpNote');
  if(cuOk){
    if(cuAmpOk){cuAmpNote.textContent='✓ Ampacidade OK';cuAmpNote.className='sub-val green';}
    else{cuAmpNote.textContent='⚠ Verificar ampacidade';cuAmpNote.className='sub-val amber';}
  } else cuAmpNote.textContent='';

  const cuWarn = document.getElementById('r_cuWarn');
  if(sMinCu_amp && sMinCu_amp > sMinCu_qdt){
    cuWarn.textContent='ℹ Cabo foi dimensionado pela ampacidade (capacidade de corrente), não pela queda de tensão.';
    cuWarn.className='note';
  } else cuWarn.className='note hidden';

  // Alumínio
  const alOk = secAl !== null;
  const alAmpOk = alOk && (AMP_AL[secAl]||0) >= I_prot;
  const alUsed16 = alOk && sMinAl_qdt < MIN_AL;
  document.getElementById('r_alSec').textContent  = alOk ? secAl + ' mm²' : 'Fora da tabela';
  document.getElementById('r_alDrop').textContent = alOk ? 'Queda real: ' + fmt2(dropAl) + '%' : '';
  document.getElementById('r_alAmp').textContent  = alOk ? (AMP_AL[secAl]||'-') + ' A' : '—';
  const alAmpNote = document.getElementById('r_alAmpNote');
  if(alOk){
    if(alAmpOk){alAmpNote.textContent='✓ Ampacidade OK';alAmpNote.className='sub-val green';}
    else{alAmpNote.textContent='⚠ Verificar ampacidade';alAmpNote.className='sub-val amber';}
  } else alAmpNote.textContent='';

  const alWarn = document.getElementById('r_alWarn');
  if(alUsed16){
    alWarn.textContent='ℹ NBR 5410: bitola mínima para alumínio é 16mm². Bitola adotada: 16mm². Considere usar cobre para bitolas menores.';
    alWarn.className='note';
  } else if(sMinAl_amp && sMinAl_amp > sMinAl_qdt){
    alWarn.textContent='ℹ Cabo foi dimensionado pela ampacidade (capacidade de corrente), não pela queda de tensão.';
    alWarn.className='note';
  } else alWarn.className='note hidden';

  // Salvar estado para PDF
  window._lastCalc = {P_cv,P_w,L,dqt,V,fase,I_nom,I_prot,
    secCu,dropCu,ampCu:AMP_CU[secCu],
    secAl,dropAl,ampAl:AMP_AL[secAl],
    sMinCu_qdt,sMinAl_qdt,sMinCu_amp,sMinAl_amp,cuAmpOk,alAmpOk,alUsed16};

  res.className='results';
  btnPdf.className='btn-pdf';
}

function gerarPDF(){
  const d = window._lastCalc;
  if(!d) return;
  const cons=document.getElementById('consultor').value.trim();
  const cli =document.getElementById('cliente').value.trim();
  const prop=document.getElementById('propriedade').value.trim();
  const cid =document.getElementById('cidade').value.trim();
  const dtRaw=document.getElementById('data').value;
  const dt=dtRaw?new Date(dtRaw+'T12:00:00').toLocaleDateString('pt-BR'):'—';

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
.g2{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:8px}
.g4{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin-bottom:8px}
.kv{border-radius:5px;padding:5px 8px}
.kv-bl{background:#e3f2fd;border:1px solid #b0cce8}
.kv-cu{background:linear-gradient(135deg,#e8f4fd,#d0eaf8);border:1px solid #a8d4f0}
.kv-al{background:linear-gradient(135deg,#f3f3f3,#e8e8e8);border:1px solid #c0c0c0}
.kv-ok{background:#e8f5e9;border:1px solid #a5d6a7}
.kv-am{background:#fff8e1;border:1px solid #ffcc80}
.kv label{font-size:.6rem;font-weight:800;color:#607080;text-transform:uppercase;display:block;margin-bottom:.1rem}
.kv .v{font-size:1.1rem;font-weight:900;color:#003d5c}
.kv .v.lg{font-size:1.35rem}
.kv .s{font-size:.68rem;color:#607080;margin-top:.08rem}
.kv .s.g{color:#1b6e3a}.kv .s.r{color:#c62828}.kv .s.am{color:#e07b00}
.note{font-size:.68rem;color:#607080;background:#f4f7fb;border-radius:4px;padding:.5rem .7rem;border-left:3px solid #b0cce8;margin-top:6px;line-height:1.5}
.ft{border-top:1px solid #d0e4f0;padding-top:4px;margin-top:8px;display:flex;justify-content:space-between;font-size:.62rem;color:#607080}
.ft img{height:18px;width:18px;object-fit:contain;border-radius:3px;background:#f0f7ff;padding:2px;border:1px solid #d0e4f0;vertical-align:middle;margin-right:3px}
@media print{*{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}body{margin:0}.pg{padding:5mm 9mm}}`;

  const hdr=`<div class="hd"><div class="hl"><img src="data:image/png;base64,${LOGO_B64}" alt=""><div class="hb"><h2>Bolsa Irriga&#174; &#8212; Sele&#231;&#227;o de Cabos El&#233;tricos</h2><p>Cobre e Alum&#237;nio &#183; ABNT NBR 5410 &#183; Queda de Tens&#227;o e Ampacidade</p></div></div><div class="hr2"><b>Jo&#227;o Paulo de Oliveira</b>Eng. Agr&#244;nomo &#183; Esp. Irriga&#231;&#227;o<br>bolsairriga.com.br &#183; (16) 3702-6571</div></div>`;
  const cliHtml=`<div class="cli"><div class="cf"><label>Consultor</label><span>${cons||'&#8212;'}</span></div><div class="cf"><label>Cliente</label><span>${cli||'&#8212;'}</span></div><div class="cf"><label>Propriedade</label><span>${prop||'&#8212;'}</span></div><div class="cf"><label>Cidade/UF</label><span>${cid||'&#8212;'}</span></div><div class="cf"><label>Data</label><span>${dt}</span></div></div>`;
  const foot=`<div class="ft"><div><img src="data:image/png;base64,${LOGO_B64}" alt=""> Bolsa Irriga&#174; &#183; Av. Elias Abr&#227;o, 140 &#183; Franca &#8211; SP</div><div>Jo&#227;o Paulo de Oliveira &#183; Eng. Agr&#244;nomo</div></div>`;

  const sistLabel = d.fase==='tri'?'Trif&#225;sico':'Monof&#225;sico';
  const cuAmpIcon = d.cuAmpOk?'&#10003;':'&#9888;';
  const alAmpIcon = d.alAmpOk?'&#10003;':'&#9888;';
  const cuAmpCls  = d.cuAmpOk?'g':'am';
  const alAmpCls  = d.alAmpOk?'g':'am';

  const alNote = d.alUsed16
    ? '<div class="note">&#9888; NBR 5410: bitola m&#237;nima para alum&#237;nio &#233; 16mm&#178;. Bitola adotada por norma.</div>'
    : '';

  const pg1=`<div class="pg">${hdr}${cliHtml}
  <div class="st">Par&#226;metros do Sistema</div>
  <div class="g4">
    <div class="kv kv-bl"><label>Pot&#234;ncia</label><div class="v">${d.P_cv.toFixed(2)} CV</div><div class="s">${(d.P_w/1000).toFixed(2)} kW</div></div>
    <div class="kv kv-bl"><label>Sistema</label><div class="v">${sistLabel}</div><div class="s">${d.V} V</div></div>
    <div class="kv kv-bl"><label>Dist&#226;ncia</label><div class="v">${d.L} m</div><div class="s">Motor ao quadro</div></div>
    <div class="kv kv-bl"><label>Queda m&#225;x.</label><div class="v">${d.dqt}%</div><div class="s">Tens&#227;o adm.</div></div>
  </div>
  <div class="g2">
    <div class="kv kv-bl"><label>Corrente Nominal (FP=0,85 / &#951;=0,88)</label><div class="v lg">${d.I_nom.toFixed(1)} A</div><div class="s">Prote&#231;&#227;o m&#237;n.: ${d.I_prot.toFixed(1)} A</div></div>
    <div class="kv kv-bl"><label>Secc. m&#237;n. por Queda de Tens&#227;o</label><div class="v">${d.sMinCu_qdt.toFixed(2)} mm&#178; (Cu) / ${d.sMinAl_qdt.toFixed(2)} mm&#178; (Al)</div><div class="s">Calculada pela f&#243;rmula ABNT NBR 5410</div></div>
  </div>

  <div class="st">Cabo de Cobre (Cu)</div>
  <div class="g4">
    <div class="kv kv-cu"><label>Bitola Adotada</label><div class="v lg">${d.secCu||'—'} mm&#178;</div></div>
    <div class="kv kv-cu"><label>Queda Real</label><div class="v">${d.dropCu?d.dropCu.toFixed(2)+'%':'—'}</div><div class="s ${d.dropCu&&d.dropCu<=d.dqt?'g':'r'}">${d.dropCu&&d.dropCu<=d.dqt?'&#10003; OK':'&#9888; Verificar'}</div></div>
    <div class="kv kv-cu"><label>Ampacidade</label><div class="v">${d.ampCu||'—'} A</div><div class="s ${cuAmpCls}">${cuAmpIcon} ${d.cuAmpOk?'OK':'Verificar'}</div></div>
    <div class="kv kv-cu"><label>Condutividade Cu</label><div class="v">44 m/&#937;&#183;mm&#178;</div><div class="s">A 70&#176;C (ABNT)</div></div>
  </div>

  <div class="st">Cabo de Alum&#237;nio (Al)</div>
  <div class="g4">
    <div class="kv kv-al"><label>Bitola Adotada</label><div class="v lg">${d.secAl||'—'} mm&#178;</div></div>
    <div class="kv kv-al"><label>Queda Real</label><div class="v">${d.dropAl?d.dropAl.toFixed(2)+'%':'—'}</div><div class="s ${d.dropAl&&d.dropAl<=d.dqt?'g':'r'}">${d.dropAl&&d.dropAl<=d.dqt?'&#10003; OK':'&#9888; Verificar'}</div></div>
    <div class="kv kv-al"><label>Ampacidade</label><div class="v">${d.ampAl||'—'} A</div><div class="s ${alAmpCls}">${alAmpIcon} ${d.alAmpOk?'OK':'Verificar'}</div></div>
    <div class="kv kv-al"><label>Condutividade Al</label><div class="v">27 m/&#937;&#183;mm&#178;</div><div class="s">A 70&#176;C (ABNT)</div></div>
  </div>
  ${alNote}
  <div class="note">
    &#9888; <strong>Tabela orientativa ABNT NBR 5410</strong>. Crit&#233;rios: eletroduto n&#227;o magn&#233;tico, temp. condutor 70&#176;C, temp. ambiente 30&#176;C, queda m&#225;x. ${d.dqt}%.<br>
    &#9888; Ampacidade baseada em 3 condutores carregados em eletroduto. Fatores de corre&#231;&#227;o (agrupamento, temperatura) devem ser aplicados pelo eletricista.<br>
    &#9888; <strong>A consulta a um profissional eletricista habilitado &#233; obrigat&#243;ria.</strong><br>
    F&#243;rmula: S = (k &#215; P &#215; L) / (V&#178; &#215; &#916;U% &#215; &#963;) &nbsp;|&nbsp; k = &#8730;3 (trifásico) ou 2 (monofásico).<br>
    Ref.: Thebe/SENAI/BRASFIO &#183; Cobre: Prysmian &#183; Alum&#237;nio: Phelpsdodge
  </div>
  ${foot}</div>`;

  const fullHtml=`<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"><title>Cabos El&#233;tricos &#8212; Bolsa Irriga</title><style>${css}</style></head><body>${pg1}<script>window.addEventListener('load',()=>setTimeout(()=>window.print(),800));<\/script></body></html>`;
  const blob=new Blob([fullHtml],{type:'text/html;charset=utf-8'});
  const url=URL.createObjectURL(blob);
  const win=window.open(url,'_blank');
  if(!win) alert('Permita popups e tente novamente.');
  setTimeout(()=>URL.revokeObjectURL(url),120000);
}

// init
document.getElementById('data').value = new Date().toISOString().split('T')[0];
</script>
</body>
</html>"""

HTML = HTML.replace('##LOGO##', LOGO)

with open('cabos.html','w',encoding='utf-8') as f:
    f.write(HTML)
print(f'OK - {len(HTML):,} bytes - cabos.html')
