// Motor de cálculo hidráulico (Multi-PN) adaptado de ../adutora/adutora-avancada.html
// Mesmas constantes/fórmulas puras (tabela de tubos, classificação por pressão,
// perda de carga Hazen-Williams, cálculo ponto-a-ponto por perfil de elevação).
// Aqui usado com um perfil simples de 10 pontos (distância automática + cota manual)
// em vez do traçado por mapa, para alimentar as abas de Adutora/Recalque do
// Sistema de Orçamento.

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
const MOTORES_CV=[1,2,3,5,7.5,10,12.5,15,20,25,30,40,50,60,75,100,125,150,175,200,250,300];
const LIMITES_PADRAO={60:45,80:65,125:110,145:130,180:170};

function nextMotorCV(cv){return MOTORES_CV.find(m=>m>=cv)||MOTORES_CV[MOTORES_CV.length-1];}
function tipoChaveMotor(cv){
  if(cv<=7.5)return'Partida Direta';
  if(cv<=20)return'Estrela-Triângulo / Série-Paralelo';
  return'Soft Start';
}
function hfPerMeter(Q,CHW,D){if(!Q||!D)return 0;const Qm=Q/3600,Dm=D/1000;return 10.67*Math.pow(Qm,1.852)/(Math.pow(CHW,1.852)*Math.pow(Dm,4.87));}
function velocity(Q,D){const Qm=Q/3600,Dm=D/1000;return Qm/(Math.PI*Dm*Dm/4);}
function pnForPressure(P,lim){if(P<=lim[60])return 60;if(P<=lim[80])return 80;if(P<=lim[125])return 125;if(P<=lim[145])return 145;return 180;}
function dIdeal_mm(Q,Vmax){return Math.sqrt(4*(Q/3600)/(Math.PI*Vmax))*1000;}
function getPipeByNominal(Dext,pnClass){const c=PIPES.filter(p=>p[4]===pnClass);return c.length?c.reduce((b,p)=>Math.abs(p[1]-Dext)<Math.abs(b[1]-Dext)?p:b):null;}
function findBestNominal(Q,Vmax){const Di=dIdeal_mm(Q,Vmax),pn125=PIPES.filter(p=>p[4]===125).sort((a,b)=>a[3]-b[3]);for(const p of pn125){if(p[3]>=Di)return p[1];}return pn125[pn125.length-1][1];}

// Cálculo Multi-PN com perfil real ponto-a-ponto (idêntico ao de adutora-avancada.html)
function calcMultiPNProfile(Q_calc,profile,CHW,nom,kLoc,filtro,pRes,slackP,lim){
  const pipeByPN={},jByPN={};
  for(const pn of PN_CLASSES){
    pipeByPN[pn]=getPipeByNominal(nom,pn);
    if(pipeByPN[pn])jByPN[pn]=hfPerMeter(Q_calc,CHW,pipeByPN[pn][3]);
  }
  const n=profile.length,z0=profile[0].elev,L=profile[n-1].dist;
  const maxGain=Math.max(...profile.map(p=>p.elev-z0));
  let AMT_hid=maxGain+pRes+filtro+kLoc+30,segs=[],totalHf=0,criticalIdx=n-1;

  for(let iter=0;iter<20;iter++){
    let P=AMT_hid-filtro-kLoc,hfAcc=0,maxReq=0;
    const s_=[];
    let sPN=pnForPressure(P,lim),sFrom=0,sPstart=P;

    for(let i=1;i<n;i++){
      const dx=profile[i].dist-profile[i-1].dist;
      const dz=profile[i].elev-profile[i-1].elev;
      const pn=pnForPressure(P,lim);
      if(pn!==sPN){s_.push({pn:sPN,from:sFrom,to:profile[i-1].dist,len:profile[i-1].dist-sFrom,P_start:sPstart,P_end:P});sPN=pn;sFrom=profile[i-1].dist;sPstart=P;}
      const j=jByPN[pn]??jByPN[125]??jByPN[80]??jByPN[60]??0;
      hfAcc+=j*dx;
      P-=j*dx+dz;
      const req=hfAcc+(profile[i].elev-z0)+pRes+filtro+kLoc;
      if(req>maxReq){maxReq=req;criticalIdx=i;}
    }
    s_.push({pn:sPN,from:sFrom,to:L,len:L-sFrom,P_start:sPstart,P_end:P});
    segs=[];
    for(const s of s_){if(segs.length&&segs[segs.length-1].pn===s.pn){segs[segs.length-1].len+=s.len;segs[segs.length-1].to=s.to;segs[segs.length-1].P_end=s.P_end;}else segs.push({...s});}
    totalHf=hfAcc;
    if(Math.abs(maxReq-AMT_hid)<0.05){AMT_hid=maxReq;break;}
    AMT_hid=maxReq;
  }
  const AMT_design=AMT_hid*(1+slackP);
  const pIni=AMT_hid-filtro-kLoc;
  return{AMT_hid,AMT_design,pIni,totalHf,filtro,kLoc,segs,pipeByPN,jByPN,
    pnsUsados:[...new Set(segs.map(s=>s.pn))],L,
    criticalDist:profile[criticalIdx].dist,criticalElev:profile[criticalIdx].elev};
}

// Ponto de entrada de alto nível usado pelo orçamento: recebe os campos simples
// (comprimento, vazão, 10 cotas) + parâmetros hidráulicos e devolve um resultado pronto p/ UI.
function calcularAdutoraSimples(cfg){
  const {comprimento,vazao,cotas,profileData,material=140,vazaoResidual=10,perdasLocalizadas=0,
    filtro=5,margemProjeto=20,velocidadeMax=1.5,folgaVazao=0,eficienciaBomba=70,
    limiarBombaDupla=80}=cfg; // Projeto-Adutora usa 80 mca; Recalque usa 150 mca (fontes reais da planilha)
  if(!comprimento||!vazao)return null;
  // Preferência: perfil real (traçado no mapa + Google Elevation API), com fallback
  // para o perfil simples de 10 pontos (distância automática + cota manual).
  let profile;
  if(profileData&&profileData.length>=4){
    profile=profileData;
  }else{
    const n=(cotas&&cotas.length)||10;
    profile=[];
    for(let i=0;i<n;i++)profile.push({dist:comprimento*i/(n-1),elev:(cotas&&cotas[i])||0});
  }
  const Q_calc=vazao*(1+folgaVazao/100);
  const nominal=findBestNominal(Q_calc,velocidadeMax);
  const multi=calcMultiPNProfile(Q_calc,profile,material,nominal,perdasLocalizadas,filtro,vazaoResidual,margemProjeto/100,LIMITES_PADRAO);
  const Pkw=(Q_calc/3600)*multi.AMT_design*9.81/(eficienciaBomba/100);
  const Pcv=Pkw/0.7355;
  const motorCV=nextMotorCV(Pcv);
  const numBombas=multi.AMT_design>limiarBombaDupla?2:1;
  const pressaoPorBomba=numBombas===2?multi.AMT_design/2:multi.AMT_design;
  const segPrimeiro=multi.segs[0];
  const tuboSaida=segPrimeiro?`${segPrimeiro.pn===60?segPrimeiro.pn:segPrimeiro.pn}/${segPrimeiro.pn} — Ø${multi.pipeByPN[segPrimeiro.pn]?.[1]??'?'}mm`:'—';
  return{multi,nominal,Q_calc,Pkw,Pcv,motorCV,chaveMotor:tipoChaveMotor(motorCV),numBombas,pressaoPorBomba,
    tuboSaidaAdutora:tuboSaida,pipeByPN:multi.pipeByPN};
}

// ═══════════════════════════════════════════════════════════════════════════
// PORTA FIEL da aba 'Projeto - Adutora 01/02' da planilha real (v1.55) — usada pras
// Adutoras do Projeto (o Recalque continua no motor Multi-PN acima). Achado com o
// orçamento real do Adelcio Peixoto Neves: o motor Multi-PN escolhia Ø118 DEFOFO + 1
// bomba onde a planilha escolhe Ø75 PBL + 2 bombas — a planilha NÃO usa velocidade
// máxima, usa um fator K POR PROJETO ('Projeto - Adutora 01'!BH2: 0,9 / 1,05 / 0,9 nos
// 3 orçamentos reais conferidos): D.teórico(mm) = ROUNDUP(K×√Q(m³/s)×1000).
// Passo a passo (colunas da aba real):
//  1) Perfil: 'Interpolação - Adutora 0x' — 42 pontos: os 10 pontos de 'Dados de
//     Entrada' (distância = comprimento×i/9) ficam nas linhas-âncora 0,5,10,14,18,23,
//     28,32,37,41; os pontos intermediários andam comprimento/41 a partir do anterior
//     (sim, passo fixo L/41, não proporcional ao trecho — é o que a planilha faz) e a
//     cota é interpolada linearmente pelo nº de linhas entre âncoras.
//  2) BZ (teórico): perda com D.teórico; pressão inicial = Σ(hf+Δz) + pressão de saída
//     (30 mca); CA = D.int real escolhido pela classe de PN que a pressão BZ do ponto
//     pede (limites 45/65/110/140/180 mca, células BH6:BH10).
//  3) CH: refaz a perda com CA; CJ = pressão "estática ou dinâmica" (CI: só conta a
//     perda de atrito nos trechos que têm alguma válvula ABERTA dali pra jusante —
//     coluna BK "Close/Open" da planilha, importada por projeto); CK = D.int real pela
//     pressão CJ — é ESSE o tubo usado (CL = "nome popular" ex. "75/125").
//  4) CQ: refaz a perda com CK → P.Trab = CQ16 (+ correção BJ5 se der negativo).
//     Pressão = filtro(10)+válvula(6)+P.Trab; Total = Pressão×(1+folga 10%);
//     nº bombas = Total>80 ? 2 : 1 ('Dados de Entrada'!D36); pressão/bomba = D35.
//  5) Potência (CP4) = Q×1,1/3600 × Total × 999,23/75 × 100/Eficiência(CS3).
//  6) Tubos: metros por "nome popular" → barras = ROUNDUP(m/5,8) (BK61:BK86).
// Tabelas "D.teórico inteiro → D.int real" por classe de PN, extraídas das colunas
// F:I / Q:T / AA:AD / AK:AN / AU:AX (idênticas nos 3 orçamentos reais conferidos).
const PLAN_TAB_DI={
  145:[[1,118,112.2],[119,170,161.7],[171,222,211.2]],
  125:[[1,75,67.82],[76,100,91.25],[101,118,108.4],[119,170,156.4],[171,222,204.2],[223,274,252],[275,326,299],[327,378,347.6]],
  80:[[1,50,46.7],[51,75,70.4],[76,100,94.4],[101,118,111.8],[119,170,161.2],[171,222,210.4],[223,274,259.8],[275,326,309],[327,378,358.2]],
  60:[[1,50,47.8],[51,75,71.4],[76,100,96],[101,118,112.6],[119,170,162.2],[171,222,212],[223,274,261.6],[275,326,311.2],[327,378,360.8]],
  180:[[1,118,110.1],[119,170,158.8],[171,222,207.3]],
};
// Aba 'B.D' (D.int → "nome popular", VLOOKUP exato, 1ª ocorrência). 91,25 (Ø100 PN125)
// NÃO existe lá — na planilha vira #N/A e o trecho some da contagem de tubos; mantido.
const PLAN_BD_NOME={47.8:'50,5/60',46.7:'50,5/80',347.6:'378/125',300:'326/125',252:'274/125',204.2:'222/125',
  156.4:'170/125',108.4:'118/125',67.82:'75/125',504.2:'532/80',406.6:'429/80',358.2:'378/80',309:'326/80',
  259.8:'274/80',210.4:'222/80',161.2:'170/80',111.8:'118/80',94.4:'100/80',507.8:'532/60',409.4:'429/60',
  360.8:'378/60',311.2:'326/60',261.6:'274/60',212:'222/60',162.2:'170/60',112.6:'118/60',140:'150/80',
  116.6:'125/80',70.4:'75/80',46.2:'50/80',142:'150/60',118.2:'125/60',96:'100/60',71.4:'75/60',
  112.2:'118/145',110.1:'118/180',161.7:'170/145',158.8:'170/180',211.2:'222/145',207.3:'222/180'};
function planDiPorPN(pn,dTeoricoMm){
  const t=PLAN_TAB_DI[pn];if(!t)return null;
  const d=Math.max(1,dTeoricoMm);
  for(const[a,b,di]of t)if(d<=b)return di;
  return t[t.length-1][2];
}
// CA/CK: IF(AND(P<=65,P<45),PN60, IF(AND(P>=45,P<65),PN80, IF(AND(P>=65,P<=110),PN125,
// IF(AND(P>=110,P<140),PN145, IF(AND(P<=180,P>140),PN180,"00")))))
function planPNPorPressao(P,lim){
  if(P<=lim[65]&&P<lim[45])return 60;
  if(P>=lim[45]&&P<lim[65])return 80;
  if(P>=lim[65]&&P<=lim[110])return 125;
  if(P>=lim[110]&&P<lim[140])return 145;
  if(P<=lim[180]&&P>lim[140])return 180;
  return null; // "00" na planilha (ex. exatamente 140 ou >180)
}
const PLAN_ANCORAS=[0,5,10,14,18,23,28,32,37,41];
function planInterpolarPerfil(comprimento,cotas){
  const L=comprimento,passo=L/41,c=(cotas&&cotas.length===10)?cotas:new Array(10).fill(0);
  const dist=new Array(42),cota=new Array(42);
  for(let k=0;k<10;k++){dist[PLAN_ANCORAS[k]]=L*k/9;cota[PLAN_ANCORAS[k]]=c[k]||0;}
  for(let k=0;k<9;k++){
    const a=PLAN_ANCORAS[k],b=PLAN_ANCORAS[k+1],inc=(cota[b]-cota[a])/(b-a);
    for(let i=a+1;i<b;i++){dist[i]=dist[i-1]+passo;cota[i]=cota[i-1]+inc;}
  }
  const pts=[];
  for(let i=0;i<42;i++)pts.push({trecho:i===0?0:dist[i]-dist[i-1],z:cota[i]-cota[0],dist:dist[i]});
  return pts;
}
function planHf(Qm3s,C,Dmm){if(!Qm3s||!Dmm)return 0;return 10.646*(1/Math.pow(Dmm/1000,4.87))*Math.pow(Qm3s/C,1.852);}
function calcularAdutoraPlanilha(cfg){
  const{comprimento,vazao,cotas,material=140,vazaoResidual=30,perdasLocalizadas=6,filtro=10,
    margemProjeto=10,folgaVazao=10,eficienciaBomba,limiarBombaDupla=80,fatorK=0.9,
    valvulasAbertas,pressaoExtraMB=0}=cfg;
  if(!comprimento||!vazao)return null;
  const lim={45:45,65:65,110:110,140:140,180:180};
  const C=material,Pout=vazaoResidual;
  const pts=planInterpolarPerfil(comprimento,cotas);
  const n=pts.length; // 42 (linhas 16..57 da aba real)
  const Q=vazao/3600;
  const dT=Math.ceil(fatorK*Math.sqrt(Q)*1000-1e-9);
  // aberta[i]: 'OPEN' na coluna BK (linha 16+i). Padrão da planilha nova: tudo CLOSE.
  const aberta=i=>!!(valvulasAbertas&&valvulasAbertas[i]);
  const temAbertaJusante=new Array(n).fill(false);
  {let acc=false;for(let i=n-1;i>=0;i--){acc=acc||aberta(i);temAbertaJusante[i]=acc;}}
  // passo 2 — teórico
  const hfT=planHf(Q,C,dT);
  let somaBY=0;for(let i=1;i<n;i++)somaBY+=hfT*pts[i].trecho+(pts[i].z-pts[i-1].z);
  const BZ=new Array(n);BZ[0]=somaBY+Pout;
  for(let i=1;i<n;i++)BZ[i]=BZ[i-1]-(hfT*pts[i].trecho+(pts[i].z-pts[i-1].z));
  const CA=BZ.map(P=>{const pn=planPNPorPressao(P,lim);return pn?planDiPorPN(pn,dT):null;});
  // passo 3 — real 1
  const CG=new Array(n).fill(0);let somaCG=0;
  for(let i=1;i<n;i++){CG[i]=(CA[i]?planHf(Q,C,CA[i]):0)*pts[i].trecho+(pts[i].z-pts[i-1].z);somaCG+=CG[i];}
  const CH0=somaCG+Pout+pressaoExtraMB;
  const CJ=new Array(n);CJ[0]=CH0;
  for(let i=1;i<n;i++){const CI=temAbertaJusante[i]?CG[i]:(pts[i].z-pts[i-1].z);CJ[i]=CJ[i-1]-CI;}
  const CK=CJ.map(P=>{const pn=planPNPorPressao(P,lim);return pn?{pn,di:planDiPorPN(pn,dT)}:null;});
  // passo 4 — real 2
  let somaCP=0,somaCO=0;
  for(let i=1;i<n;i++){const co=(CK[i]?planHf(Q,C,CK[i].di):0)*pts[i].trecho;somaCO+=co;somaCP+=co+(pts[i].z-pts[i-1].z);}
  const BI5=somaCP+Pout,BJ5=BI5<0?-BI5:0;
  const pTrab=somaCP+Pout+pressaoExtraMB+BJ5;
  const pressao=filtro+perdasLocalizadas+pTrab;
  const AMT_design=pressao*(1+margemProjeto/100);
  const numBombas=AMT_design>limiarBombaDupla?2:1;
  const pressaoPorBomba=numBombas===2?AMT_design/2:AMT_design;
  const Q_calc=vazao*(1+folgaVazao/100);
  const efic=eficienciaBomba||(Q_calc<15?53:78);
  const Pcv=(Q_calc/3600*AMT_design*999.23/75)*100/efic;
  const Pkw=Pcv*0.736;
  // trechos por "nome popular" (linha i usa o tubo do ponto i — o trecho que chega nele)
  const metrosPorNome={};const segs=[];
  for(let i=1;i<n;i++){
    const ck=CK[i];const nome=ck?PLAN_BD_NOME[ck.di]:null;
    if(nome)metrosPorNome[nome]=(metrosPorNome[nome]||0)+pts[i].trecho;
    const ult=segs[segs.length-1];
    if(ult&&ult.nome===nome&&ult.pn===(ck&&ck.pn)){ult.len+=pts[i].trecho;ult.to=pts[i].dist;ult.P_end=CJ[i];}
    else segs.push({nome,pn:ck?ck.pn:null,di:ck?ck.di:null,from:pts[i-1].dist,to:pts[i].dist,len:pts[i].trecho,P_start:CJ[i-1],P_end:CJ[i]});
  }
  const nome0=CK[0]?PLAN_BD_NOME[CK[0].di]:null;
  const nominal=nome0?parseFloat(nome0.split('/')[0].replace(',','.')):null;
  return{motor:'planilha',dTeorico:dT,AMT_hid:pressao,AMT_design,pIni:pTrab,totalHf:somaCO,
    pnsUsados:[...new Set(segs.map(s=>s.pn).filter(Boolean))],segs,metrosPorNome,nominal,tuboSaidaAdutora:nome0||'—',
    Q_calc,Pkw,Pcv,motorCV:nextMotorCV(Pcv),chaveMotor:tipoChaveMotor(nextMotorCV(Pcv)),numBombas,pressaoPorBomba,eficiencia:efic};
}

// Seleção do Moto-Bomba principal + Quadro de Partida (motor 'MB+CH Partida' da planilha,
// validado contra 2 orçamentos reais, aba 'MB+CH Partida' — fórmulas exatas extraídas
// via openpyxl: Moto-Bomba Trifásico = R$800/cv, Quadro de Partida = R$450/cv; margem
// de segurança sobre o CV calculado (CQ4 da aba 'Projeto - Adutora 01/02'): ≤2cv → +20%,
// ≤20cv → +15%, >20cv → +10%.
// CORRIGIDO (v1.32): o CV COM margem É dividido pelo nº de bombas ANTES de arredondar
// pro catálogo — fórmula real: J5 = CQ4/K3(nºBombas), depois CEILING.MATH(J5,1,1) e só
// então VLOOKUP numa tabela 0→125cv (idêntica ao nextMotorCV: arredonda pro próximo
// tamanho comercial). A versão anterior (v1.19) NÃO dividia, por uma falsa verificação:
// no caso usado pra validar (Antonio Gilberto), CQ4=71,31 ÷ 2 = 35,66 → 40cv — e por
// coincidência dividir OU não dividir batiam no mesmo balde do catálogo (71,31 sem
// dividir também cairia perto de 75, mas o valor que a planilha mostrava já era o
// dividido, 35,66, lido por engano como se fosse o valor "sem dividir"). Caso novo
// (Miguel Angelo) prova a divisão: CQ4=31,92 ÷ 2 bombas = 15,96 → 20cv (real) — sem
// dividir daria 40cv (errado, era exatamente o sintoma que o usuário reportou: "2 bombas
// de 40 ao invés de 2 de 20").
// Fase: a planilha real NUNCA usa monofásico pro Moto-Bomba/Quadro principal — a tabela
// de códigos usada pelas fórmulas (E33:F48 e E5:F20 da aba 'MB+CH Partida') só tem
// entradas "...CVMB-TRIF"/"...CVCP-TRIF", em AMBOS os orçamentos reais (mesmo com
// energiaRede="monofásica" nos Dados de Entrada do projeto) — então aqui é sempre
// trifásico, independente do campo energiaRede (que não alimenta essa fórmula na
// planilha original).
// precos opcional: {trif,quadro} — vem da aba "Configurações" do orçamento; se omitido,
// usa os valores padrão acima (compatibilidade com chamadas antigas).
function calcularMotorEQuadroPartida(Pcv,numBombas,precos){
  if(!Pcv||!numBombas)return null;
  const p={trif:800,quadro:450,...(precos||{})};
  const margem=Pcv<=2?1.2:Pcv<=20?1.15:1.1;
  const cvComMargem=(Pcv*margem)/numBombas;
  const cvCatalogo=nextMotorCV(Math.ceil(cvComMargem));
  const trifasico=true;
  const custoMotoBomba=cvCatalogo*p.trif;
  const custoQuadroPartida=cvCatalogo*p.quadro;
  const cvFmt=String(cvCatalogo).replace('.',',');
  const faseTag=trifasico?'TRIF':'MONO';
  const faseTxt=trifasico?'Trifásico':'Monofásico';
  return{
    cvCatalogo,numBombas,
    motoBomba:{codigo:`${cvFmt}CVMB-${faseTag}`,descricao:`Moto-Bomba ${cvFmt} cvs ${faseTxt}`,custo:custoMotoBomba,qtd:numBombas},
    quadroPartida:{codigo:`${cvFmt}CVCP-${faseTag}`,descricao:`Quadro de Partida ${cvFmt} cvs ${faseTxt}`,custo:custoQuadroPartida,qtd:numBombas},
  };
}
