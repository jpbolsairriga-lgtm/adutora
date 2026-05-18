import base64, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('logo perfil branca.png','rb') as f:
    LOGO = base64.b64encode(f.read()).decode()

HTML = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Adutora de Recalque — Bolsa Irriga</title>
<style>
:root{
  --bl:#005f8e;--bl2:#0077b6;--bl3:#00b4d8;--bl4:#caf0f8;
  --gn:#1b6e3a;--gn2:#2d9e5a;--gn3:#d4edda;
  --rd:#c62828;--am:#e07b00;--am2:#fff8e1;
  --bg:#f4f7fb;--bdr:#d0e4f0;--tx:#1a2535;--mu:#607080;
  --sh:0 2px 16px rgba(0,80,160,.10);
  --c180:#6a1b9a;--c145:#ad1457;--c125:#b71c1c;--c80:#e65100;--c60:#0d47a1;
}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--tx);font-size:14px}
header{background:linear-gradient(135deg,#003d5c,var(--bl2),var(--bl3));color:#fff;box-shadow:0 3px 20px rgba(0,0,0,.2)}
.hdr{max-width:1360px;margin:0 auto;padding:1rem 1.5rem;display:flex;justify-content:space-between;align-items:center;gap:1rem;flex-wrap:wrap}
.hdr-logo{display:flex;align-items:center;gap:1rem}
.hdr-logo img{height:70px;width:70px;object-fit:contain;background:#fff;border-radius:10px;padding:7px;box-shadow:0 2px 10px rgba(0,0,0,.18)}
.hdr-brand h1{font-size:1.45rem;font-weight:800;letter-spacing:-.3px}
.hdr-brand p{opacity:.85;font-size:.82rem;margin-top:.1rem}
.hdr-dev{text-align:right;font-size:.78rem;line-height:1.7;opacity:.92;border-left:2px solid rgba(255,255,255,.25);padding-left:1.2rem}
.hdr-dev .dn{font-size:.95rem;font-weight:800}
.hdr-co{font-size:.7rem;opacity:.75;margin-top:.15rem}
.page{max-width:1360px;margin:1.4rem auto;padding:0 1rem}
.card{background:#fff;border-radius:12px;padding:1.2rem 1.4rem;margin-bottom:1rem;box-shadow:var(--sh);border:1px solid var(--bdr)}
.ct{font-size:.76rem;font-weight:800;color:var(--bl2);text-transform:uppercase;letter-spacing:.08em;margin-bottom:.8rem;padding-bottom:.48rem;border-bottom:2px solid var(--bl4);display:flex;align-items:center;gap:.45rem}
.ct::before{content:'';width:4px;height:1.1em;background:var(--bl3);border-radius:2px;flex-shrink:0}
.sn{display:inline-flex;width:20px;height:20px;background:var(--bl2);color:#fff;border-radius:50%;align-items:center;justify-content:center;font-size:.72rem;font-weight:900;flex-shrink:0}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
.g3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:.8rem}
.g4{display:grid;grid-template-columns:repeat(4,1fr);gap:.7rem}
.g5{display:grid;grid-template-columns:repeat(5,1fr);gap:.7rem}
@media(max-width:960px){.g2{grid-template-columns:1fr}.g3{grid-template-columns:1fr 1fr}.g4,.g5{grid-template-columns:1fr 1fr}}
@media(max-width:560px){.g3,.g4,.g5{grid-template-columns:1fr}}
.fg{display:flex;flex-direction:column;gap:.2rem}
label{font-size:.72rem;font-weight:700;color:var(--mu);text-transform:uppercase;letter-spacing:.05em}
.fg small{font-size:.67rem;color:var(--mu);margin-top:.08rem}
.iu{display:flex}
.iu input,.iu select{flex:1;border-radius:8px 0 0 8px}
.iu .u{background:var(--bdr);border:1.5px solid var(--bdr);border-left:none;padding:.48rem .55rem;font-size:.77rem;color:var(--mu);border-radius:0 8px 8px 0;white-space:nowrap;display:flex;align-items:center}
input[type=number],input[type=text],input[type=date],select{padding:.48rem .68rem;border:1.5px solid var(--bdr);border-radius:8px;font-size:.9rem;color:var(--tx);background:#fafeff;outline:none;transition:border-color .18s,box-shadow .18s;width:100%}
input:focus,select:focus{border-color:var(--bl3);box-shadow:0 0 0 3px rgba(0,180,216,.13)}
.tile{border-radius:10px;padding:.75rem .9rem}
.tb2{background:linear-gradient(135deg,#e8f4fd,#d0eaf8);border:1px solid #a8d4f0}
.tg{background:linear-gradient(135deg,#e8f5e9,#c8e6c9);border:1px solid #a5d6a7}
.tt{background:linear-gradient(135deg,#e0f7fa,#b2ebf2);border:1px solid #80deea}
.to{background:linear-gradient(135deg,#fff3e0,#ffe0b2);border:1px solid #ffcc80}
.tl{font-size:.67rem;font-weight:800;color:#005f8e;text-transform:uppercase;letter-spacing:.06em;margin-bottom:.15rem}
.tv{font-size:1.15rem;font-weight:900;color:#003d5c;line-height:1.1}
.tv.lg{font-size:1.35rem}
.tv small{font-size:.7rem;font-weight:500;color:var(--mu);margin-left:.1rem}
.sbox{padding:.75rem 1rem;border-radius:8px;font-size:.84rem;line-height:1.5}
.sbox.warn{background:var(--am2);border-left:4px solid #f59e0b;color:#7c4d00}
.sbox.ok{background:var(--gn3);border-left:4px solid var(--gn2);color:#1b4d2e}
.sbox.info{background:#e3f2fd;border-left:4px solid #0077b6;color:#003d5c}
/* PN badges */
.pn-badge{display:inline-block;padding:.18rem .6rem;border-radius:12px;font-size:.78rem;font-weight:800;letter-spacing:.03em}
.pn180{background:#f3e5f5;color:#6a1b9a;border:1px solid #8e24aa}
.pn145{background:#fce4ec;color:#ad1457;border:1px solid #d81b60}
.pn125{background:#ffebee;color:#b71c1c;border:1px solid #e53935}
.pn80{background:#fff3e0;color:#e65100;border:1px solid #f57c00}
.pn60{background:#e3f2fd;color:#0d47a1;border:1px solid #1976d2}
/* motor badge */
.motor-badge{display:inline-block;padding:.28rem .9rem;border-radius:16px;font-size:1.05rem;font-weight:900;background:linear-gradient(135deg,#1b3a5e,#0077b6);color:#fff;letter-spacing:.03em;box-shadow:0 2px 8px rgba(0,80,160,.25)}
/* chave badge */
.chave-badge{display:inline-block;padding:.2rem .7rem;border-radius:10px;font-size:.76rem;font-weight:700;background:#e8f5e9;color:#1b5e20;border:1px solid #2d9e5a}
.chave-badge.et{background:#fff8e1;color:#7c4d00;border-color:#f59e0b}
.chave-badge.ss{background:#f3e5f5;color:#6a1b9a;border-color:#8e24aa}
/* seg bar */
.seg-bar{display:flex;height:38px;border-radius:8px;overflow:hidden;margin:.6rem 0;border:1px solid #cdd}
.seg-sec{display:flex;align-items:center;justify-content:center;font-size:.72rem;font-weight:800;color:#fff;text-shadow:0 1px 2px rgba(0,0,0,.4);min-width:36px;overflow:hidden;white-space:nowrap}
.ss180{background:var(--c180)}.ss145{background:var(--c145)}.ss125{background:var(--c125)}.ss80{background:var(--c80)}.ss60{background:var(--c60)}
/* tables */
.cmp-wrap{overflow-x:auto;margin-bottom:.6rem}
.cmp{width:100%;border-collapse:collapse;font-size:.83rem}
.cmp th{padding:.5rem .7rem;font-size:.7rem;font-weight:800;text-transform:uppercase;letter-spacing:.05em;text-align:center;border:1px solid var(--bdr)}
.cmp td{padding:.45rem .7rem;border:1px solid var(--bdr);text-align:center;vertical-align:middle}
.cmp td.lbl{text-align:left;font-weight:600;color:var(--mu);font-size:.81rem;background:#fafeff}
/* bomba cards */
.bomba-card{border-radius:10px;padding:.8rem 1rem;border:2px solid;margin-bottom:.6rem}
.bc-single{background:linear-gradient(135deg,#e8f5e9,#c8e6c9);border-color:#2d9e5a}
.bc-serie{background:linear-gradient(135deg,#e3f2fd,#bbdefb);border-color:#0077b6}
.bc-par{background:linear-gradient(135deg,#fff3e0,#ffe0b2);border-color:#f57c00}
.bc-title{font-size:.76rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em;margin-bottom:.5rem;color:#1a2535;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:.3rem}
.bc-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:.35rem .7rem}
.bc-item{font-size:.83rem}
.bc-item .lbl{font-size:.62rem;font-weight:700;color:var(--mu);text-transform:uppercase;display:block;margin-bottom:.08rem}
.bc-energy{border-top:1px solid rgba(0,0,0,.1);margin-top:.5rem;padding-top:.5rem;display:grid;grid-template-columns:repeat(auto-fit,minmax(110px,1fr));gap:.3rem .6rem;font-size:.82rem}
/* canvas */
.cf2{background:#fff;border-radius:10px;border:2px solid #b8d4f0;box-shadow:0 4px 20px rgba(0,80,160,.1);overflow:hidden}
.cl{background:var(--bl4);color:var(--bl2);font-size:.71rem;font-weight:800;text-transform:uppercase;letter-spacing:.07em;padding:.3rem .8rem;text-align:center;border-bottom:1px solid #b0cce8}
canvas{display:block;max-width:100%}
.btn{padding:.65rem 1.4rem;border:none;border-radius:8px;font-size:.88rem;font-weight:700;cursor:pointer;transition:all .18s;display:inline-flex;align-items:center;gap:.4rem}
.bpdf{background:linear-gradient(135deg,#b71c1c,#880e4f);color:#fff;padding:.72rem 1.8rem}
.bpdf:hover{transform:translateY(-1px);box-shadow:0 4px 16px rgba(183,28,28,.38)}
.bg{background:var(--bdr);color:var(--tx)}.bg:hover{background:#b8d8ee}
.abar{display:flex;justify-content:flex-end;gap:.75rem;padding:.3rem 0 .9rem;flex-wrap:wrap}
footer{background:#fff;border-top:2px solid var(--bdr);padding:1rem 1.5rem;margin-top:.5rem}
.fi{max-width:1360px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:.8rem}
.fd{display:flex;align-items:center;gap:.75rem}
.fd img{height:40px;width:40px;object-fit:contain;border-radius:7px;padding:3px;background:#f0f7ff;border:1px solid var(--bdr)}
.fdn .fn{font-weight:800;color:var(--bl2);font-size:.88rem}
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
        <h1>Adutora de Recalque</h1>
        <p>Multi-PN &middot; Hazen-Williams &middot; Motor Comercial &middot; Consumo Energ&#233;tico &middot; Tipo de Chave</p>
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
    <div class="ct"><span class="sn">1</span> Par&#226;metros Hidr&#225;ulicos</div>
    <div class="g2">
      <div class="fg"><label>Vaz&#227;o nominal (Q)</label>
        <div class="iu"><input type="number" id="Q" value="" min="0" step="1" oninput="calc()"><span class="u">m&#179;/h</span></div></div>
      <div class="fg"><label>Folga de Vaz&#227;o</label>
        <div class="iu"><input type="number" id="slackQ" value="" min="0" max="30" step="1" oninput="calc()"><span class="u">%</span></div>
        <small>Q c&#225;lculo = Q &times; (1 + folga%)</small></div>
      <div class="fg"><label>Comprimento total (L)</label>
        <div class="iu"><input type="number" id="L" value="" min="0" step="10" oninput="calc()"><span class="u">m</span></div></div>
      <div class="fg"><label>Cota de Suc&#231;&#227;o</label>
        <div class="iu"><input type="number" id="cotaS" value="" step="0.5" oninput="calc()"><span class="u">m</span></div></div>
      <div class="fg"><label>Cota de Recalque</label>
        <div class="iu"><input type="number" id="cotaR" value="" step="0.5" oninput="calc()"><span class="u">m</span></div></div>
      <div class="fg"><label>Efici&#234;ncia da Bomba</label>
        <div class="iu"><input type="number" id="eff" value="75" min="10" max="100" step="1" oninput="calc()"><span class="u">%</span></div></div>
      <div class="fg"><label>Perdas Localizadas</label>
        <div class="iu"><input type="number" id="kLoc" value="" min="0" max="50" step="1" oninput="calc()"><span class="u">%</span></div>
        <small>% sobre hf distribu&#237;da (curvas, registros...)</small></div>
      <div class="fg"><label>Perda no Filtro</label>
        <div class="iu"><input type="number" id="filtro" value="0" min="0" step="1" oninput="calc()"><span class="u">mca</span></div>
        <small>Perda fixa de carga no filtro (0 = sem filtro)</small></div>
      <div class="fg"><label>Press&#227;o Residual Final</label>
        <div class="iu"><input type="number" id="pRes" value="0" min="0" step="1" oninput="calc()"><span class="u">mca</span></div>
        <small>Press&#227;o m&#237;nima na entrega</small></div>
      <div class="fg"><label>Folga de Press&#227;o</label>
        <div class="iu"><input type="number" id="slackP" value="" min="0" max="30" step="1" oninput="calc()"><span class="u">%</span></div>
        <small>Margem sobre o AMT calculado</small></div>
    </div>
  </div>

  <div class="card">
    <div class="ct"><span class="sn">2</span> Crit&#233;rios de Sele&#231;&#227;o &amp; Energia</div>
    <div class="g2">
      <div class="fg"><label>Velocidade M&#225;xima Econ&#244;mica</label>
        <div class="iu"><input type="number" id="Vmax" value="1.5" min="0.3" max="3.0" step="0.1" oninput="calc()"><span class="u">m/s</span></div>
        <small>Planilha usa 1,1 m/s</small></div>
      <div class="fg"><label>Material da Tubula&#231;&#227;o</label>
        <select id="material" onchange="calc()">
          <option value="140">PVC / PEAD &mdash; C=140</option>
          <option value="130">Ferro Fundido &mdash; C=130</option>
          <option value="130s">A&#231;o &mdash; C=130</option>
          <option value="120">Concreto &mdash; C=120</option>
          <option value="110">Cimento-Amianto &mdash; C=110</option>
        </select></div>
      <div class="fg"><label>Horas de opera&#231;&#227;o / dia</label>
        <div class="iu"><input type="number" id="horasDia" value="8" min="1" max="24" step="0.5" oninput="calc()"><span class="u">h/dia</span></div></div>
      <div class="fg"><label>Tarifa de energia</label>
        <div class="iu"><input type="number" id="tarifa" value="0.80" min="0" step="0.01" oninput="calc()"><span class="u">R$/kWh</span></div></div>
    </div>
  </div>

  <div class="card">
    <div class="ct"><span class="sn">3</span> Limites de Press&#227;o por Classe PN</div>
    <p style="font-size:.76rem;color:var(--mu);margin-bottom:.7rem">Press&#227;o de trabalho m&#225;xima por classe (com fator de seguran&#231;a j&#225; inclu&#237;do).</p>
    <div class="g3">
      <div class="fg"><label><span class="pn-badge pn60">PN 60</span> &le;</label>
        <div class="iu"><input type="number" id="lim60" value="45" min="10" max="60" step="1" oninput="calc()"><span class="u">mca</span></div></div>
      <div class="fg"><label><span class="pn-badge pn80">PN 80</span> &le;</label>
        <div class="iu"><input type="number" id="lim80" value="65" min="45" max="80" step="1" oninput="calc()"><span class="u">mca</span></div></div>
      <div class="fg"><label><span class="pn-badge pn125">PN 125</span> &le;</label>
        <div class="iu"><input type="number" id="lim125" value="110" min="65" max="125" step="1" oninput="calc()"><span class="u">mca</span></div></div>
      <div class="fg"><label><span class="pn-badge pn145">PN 145</span> &le;</label>
        <div class="iu"><input type="number" id="lim145" value="130" min="110" max="145" step="1" oninput="calc()"><span class="u">mca</span></div></div>
      <div class="fg"><label><span class="pn-badge pn180">PN 180</span> &le;</label>
        <div class="iu"><input type="number" id="lim180" value="170" min="130" max="180" step="1" oninput="calc()"><span class="u">mca</span></div></div>
    </div>
  </div>
</div>

<!-- RIGHT: RESULTS -->
<div>
  <div class="card">
    <div class="ct">Resultados Hidr&#225;ulicos</div>
    <div id="quick-results"><div class="sbox warn">Preencha Q, L, cotaS e cotaR para calcular.</div></div>
  </div>
  <div class="card">
    <div class="ct">Motor Comercial &amp; Consumo Energ&#233;tico</div>
    <div id="bomba-results"><div class="sbox warn">Preencha os dados para calcular.</div></div>
  </div>
</div>

</div><!-- /g2 -->

<!-- DIÂMETRO SELECIONADO -->
<div class="card" id="card-diam" style="display:none">
  <div class="ct"><span class="sn">D</span> Di&#226;metro Selecionado &mdash; Mesmo Nominal nos Trechos Utilizados</div>
  <div id="diam-content"></div>
</div>

<!-- ANÁLISE MULTI-PN -->
<div class="card" id="card-multi" style="display:none">
  <div class="ct"><span class="sn">M</span> An&#225;lise Multi-PN &mdash; Segmenta&#231;&#227;o por Press&#227;o ao Longo da Adutora</div>
  <div id="multi-content"></div>
</div>

<!-- PERFIL DE PRESSÃO -->
<div class="card">
  <div class="ct">Perfil de Press&#227;o &mdash; Adutora de Recalque</div>
  <div class="cl">PRESS&#195;O DISPON&#205;VEL (mca) AO LONGO DA ADUTORA &middot; SEGMENTA&#199;&#195;O MULTI-PN</div>
  <div class="cf2"><canvas id="c-perfil" width="1280" height="420"></canvas></div>
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
    <div class="fc">Bolsa Irriga&#174; &mdash; Adutora de Recalque v6.0<br>
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

// ── BANCO DE DADOS ──────────────────────────────────────────────────
const PIPES=[
  ['75/60',75,1.8,71.4,60],['100/60',100,2.8,96.0,60],['118/60',118,2.7,112.6,60],['125/60',125,3.4,118.2,60],
  ['150/60',150,4.0,142.0,60],['170/60',170,3.9,162.2,60],['222/60',222,5.0,212.0,60],['274/60',274,6.2,261.6,60],
  ['326/60',326,7.4,311.2,60],['378/60',378,8.6,360.8,60],['429/60',429,9.8,409.4,60],['532/60',532,12.1,507.8,60],
  ['50,5/80',50.5,1.9,46.7,80],['75/80',75,2.3,70.4,80],['100/80',100,5.6,94.4,80],['101,6/80',101.6,3.6,94.4,80],
  ['118/80',118,3.1,111.8,80],['125/80',125,4.2,116.6,80],['150/80',150,5.0,140.0,80],['170/80',170,4.4,161.2,80],
  ['222/80',222,5.8,210.4,80],['274/80',274,7.1,259.8,80],['326/80',326,8.5,309.0,80],['378/80',378,9.9,358.2,80],
  ['429/80',429,11.2,406.6,80],['532/80',532,13.9,504.2,80],
  ['75/125',75,7.18,67.82,125],['118/125',118,4.8,108.4,125],['170/125',170,6.8,156.4,125],
  ['222/125',222,8.9,204.2,125],['274/125',274,11.0,252.0,125],['326/125',326,13.0,300.0,125],
  ['378/125',378,15.2,347.6,125],['429/125',429,17.2,394.6,125],['532/125',532,21.3,489.4,125],
  ['118/145',118,2.9,112.2,145],['170/145',170,4.15,161.7,145],['222/145',222,5.4,211.2,145],
  ['118/180',118,3.95,110.1,180],['170/180',170,5.6,158.8,180],['222/180',222,7.35,207.3,180],
];
const PN_CLASSES=[180,145,125,80,60];
const PN_COLOR={180:'#6a1b9a',145:'#ad1457',125:'#b71c1c',80:'#e65100',60:'#0d47a1'};
const PN_BG={180:'rgba(106,27,154,.13)',145:'rgba(173,20,87,.11)',125:'rgba(183,28,28,.12)',80:'rgba(230,81,0,.11)',60:'rgba(13,71,161,.10)'};
const PN_CSS={180:'pn180',145:'pn145',125:'pn125',80:'pn80',60:'pn60'};
const PN_SS={180:'ss180',145:'ss145',125:'ss125',80:'ss80',60:'ss60'};

// ── MOTORES E CHAVES ─────────────────────────────────────────────────
const MOTORES_CV=[1,2,3,5,7.5,10,12.5,15,20,25,30,40,50,60,75,100,125,150,175,200,250,300];
function nextMotorCV(cv){ return MOTORES_CV.find(m=>m>=cv)||MOTORES_CV[MOTORES_CV.length-1]; }
function tipoChave(cv){
  if(cv<=7.5) return{texto:'Partida Direta',cls:'chave-badge'};
  if(cv<=20)  return{texto:'Estrela-Tri&#226;ngulo (220V) / S&#233;rie-Paralelo (380V)',cls:'chave-badge et'};
  return       {texto:'Soft Start',cls:'chave-badge ss'};
}

// ── HIDRÁULICA ────────────────────────────────────────────────────────
function getCHW(){ return parseFloat($('material').value)||140; }
function hfPerMeter(Q_m3h,CHW,Dint_mm){
  if(!Q_m3h||!Dint_mm) return 0;
  const Qm3s=Q_m3h/3600,Dm=Dint_mm/1000;
  return 10.67*Math.pow(Qm3s,1.852)/(Math.pow(CHW,1.852)*Math.pow(Dm,4.87));
}
function velocity(Q_m3h,Dint_mm){
  const Qm3s=Q_m3h/3600,Dm=Dint_mm/1000;
  return Qm3s/(Math.PI*Dm*Dm/4);
}

// ── LIMITES PN ───────────────────────────────────────────────────────
function getLimits(){ return{60:gv('lim60')||45,80:gv('lim80')||65,125:gv('lim125')||110,145:gv('lim145')||130,180:gv('lim180')||170}; }
function pnForPressure(P,lim){
  if(P<=lim[60]) return 60;
  if(P<=lim[80]) return 80;
  if(P<=lim[125]) return 125;
  if(P<=lim[145]) return 145;
  return 180;
}

// ── SELEÇÃO DE TUBO ──────────────────────────────────────────────────
function autoSelect(Q_m3h,Vmax,pnClass,CHW){
  const cands=PIPES.filter(p=>p[4]===pnClass).sort((a,b)=>a[3]-b[3]);
  if(!cands.length) return null;
  for(const p of cands){ const V=velocity(Q_m3h,p[3]); if(V<=Vmax) return{pipe:p,V}; }
  const best=cands[cands.length-1]; return{pipe:best,V:velocity(Q_m3h,best[3]),overVmax:true};
}
function dIdeal_mm(Q,Vmax){ return Math.sqrt(4*(Q/3600)/(Math.PI*Vmax))*1000; }
function findBestNominal(Q,Vmax){
  const Di=dIdeal_mm(Q,Vmax);
  const pn125=PIPES.filter(p=>p[4]===125).sort((a,b)=>a[3]-b[3]);
  for(const p of pn125){ if(p[3]>=Di) return p[1]; }
  return pn125[pn125.length-1][1];
}
function getPipeByNominal(Dext,pnClass){
  const c=PIPES.filter(p=>p[4]===pnClass);
  return c.length?c.reduce((b,p)=>Math.abs(p[1]-Dext)<Math.abs(b[1]-Dext)?p:b):null;
}

// ── MULTI-PN ─────────────────────────────────────────────────────────
function calcMultiPN(Q_calc,L,Hg,CHW,nom,kLoc,filtro,pRes,slackP,lim){
  const pipeByPN={},jByPN={};
  for(const pn of PN_CLASSES){
    pipeByPN[pn]=getPipeByNominal(nom,pn);
    if(pipeByPN[pn]) jByPN[pn]=hfPerMeter(Q_calc,CHW,pipeByPN[pn][3])*(1+kLoc);
  }
  const ts=Hg/L, STEP=Math.max(1,Math.round(L/500));
  let AMT_hid=Hg+pRes+filtro+30,segs=[],totalHf=0;
  for(let iter=0;iter<20;iter++){
    const AMT_d=AMT_hid*(1+slackP);
    let x=0,P=AMT_d,s_=[];
    let sPN=pnForPressure(P,lim),sX=0,sP=P;
    while(x<L){
      const dx=Math.min(STEP,L-x),pn=pnForPressure(P,lim);
      if(pn!==sPN){s_.push({pn:sPN,from:sX,to:x,len:x-sX,P_start:sP,P_end:P});sX=x;sPN=pn;sP=P;}
      P-=(jByPN[pn]??jByPN[125]??jByPN[80]??jByPN[60])*dx+ts*dx;x+=dx;
    }
    s_.push({pn:sPN,from:sX,to:L,len:L-sX,P_start:sP,P_end:P});
    // consolida
    segs=[];
    for(const s of s_){
      if(segs.length&&segs[segs.length-1].pn===s.pn){segs[segs.length-1].len+=s.len;segs[segs.length-1].to=s.to;segs[segs.length-1].P_end=s.P_end;}
      else segs.push({...s});
    }
    totalHf=0; for(const s of segs) totalHf+=(jByPN[s.pn]??jByPN[125]??jByPN[80]??0)*s.len;
    const an=Hg+totalHf+filtro+pRes; if(Math.abs(an-AMT_hid)<0.05){AMT_hid=an;break;} AMT_hid=an;
  }
  return{AMT_hid,AMT_design:AMT_hid*(1+slackP),totalHf,segs,pipeByPN,jByPN,pnsUsados:new Set(segs.map(s=>s.pn))};
}

// ── PRESSÃO NO PERFIL ─────────────────────────────────────────────────
// Retorna array [{x,P}] com pontos de transição
function pressurePoints(multi,L,Hg){
  const ts=Hg/L;
  const pts=[{x:0,P:multi.AMT_design}];
  let P=multi.AMT_design;
  for(const s of multi.segs){
    const J=multi.jByPN[s.pn]??0;
    P-=(J+ts)*s.len;
    pts.push({x:s.to,P:Math.max(0,P)});
  }
  return pts;
}

// ── ENERGIA ──────────────────────────────────────────────────────────
function energyInfo(Pkw){
  const h=gv('horasDia')||8, tar=gv('tarifa')||0.80;
  return{
    kwh_h:Pkw, kwh_dia:Pkw*h, kwh_mes:Pkw*h*30,
    r_dia:Pkw*h*tar, r_mes:Pkw*h*30*tar
  };
}

// ── ESTADO GLOBAL ────────────────────────────────────────────────────
let _multi=null,_nominal=null;

// ── CALC PRINCIPAL ───────────────────────────────────────────────────
function calc(){
  const Q=gv('Q'),L=gv('L'),cotaS=gv('cotaS'),cotaR=gv('cotaR');
  const slackQ=gv('slackQ')||0,slackP=gv('slackP')||0;
  const Q_calc=Q*(1+slackQ/100);
  const eff=gv('eff'),kLoc=gv('kLoc')/100,filtro=gv('filtro'),pRes=gv('pRes');
  const Vmax=gv('Vmax')||1.5,CHW=getCHW(),Hg=cotaR-cotaS,lim=getLimits();
  if(!Q||!L){
    $('quick-results').innerHTML='<div class="sbox warn">Preencha Q, L, cotaS e cotaR.</div>';
    $('bomba-results').innerHTML='<div class="sbox warn">Preencha os dados para calcular.</div>';
    $('card-diam').style.display='none';$('card-multi').style.display='none';drawPerfil(null);return;
  }
  const nominal=findBestNominal(Q_calc,Vmax); _nominal=nominal;
  const multi=calcMultiPN(Q_calc,L,Hg,CHW,nominal,kLoc,filtro,pRes,slackP/100,lim); _multi=multi;
  const Pkw=(Q_calc/3600)*multi.AMT_design*9.81/(eff/100);
  const Pcv=Pkw/0.7355;
  buildDiamCard(nominal,Q_calc,CHW,kLoc,L,multi);
  buildMultiCard(multi,Q_calc,L,eff,slackP,Pkw,Pcv,lim);
  updateQuick(multi,Q_calc,Vmax,slackP);
  updateBomba(multi,Q_calc,eff,Pkw,Pcv);
  drawPerfil(multi,Q_calc,Hg,L,lim,cotaS,cotaR,pRes);
}

// ── CARD DIÂMETRO ─────────────────────────────────────────────────────
function buildDiamCard(nominal,Q_calc,CHW,kLoc,L,multi){
  $('card-diam').style.display='';
  const Di=dIdeal_mm(Q_calc,gv('Vmax')||1.5),Vm=gv('Vmax')||1.5;
  const pnsAtivos=[...multi.pnsUsados].sort((a,b)=>b-a);
  let rows='';
  for(const pn of pnsAtivos){
    const p=multi.pipeByPN[pn]; if(!p) continue;
    const V=velocity(Q_calc,p[3]);
    const cl=V>3?'color:#c62828;font-weight:800':V>Vm?'color:#e07b00;font-weight:800':'color:#1b6e3a;font-weight:800';
    const J=hfPerMeter(Q_calc,CHW,p[3]);
    rows+=`<tr>
      <td><span class="pn-badge ${PN_CSS[pn]}">PN ${pn}</span></td>
      <td>${p[1]} mm</td><td>${p[2]} mm</td>
      <td><strong>${fmt(p[3])} mm</strong></td>
      <td><span style="${cl}">${fmt(V)} m/s</span></td>
      <td>${fmt(J,4)} m/m</td>
      <td>${fmt(J*(1+kLoc)*L)} m</td>
    </tr>`;
  }
  $('diam-content').innerHTML=`
    <div style="display:flex;gap:1.2rem;flex-wrap:wrap;margin-bottom:.9rem;align-items:center">
      <div class="tile tb2" style="flex:0 0 auto;min-width:130px">
        <div class="tl">D. Interno Ideal</div>
        <div class="tv lg">${fmt(Di)} <small>mm</small></div>
        <div style="font-size:.7rem;color:var(--mu);margin-top:.2rem">V = ${fmt(Vm)} m/s</div>
      </div>
      <div class="tile tg" style="flex:0 0 auto;min-width:140px">
        <div class="tl">Nominal Selecionado</div>
        <div class="tv lg">${nominal} <small>mm</small></div>
        <div style="font-size:.7rem;color:var(--mu);margin-top:.2rem">D. externo nominal</div>
      </div>
      <div class="sbox info" style="flex:1;min-width:220px;margin:0;font-size:.8rem">
        Apenas os PN efetivamente usados no perfil. Mesmo nominal <strong>${nominal}mm</strong> em todos os trechos —
        D. interno varia pelas espessuras de parede de cada classe.
      </div>
    </div>
    <div class="cmp-wrap">
    <table class="cmp">
      <thead><tr>
        <th style="text-align:left;background:#f4f7fb">Classe PN</th>
        <th>D. Ext.</th><th>Espessura</th><th>D. Interno</th>
        <th>Velocidade</th><th>hf (m/m)</th><th>hf total</th>
      </tr></thead>
      <tbody>${rows}</tbody>
    </table></div>`;
}

// ── CARD MULTI-PN ────────────────────────────────────────────────────
function buildMultiCard(multi,Q_calc,L,eff,slackP,Pkw,Pcv,lim){
  $('card-multi').style.display='';
  const pnPrev={180:lim[145],145:lim[125],125:lim[80],80:lim[60],60:0};
  const motorCV=nextMotorCV(Pcv);
  const motorkW=motorCV*0.7355;
  const ch=tipoChave(motorCV);

  let bar='<div class="seg-bar">';
  for(const s of multi.segs) bar+=`<div class="seg-sec ${PN_SS[s.pn]}" style="flex:${s.len}" title="PN ${s.pn}: ${fmt(s.len,0)}m">${(s.len/L*100).toFixed(0)}%&nbsp;PN${s.pn}</div>`;
  bar+='</div>';

  let rows='';
  for(const s of multi.segs){
    const p=multi.pipeByPN[s.pn];
    const Ps=s.P_start!=null?fmt(s.P_start,1):'—';
    const Pe=s.P_end!=null?fmt(s.P_end,1):'—';
    rows+=`<tr>
      <td><span class="pn-badge ${PN_CSS[s.pn]}">PN ${s.pn}</span></td>
      <td style="white-space:nowrap">
        <div style="font-size:.78rem;font-weight:700;color:${PN_COLOR[s.pn]}">${fmt(pnPrev[s.pn],0)} &ndash; ${fmt(lim[s.pn],0)} mca</div>
        <div style="font-size:.7rem;color:var(--mu)">${Ps} &rarr; ${Pe} mca</div>
      </td>
      <td>${fmt(s.from,0)} &ndash; ${fmt(s.to,0)} m</td>
      <td><strong>${fmt(s.len,0)} m</strong></td>
      <td>${(s.len/L*100).toFixed(1)}%</td>
      <td>${p?p[0]:'—'}</td>
      <td>${p?fmt(p[3])+'mm':'—'}</td>
      <td>${p?fmt(velocity(Q_calc,p[3]))+' m/s':'—'}</td>
      <td>${fmt((multi.jByPN[s.pn]??0)*s.len)} m</td>
    </tr>`;
  }

  const lenByPN={};
  for(const s of multi.segs) lenByPN[s.pn]=(lenByPN[s.pn]||0)+s.len;
  let sumCards='';
  for(const pn of PN_CLASSES){
    if(!lenByPN[pn]) continue;
    const p=multi.pipeByPN[pn];
    sumCards+=`<div class="tile" style="border:2px solid ${PN_COLOR[pn]};background:${PN_COLOR[pn]}1a">
      <div class="tl" style="color:${PN_COLOR[pn]}">PN ${pn}</div>
      <div class="tv lg" style="color:${PN_COLOR[pn]}">${fmt(lenByPN[pn],0)} <small>m</small></div>
      <div style="font-size:.7rem;color:var(--mu)">${(lenByPN[pn]/L*100).toFixed(0)}% &nbsp;|&nbsp; ${p?p[0]:'—'}</div>
    </div>`;
  }

  $('multi-content').innerHTML=`
    ${bar}
    <div class="g5" style="margin:.5rem 0">${sumCards}</div>
    <div class="cmp-wrap">
    <table class="cmp">
      <thead><tr>
        <th>PN</th><th>Faixa de Press&#227;o</th><th>Trecho (m)</th>
        <th>Comprimento</th><th>%</th>
        <th>Tubo</th><th>D. Interno</th><th>Velocidade</th><th>hf trecho</th>
      </tr></thead>
      <tbody>${rows}
        <tr style="background:#f0f7ff;font-weight:700">
          <td colspan="3" class="lbl">TOTAL</td>
          <td><strong>${fmt(L,0)} m</strong></td><td>100%</td>
          <td colspan="3"></td><td><strong>${fmt(multi.totalHf)} m</strong></td>
        </tr>
      </tbody>
    </table></div>
    <div class="g4" style="margin-top:.8rem">
      <div class="tile tg"><div class="tl">AMT Hidr&#225;ulico</div><div class="tv lg">${fmt(multi.AMT_hid)} <small>mca</small></div></div>
      <div class="tile to"><div class="tl">AMT c/ Folga ${slackP}%</div><div class="tv lg">${fmt(multi.AMT_design)} <small>mca</small></div></div>
      <div class="tile tt"><div class="tl">Pot&#234;ncia Calculada</div><div class="tv">${fmt(Pkw)} <small>kW</small> / ${fmt(Pcv)} <small>CV</small></div></div>
      <div class="tile tb2" style="border:2px solid #0077b6">
        <div class="tl">Motor / Chave de Partida</div>
        <div style="margin-top:.25rem"><span class="motor-badge">${motorCV} CV</span></div>
        <div style="margin-top:.3rem"><span class="${ch.cls}">${ch.texto}</span></div>
      </div>
    </div>`;
}

// ── QUICK RESULTS ────────────────────────────────────────────────────
function updateQuick(multi,Q_calc,Vmax,slackP){
  const p125=multi.pipeByPN[125]||multi.pipeByPN[80];
  const V=p125?velocity(Q_calc,p125[3]):null;
  const pFinal=multi.segs.length?multi.segs[multi.segs.length-1].P_end:null;
  $('quick-results').innerHTML=`
    <div class="g2" style="margin-bottom:.5rem">
      <div class="tile tg"><div class="tl">AMT Hidráulico</div><div class="tv lg">${fmt(multi.AMT_hid)} <small>mca</small></div></div>
      <div class="tile to"><div class="tl">AMT c/ Folga ${slackP}%</div><div class="tv lg">${fmt(multi.AMT_design)} <small>mca</small></div></div>
    </div>
    <div class="g2" style="margin-bottom:.5rem">
      <div class="tile tb2"><div class="tl">Nominal</div><div class="tv">${_nominal} <small>mm</small></div></div>
      <div class="tile tb2"><div class="tl">Press&#227;o Final</div><div class="tv">${pFinal!=null?fmt(pFinal,1):'—'} <small>mca</small></div></div>
    </div>
    ${multi.segs.length>1?`<div class="sbox ok" style="font-size:.8rem">&#10003; ${multi.segs.map(s=>`PN${s.pn}: ${fmt(s.len,0)}m`).join(' → ')}</div>`:
      `<div class="sbox info" style="font-size:.8rem">Tubulação toda em PN ${multi.segs[0]?.pn||'—'}.</div>`}
    ${V&&V>Vmax?`<div class="sbox warn" style="font-size:.8rem;margin-top:.4rem">&#9888; V = ${fmt(V)} m/s excede Vmax = ${fmt(Vmax)} m/s.</div>`:''}`;
}

// ── BOMBA + MOTOR + CONSUMO ───────────────────────────────────────────
function updateBomba(multi,Q_calc,eff,Pkw_total,Pcv_total){
  const AMT=multi.AMT_design;
  function bCard(title,cls,q,h,p_kw,p_cv){
    const mCV=nextMotorCV(p_cv),mKw=mCV*0.7355,ch=tipoChave(mCV);
    const en=energyInfo(p_kw);
    return`<div class="bomba-card ${cls}">
      <div class="bc-title">
        <span>${title}</span>
        <div style="display:flex;gap:.4rem;align-items:center;flex-wrap:wrap">
          <span class="motor-badge" style="font-size:.9rem">${mCV} CV</span>
          <span class="${ch.cls}">${ch.texto}</span>
        </div>
      </div>
      <div class="bc-grid">
        <div class="bc-item"><span class="lbl">Vaz&#227;o/bomba</span><strong>${fmt(q,1)} m&#179;/h</strong></div>
        <div class="bc-item"><span class="lbl">AMT/bomba</span><strong>${fmt(h)} mca</strong></div>
        <div class="bc-item"><span class="lbl">Pot. calculada</span><strong>${fmt(p_kw)} kW / ${fmt(p_cv)} CV</strong></div>
        <div class="bc-item"><span class="lbl">Motor comercial</span><strong>${mCV} CV (${fmt(mKw,1)} kW)</strong></div>
      </div>
      <div class="bc-energy">
        <div class="bc-item"><span class="lbl">Consumo</span><strong>${fmt(en.kwh_h,1)} kW</strong></div>
        <div class="bc-item"><span class="lbl">kWh/dia</span><strong>${fmt(en.kwh_dia,1)} kWh</strong></div>
        <div class="bc-item"><span class="lbl">kWh/m&#234;s</span><strong>${fmt(en.kwh_mes,0)} kWh</strong></div>
        <div class="bc-item"><span class="lbl">Custo/dia</span><strong>${fmtR(en.r_dia)}</strong></div>
        <div class="bc-item"><span class="lbl">Custo/m&#234;s</span><strong>${fmtR(en.r_mes)}</strong></div>
      </div>
    </div>`;
  }
  $('bomba-results').innerHTML=`
    ${bCard('&#9675; 1 Bomba Solteira','bc-single',Q_calc,AMT,Pkw_total,Pcv_total)}
    ${bCard('&#8645; 2 Bombas em S&#233;rie','bc-serie',Q_calc,AMT/2,Pkw_total/2,Pcv_total/2)}
    ${bCard('&#8646; 2 Bombas em Paralelo','bc-par',Q_calc/2,AMT,Pkw_total/2,Pcv_total/2)}
    <div class="sbox info" style="font-size:.78rem;margin-top:.3rem">
      Consumo baseado em <strong>${gv('horasDia')||8} h/dia</strong> a
      <strong>R$ ${fmt(gv('tarifa')||0.80,2)}/kWh</strong> &middot; 30 dias/m&#234;s.
    </div>`;
}

// ── CANVAS — PERFIL DE PRESSÃO ────────────────────────────────────────
function drawPerfil(multi, Q_calc, Hg, L, lim, cotaS, cotaR, pRes){
  const cv=$('c-perfil'),ctx=cv.getContext('2d');
  const W=cv.width,H=cv.height;
  ctx.clearRect(0,0,W,H);
  ctx.fillStyle='#f8fbff';ctx.fillRect(0,0,W,H);
  if(!multi||!L){
    ctx.fillStyle='#9aabbc';ctx.font='16px Segoe UI';ctx.textAlign='center';
    ctx.fillText('Preencha os dados para ver o perfil de pressão',W/2,H/2);return;
  }
  const pts=pressurePoints(multi,L,Hg||0);
  const P_max=multi.AMT_design;
  const P_final=pts[pts.length-1].P;
  const yMax=Math.ceil(P_max*1.08/10)*10;
  const mg={t:44,b:58,l:72,r:48};
  const cW=W-mg.l-mg.r,cH=H-mg.t-mg.b;
  const px=x=>mg.l+(x/L)*cW;
  const py=P=>mg.t+cH*(1-P/yMax);

  // ── Bandas de fundo por classe PN ──
  const pnBands=[[0,lim[60],60],[lim[60],lim[80],80],[lim[80],lim[125],125],[lim[125],lim[145],145],[lim[145],lim[180],180]];
  for(const [p0,p1,pn] of pnBands){
    if(p1<=0||p0>=yMax) continue;
    const y0=py(Math.min(p1,yMax)),y1=py(p0);
    ctx.fillStyle=PN_BG[pn];
    ctx.fillRect(mg.l,Math.max(y0,mg.t),cW,Math.min(y1,mg.t+cH)-Math.max(y0,mg.t));
  }

  // ── Grade ──
  ctx.strokeStyle='rgba(0,80,160,.07)';ctx.lineWidth=1;
  const nY=8;
  for(let i=0;i<=nY;i++){
    const P=yMax*i/nY,y=py(P);
    ctx.beginPath();ctx.moveTo(mg.l,y);ctx.lineTo(mg.l+cW,y);ctx.stroke();
    ctx.fillStyle='#607080';ctx.font='10px Segoe UI';ctx.textAlign='right';
    ctx.fillText(fmt(P,0)+' mca',mg.l-5,y+4);
  }
  for(let i=0;i<=6;i++){
    const x=mg.l+cW*i/6;
    ctx.beginPath();ctx.moveTo(x,mg.t);ctx.lineTo(x,mg.t+cH);ctx.stroke();
    ctx.fillStyle='#607080';ctx.font='10px Segoe UI';ctx.textAlign='center';
    ctx.fillText(fmt(L*i/6,0)+'m',x,mg.t+cH+16);
  }
  ctx.fillStyle='#607080';ctx.textAlign='center';ctx.fillText('Distância ao longo da adutora (m)',mg.l+cW/2,H-8);

  // ── Linhas de limite PN ──
  for(const [,p1,pn] of pnBands){
    if(p1<=0||p1>=yMax) continue;
    const y=py(p1);
    ctx.setLineDash([5,4]);ctx.strokeStyle=PN_COLOR[pn];ctx.lineWidth=1;
    ctx.beginPath();ctx.moveTo(mg.l,y);ctx.lineTo(mg.l+cW,y);ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle=PN_COLOR[pn];ctx.font='bold 9px Segoe UI';ctx.textAlign='left';
    ctx.fillText(`Limite PN ${pn} (${fmt(p1,0)} mca)`,mg.l+4,y-3);
  }

  // ── Curva de pressão colorida por segmento ──
  for(const s of multi.segs){
    const i=multi.segs.indexOf(s);
    const x0=pts[i].x,x1=pts[i+1]?.x??L;
    const P0=pts[i].P,P1=pts[i+1]?.P??P_final;
    // Área preenchida abaixo da curva
    ctx.beginPath();
    ctx.moveTo(px(x0),py(P0));ctx.lineTo(px(x1),py(P1));
    ctx.lineTo(px(x1),py(0));ctx.lineTo(px(x0),py(0));
    ctx.closePath();
    ctx.fillStyle=PN_COLOR[s.pn]+'28';ctx.fill();
    // Linha da curva
    ctx.beginPath();ctx.moveTo(px(x0),py(P0));ctx.lineTo(px(x1),py(P1));
    ctx.strokeStyle=PN_COLOR[s.pn];ctx.lineWidth=3;ctx.stroke();
    // Linha vertical de transição
    if(i>0){
      ctx.setLineDash([3,3]);ctx.strokeStyle='rgba(0,0,0,.3)';ctx.lineWidth=1;
      ctx.beginPath();ctx.moveTo(px(x0),mg.t);ctx.lineTo(px(x0),mg.t+cH);ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle='rgba(0,0,0,.5)';ctx.font='bold 9px Segoe UI';ctx.textAlign='center';
      ctx.fillText(`${fmt(x0,0)}m`,px(x0),mg.t-5);
    }
    // Rótulo do segmento
    const mx=px((x0+x1)/2),myP=(py(P0)+py(P1))/2;
    const segMid=myP+20<mg.t+cH?myP+20:myP-10;
    ctx.fillStyle=PN_COLOR[s.pn];ctx.font='bold 11px Segoe UI';ctx.textAlign='center';
    ctx.fillText(`PN ${s.pn}`,mx,segMid);
    ctx.font='10px Segoe UI';ctx.fillText(`${fmt(s.len,0)}m`,mx,segMid+13);
  }

  // ── Pressão na bomba ──
  const circleR=6;
  ctx.fillStyle='#003d5c';ctx.beginPath();ctx.arc(px(0),py(pts[0].P),circleR,0,Math.PI*2);ctx.fill();
  ctx.fillStyle='#003d5c';ctx.font='bold 11px Segoe UI';ctx.textAlign='left';
  ctx.fillText(`Bomba: ${fmt(pts[0].P,1)} mca`,px(0)+circleR+4,py(pts[0].P)-8);

  // ── Pressão na entrega ──
  const pNom=pRes||0;
  ctx.fillStyle='#0d47a1';ctx.beginPath();ctx.arc(px(L),py(P_final),circleR,0,Math.PI*2);ctx.fill();
  ctx.fillStyle='#0d47a1';ctx.font='bold 11px Segoe UI';ctx.textAlign='right';
  ctx.fillText(`Entrega: ${fmt(P_final,1)} mca`,px(L)-circleR-4,py(P_final)-8);
  if(pNom>0){
    ctx.setLineDash([4,3]);ctx.strokeStyle='#0d47a1';ctx.lineWidth=1;
    ctx.beginPath();ctx.moveTo(mg.l,py(pNom));ctx.lineTo(mg.l+cW,py(pNom));ctx.stroke();
    ctx.setLineDash([]);
    ctx.fillStyle='#0d47a1';ctx.font='10px Segoe UI';ctx.textAlign='right';
    ctx.fillText(`P. residual min. (${fmt(pNom,0)} mca)`,mg.l+cW-4,py(pNom)-3);
  }

  // ── Legenda PN ──
  const pnsUsed=[...new Set(multi.segs.map(s=>s.pn))];
  let lx=mg.l+10,ly=mg.t+10;
  pnsUsed.forEach(pn=>{
    ctx.fillStyle=PN_COLOR[pn];ctx.fillRect(lx,ly,12,10);
    ctx.fillStyle='#1a2535';ctx.font='10px Segoe UI';ctx.textAlign='left';
    ctx.fillText(`PN ${pn}`,lx+16,ly+9);lx+=60;
  });

  // ── Título ──
  ctx.fillStyle='rgba(0,61,92,.06)';ctx.fillRect(0,0,W,36);
  ctx.fillStyle='#003d5c';ctx.font='bold 13px Segoe UI';ctx.textAlign='center';
  ctx.fillText('PERFIL DE PRESSÃO DISPONÍVEL — ADUTORA DE RECALQUE',W/2,23);
  ctx.fillStyle='#005f8e';ctx.font='10px Segoe UI';ctx.textAlign='right';
  ctx.fillText('João Paulo de Oliveira · Eng. Agrônomo · Bolsa Irriga®',W-9,H-8);
}

// ── RESET ──────────────────────────────────────────────────────────────
function resetForm(){
  ['Q','L','cotaS','cotaR','consultor','cliente','propriedade','cidade'].forEach(id=>{try{$(id).value='';}catch(e){}});
  $('eff').value=75;$('kLoc').value=15;$('pRes').value=0;$('filtro').value=0;
  $('Vmax').value=1.5;$('slackQ').value=10;$('slackP').value=10;
  $('horasDia').value=8;$('tarifa').value=0.80;
  $('lim60').value=45;$('lim80').value=65;$('lim125').value=110;$('lim145').value=130;$('lim180').value=170;
  $('material').value='140';
  $('data').value=new Date().toISOString().split('T')[0];
  _multi=null;_nominal=null;calc();
}

// ── PDF ────────────────────────────────────────────────────────────────
function gerarPDF(){
  if(!_multi){alert('Preencha os dados primeiro.');return;}
  requestAnimationFrame(()=>{ const img=$('c-perfil').toDataURL('image/png'); _popup(img); });
}
function _popup(img){
  if(!_multi) return;
  const Q=gv('Q'),L=gv('L'),cotaS=gv('cotaS'),cotaR=gv('cotaR');
  const slackQ=gv('slackQ'),slackP=gv('slackP'),Q_calc=Q*(1+slackQ/100);
  const eff=gv('eff'),kLoc=gv('kLoc'),filtro=gv('filtro'),pRes=gv('pRes');
  const horasDia=gv('horasDia')||8,tarifa=gv('tarifa')||0.80;
  const Hg=cotaR-cotaS;
  const multi=_multi;
  const Pkw=(Q_calc/3600)*multi.AMT_design*9.81/(eff/100);
  const Pcv=Pkw/0.7355;
  const motorCV=nextMotorCV(Pcv);
  const ch=tipoChave(motorCV);
  const en=energyInfo(Pkw);
  const cons=$('consultor').value||'—',cli=$('cliente').value||'—';
  const prop=$('propriedade').value||'—',cid=$('cidade').value||'—';
  const dt=$('data').value?new Date($('data').value+'T12:00:00').toLocaleDateString('pt-BR'):'—';
  const lim=getLimits();
  const pnPrev={180:lim[145],145:lim[125],125:lim[80],80:lim[60],60:0};
  const pFinal=multi.segs.length?multi.segs[multi.segs.length-1].P_end:0;

  const css=`*{box-sizing:border-box;margin:0;padding:0;font-family:'Segoe UI',sans-serif}
body{font-size:10pt;color:#1a2535;background:#fff}
.pg{padding:8mm 10mm;page-break-after:always;min-height:280mm}.pg:last-child{page-break-after:avoid}
.hd{background:linear-gradient(135deg,#003d5c,#0077b6,#00b4d8);color:#fff;padding:6px 12px;display:flex;justify-content:space-between;align-items:center;margin-bottom:6px;border-radius:4px}
.hl{display:flex;align-items:center;gap:8px}.hl img{height:40px;width:40px;background:#fff;border-radius:6px;padding:3px;object-fit:contain}
.hb h2{font-size:.95rem;font-weight:800}.hb p{font-size:.65rem;opacity:.85}
.hr2{text-align:right;font-size:.65rem;line-height:1.6}.hr2 b{font-size:.78rem;display:block}
.cli{background:#f0f7ff;border:1px solid #c0daf0;border-radius:4px;padding:4px 10px;display:grid;grid-template-columns:repeat(5,1fr);gap:4px;margin-bottom:6px;font-size:.76rem}
.cf label{font-size:.6rem;font-weight:800;color:#607080;text-transform:uppercase;display:block}
.cf span{font-weight:700;color:#003d5c}
.st{font-size:.72rem;font-weight:900;color:#0077b6;text-transform:uppercase;letter-spacing:.06em;padding:3px 0 4px;border-bottom:1.5px solid #caf0f8;margin:6px 0 4px;display:flex;align-items:center;gap:4px}
.st::before{content:'';width:3px;height:1em;background:#00b4d8;border-radius:2px;flex-shrink:0}
.gx{display:grid;gap:4px;margin-bottom:5px}
.kv{border-radius:5px;padding:4px 6px}
.kv label{font-size:.58rem;font-weight:800;color:#607080;text-transform:uppercase;display:block}
.kv strong{font-size:.88rem;color:#003d5c}
.motor-box{background:linear-gradient(135deg,#1b3a5e,#0077b6);color:#fff;border-radius:7px;padding:5px 10px;text-align:center}
.motor-box label{font-size:.6rem;font-weight:800;text-transform:uppercase;opacity:.8;display:block}
.motor-box strong{font-size:1.4rem;font-weight:900;display:block;line-height:1.2}
.tbl{width:100%;border-collapse:collapse;font-size:.78rem;margin-bottom:5px}
.tbl th{padding:3px 5px;font-size:.66rem;font-weight:800;text-transform:uppercase;text-align:center;border:1px solid #d0e4f0}
.tbl td{padding:3px 5px;border:1px solid #d0e4f0;text-align:center}
.tbl td.l{text-align:left;color:#607080;font-weight:600;background:#fafeff}
.bar{display:flex;height:22px;border-radius:5px;overflow:hidden;border:1px solid #ddd;margin-bottom:5px}
.bsec{display:flex;align-items:center;justify-content:center;font-size:.65rem;font-weight:800;color:#fff;overflow:hidden;white-space:nowrap}
.bc{display:grid;grid-template-columns:repeat(3,1fr);gap:5px;margin-bottom:5px}
.bc-c{border-radius:5px;padding:5px 7px}
.bc-c h4{font-size:.7rem;font-weight:800;margin-bottom:3px}
.bc-c .row{display:flex;justify-content:space-between;font-size:.72rem;padding:1px 0}
.img-box{border:1.5px solid #b0cce8;border-radius:5px;overflow:hidden;margin-top:4px}
.img-box img{width:100%;display:block}
.ft{border-top:1px solid #d0e4f0;padding-top:4px;margin-top:6px;display:flex;justify-content:space-between;font-size:.62rem;color:#607080}
.ft img{height:18px;width:18px;object-fit:contain;border-radius:3px;background:#f0f7ff;padding:2px;border:1px solid #d0e4f0;vertical-align:middle;margin-right:3px}
@media print{*{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important}body{margin:0}.pg{padding:5mm 8mm}}`;

  const hdr=`<div class="hd"><div class="hl"><img src="data:image/png;base64,${LOGO}" alt=""><div class="hb"><h2>Bolsa Irriga&#174; &mdash; Adutora de Recalque Multi-PN</h2><p>Hazen-Williams &middot; Sele&#231;&#227;o Multi-PN &middot; Motor &middot; Chave de Partida &middot; Consumo Energ&#233;tico</p></div></div><div class="hr2"><b>Jo&#227;o Paulo de Oliveira</b>Eng. Agr&#244;nomo &middot; Esp. Irriga&#231;&#227;o<br>bolsairriga.com.br &middot; (16) 3702-6571</div></div>`;
  const cliHtml=`<div class="cli"><div class="cf"><label>Consultor</label><span>${cons}</span></div><div class="cf"><label>Cliente</label><span>${cli}</span></div><div class="cf"><label>Propriedade</label><span>${prop}</span></div><div class="cf"><label>Cidade/UF</label><span>${cid}</span></div><div class="cf"><label>Data</label><span>${dt}</span></div></div>`;
  const foot=`<div class="ft"><div><img src="data:image/png;base64,${LOGO}" alt=""> Bolsa Irriga&#174; &middot; Av. Elias Abr&#227;o, 140 &middot; Franca &ndash; SP</div><div>Jo&#227;o Paulo de Oliveira &middot; Eng. Agr&#244;nomo</div></div>`;

  let barHtml='<div class="bar">';
  for(const s of multi.segs) barHtml+=`<div class="bsec" style="flex:${s.len};background:${PN_COLOR[s.pn]}">PN${s.pn} ${fmt(s.len,0)}m</div>`;
  barHtml+='</div>';

  let segRows='';
  for(const s of multi.segs){
    const p=multi.pipeByPN[s.pn];
    const faixa=`${fmt(pnPrev[s.pn],0)}&ndash;${fmt(lim[s.pn],0)} mca`;
    const Ps=s.P_start!=null?fmt(s.P_start,1):'—',Pe=s.P_end!=null?fmt(s.P_end,1):'—';
    segRows+=`<tr>
      <td style="font-weight:800;color:${PN_COLOR[s.pn]}">PN ${s.pn}</td>
      <td style="font-size:.72rem"><div style="font-weight:700;color:${PN_COLOR[s.pn]}">${faixa}</div><div style="color:#607080">${Ps}&rarr;${Pe} mca</div></td>
      <td>${fmt(s.from,0)}&ndash;${fmt(s.to,0)} m</td><td><strong>${fmt(s.len,0)} m</strong></td>
      <td>${(s.len/L*100).toFixed(0)}%</td><td>${p?p[0]:'—'}</td>
      <td>${p?fmt(p[3])+'mm':'—'}</td><td>${p?fmt(velocity(Q_calc,p[3]))+' m/s':'—'}</td>
      <td>${fmt((multi.jByPN[s.pn]??0)*s.len)} m</td>
    </tr>`;
  }

  function bcPDF(title,cls,q,h,p_kw,p_cv){
    const mCV=nextMotorCV(p_cv),chv=tipoChave(mCV);
    const kwh_dia=p_kw*(gv('horasDia')||8),r_mes=kwh_dia*30*(gv('tarifa')||0.80);
    return`<div class="bc-c" style="${cls}">
      <h4>${title}</h4>
      <div class="row"><span>Vaz&#227;o/bomba</span><strong>${fmt(q,1)} m&#179;/h</strong></div>
      <div class="row"><span>AMT/bomba</span><strong>${fmt(h)} mca</strong></div>
      <div class="row"><span>Pot&#234;ncia</span><strong>${fmt(p_kw)} kW / ${fmt(p_cv)} CV</strong></div>
      <div class="row"><span>Motor</span><strong>${mCV} CV</strong></div>
      <div class="row"><span>Chave</span><strong>${chv.texto.replace('&#226;','â').replace('&#233;','é').replace('&#234;','ê').replace('&#250;','ú').replace('&#227;','ã')}</strong></div>
      <div class="row"><span>kWh/dia</span><strong>${fmt(kwh_dia,1)} kWh</strong></div>
      <div class="row"><span>Custo/m&#234;s</span><strong>${fmtR(r_mes)}</strong></div>
    </div>`;
  }

  const pg1=`<div class="pg">${hdr}${cliHtml}
    <div class="st">Par&#226;metros do Sistema</div>
    <div class="gx" style="grid-template-columns:repeat(6,1fr)">
      <div class="kv" style="background:#f0f7ff;border:1px solid #cce5f4"><label>Q nominal</label><strong>${fmt(Q,0)} m&#179;/h</strong></div>
      <div class="kv" style="background:#f0f7ff;border:1px solid #cce5f4"><label>Q c&#225;lculo</label><strong>${fmt(Q_calc,1)} m&#179;/h</strong></div>
      <div class="kv" style="background:#f0f7ff;border:1px solid #cce5f4"><label>Comprimento</label><strong>${fmt(L,0)} m</strong></div>
      <div class="kv" style="background:#f0f7ff;border:1px solid #cce5f4"><label>Desnível</label><strong>${fmt(Hg)} m</strong></div>
      <div class="kv" style="background:#f0f7ff;border:1px solid #cce5f4"><label>Filtro</label><strong>${fmt(filtro,0)} mca</strong></div>
      <div class="kv" style="background:#f0f7ff;border:1px solid #cce5f4"><label>Press. Final</label><strong>${fmt(pFinal,1)} mca</strong></div>
    </div>
    <div class="gx" style="grid-template-columns:1fr 1fr 1fr 1fr 1.6fr;margin-bottom:5px">
      <div class="kv" style="background:#fff8e1;border:1px solid #ffe082"><label>AMT Hidr.</label><strong>${fmt(multi.AMT_hid)} mca</strong></div>
      <div class="kv" style="background:#fff8e1;border:1px solid #ffe082"><label>AMT c/ folga ${slackP}%</label><strong>${fmt(multi.AMT_design)} mca</strong></div>
      <div class="kv" style="background:#e8f5e9;border:1px solid #a5d6a7"><label>Pot&#234;ncia calc.</label><strong>${fmt(Pkw)} kW / ${fmt(Pcv)} CV</strong></div>
      <div class="kv" style="background:#e8f5e9;border:1px solid #a5d6a7"><label>Nominal</label><strong>${_nominal} mm</strong></div>
      <div class="motor-box"><label>Motor Comercial</label><strong>${motorCV} CV</strong><span style="font-size:.65rem;opacity:.85"> ${ch.texto.replace(/&#[0-9]+;/g,'?')}</span></div>
    </div>
    <div class="st">Segmenta&#231;&#227;o Multi-PN &mdash; Faixa de Press&#227;o por Trecho</div>
    ${barHtml}
    <table class="tbl"><thead><tr>
      <th>PN</th><th>Faixa de Press&#227;o</th><th>Trecho</th><th>Comprimento</th>
      <th>%</th><th>Tubo</th><th>D. Int.</th><th>Velocidade</th><th>hf trecho</th>
    </tr></thead><tbody>${segRows}
      <tr style="background:#f0f7ff;font-weight:700">
        <td colspan="3">TOTAL</td><td><strong>${fmt(L,0)} m</strong></td><td>100%</td>
        <td colspan="3"></td><td><strong>${fmt(multi.totalHf)} m</strong></td>
      </tr>
    </tbody></table>
    <div class="st">Motor Comercial &amp; Chave de Partida &amp; Consumo Energ&#233;tico</div>
    <div class="bc">
      ${bcPDF('1 Bomba Solteira','background:#e8f5e9;border:1.5px solid #2d9e5a',Q_calc,multi.AMT_design,Pkw,Pcv)}
      ${bcPDF('2 Bombas em S&#233;rie','background:#e3f2fd;border:1.5px solid #0077b6',Q_calc,multi.AMT_design/2,Pkw/2,Pcv/2)}
      ${bcPDF('2 Bombas em Paralelo','background:#fff3e0;border:1.5px solid #f57c00',Q_calc/2,multi.AMT_design,Pkw/2,Pcv/2)}
    </div>
    ${foot}</div>`;

  const pg2=`<div class="pg">${hdr}${cliHtml}
    <div class="st">Perfil de Press&#227;o Dispon&#237;vel ao Longo da Adutora (mca)</div>
    <div class="img-box"><img src="${img}" alt="Perfil de Press&#227;o"></div>
    ${foot}</div>`;

  const fullHtml=`<!DOCTYPE html><html lang="pt-BR"><head><meta charset="UTF-8"><title>Adutora Multi-PN &mdash; Bolsa Irriga</title><style>${css}</style></head><body>${pg1}${pg2}<script>window.addEventListener('load',()=>setTimeout(()=>window.print(),800));<\/script></body></html>`;
  const blob=new Blob([fullHtml],{type:'text/html;charset=utf-8'});
  const url=URL.createObjectURL(blob);
  const win=window.open(url,'_blank');
  if(!win)alert('Permita popups e tente novamente.');
  setTimeout(()=>URL.revokeObjectURL(url),120000);
}

$('data').value=new Date().toISOString().split('T')[0];
calc();
</script>
</body>
</html>"""

HTML = HTML.replace('##LOGO##', LOGO)
with open('adutora.html','w',encoding='utf-8') as f:
    f.write(HTML)
print(f'OK — {len(HTML):,} bytes')
