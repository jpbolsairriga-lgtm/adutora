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

// Seleção do Moto-Bomba principal + Quadro de Partida (motor 'MB+CH Partida' da planilha,
// validado contra orçamento real: Moto-Bomba Trifásico = R$800/cv, Monofásico = R$850/cv,
// Quadro de Partida = R$450/cv nas duas fases; margem de segurança sobre o CV calculado:
// ≤2cv → +20%, ≤20cv → +15%, >20cv → +10%; CV arredondado para cima ao catálogo padrão).
// precos opcional: {trif,mono,quadro} — vem da aba "Configurações" do orçamento; se omitido,
// usa os valores padrão acima (compatibilidade com chamadas antigas).
function calcularMotorEQuadroPartida(Pcv,numBombas,fase,precos){
  if(!Pcv||!numBombas)return null;
  const p={trif:800,mono:850,quadro:450,...(precos||{})};
  const margem=Pcv<=2?1.2:Pcv<=20?1.15:1.1;
  const cvComMargem=Pcv*margem;
  const cvPorBomba=cvComMargem/numBombas;
  const cvCatalogo=nextMotorCV(cvPorBomba);
  const trifasico=fase!=='monofásica';
  const custoMotoBomba=cvCatalogo*(trifasico?p.trif:p.mono);
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
