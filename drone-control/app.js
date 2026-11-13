'use strict';
const $=id=>document.getElementById(id),fmt=(n,d=1)=>n.toLocaleString('pt-BR',{maximumFractionDigits:d,minimumFractionDigits:d});let cityBusy=false;let altitudeBusy=false,altitudeJob=0,altitudeError="";let pointDrag=null,moveInProgress=false,moveHistory=[],terrainNeedsReview=false;let camera={zoom:1,panX:0,panY:0},fitGoogle=true,panDrag=null,suppressClick=false;let forestRaster=null,forestImage=null,forestKey=null,exclusions=[],drawKind='area';let geom=null,points=[],map=null,overlays=[],drawing=false,draft=[],busy=false,revision=0,terrainUsed=false,view=null;
function status(s,error=false){$('status').textContent=s;$('status').className=error?'error':'';}
function clearPlan(){altitudeJob++;altitudeBusy=false;altitudeError="";pointDrag=null;moveInProgress=false;moveHistory=[];terrainNeedsReview=false;points=[];terrainUsed=false;revision++;render();}
function setArea(r){const next=Planner.prepare(r);geom=next;camera={zoom:1,panX:0,panY:0};fitGoogle=true;$('forestInfo').className='muted';forestRaster=null;forestImage=null;forestKey=null;exclusions=[];drawKind='area';drawing=false;draft=[];$('finish').hidden=$('undo').hidden=true;$('coords').value=geom.ring.map(p=>p.lat.toFixed(7)+', '+p.lng.toFixed(7)).join('\n');clearPlan();status('Área pronta. Ajuste os parâmetros e distribua os pontos.');}
function sample(){setArea([{lat:-22.707,lng:-47.643},{lat:-22.7065,lng:-47.635},{lat:-22.710,lng:-47.631},{lat:-22.715,lng:-47.634},{lat:-22.7155,lng:-47.641}]);}
function svgEl(tag,attrs,text){let el=document.createElementNS('http://www.w3.org/2000/svg',tag);for(let [k,v]of Object.entries(attrs))el.setAttribute(k,v);if(text!==undefined)el.textContent=text;return el;}
function render(){updateAltitudeInfo();renderForestInfo();$('movePoints').disabled=busy||drawing||!points.length;$('undoMove').disabled=busy||drawing||moveInProgress||!moveHistory.length;const svg=$('plot');$('drawingActions').hidden=!drawing;svg.replaceChildren();$('empty').hidden=!!map||!!geom||drawing;$('areaMetric').innerHTML=geom?fmt(geom.area/10000)+' <small>ha</small>':'— <small>ha</small>';$('areaTitle').textContent=geom?'Área de levantamento':'Seu plano começa aqui';$('pointMetric').textContent=points.length||'—';let nearest=points.map(p=>points.length>1?Math.min(...points.filter(q=>q!==p).map(q=>Planner.distance(p,q))):null);$('distanceMetric').innerHTML=points.length>1?fmt(Math.min(...nearest))+' <small>m</small>':'— <small>m</small>';$('elevationMetric').textContent=terrainNeedsReview?'Revalidar ajuste':terrainUsed?'Considerado':'Não consultado';$('csv').disabled=$('kml').disabled=!points.length||moveInProgress;const rows=$('rows');rows.replaceChildren();if(!points.length){let tr=document.createElement('tr'),td=document.createElement('td');td.colSpan=7;td.textContent='Os pontos aparecerão depois da distribuição.';td.className='muted';tr.append(td);rows.append(tr);}points.forEach((p,i)=>{let tr=document.createElement('tr');const u=UTM.fromLatLng(p.lat,p.lng);[p.id,p.lat.toFixed(7),p.lng.toFixed(7),fmt(u.easting,3),fmt(u.northing,3),u.zone+' / '+u.hemisphere,Number.isFinite(p.z)?fmt(p.z,1):altitudeBusy?'…':'—'].forEach(t=>{let td=document.createElement('td');td.textContent=t;tr.append(td);});rows.append(tr);});
if(map){overlays.forEach(o=>o.setMap(null));overlays=[];if(geom){overlays.push(new google.maps.Polygon({map,paths:geom.ring,strokeColor:'#41b983',strokeWeight:2,fillColor:'#36b77c',fillOpacity:.15,clickable:false}));if(fitGoogle&&!drawing){let b=new google.maps.LatLngBounds();geom.ring.forEach(p=>b.extend(p));map.fitBounds(b,{top:35,right:35,bottom:35,left:35});fitGoogle=false;}}renderForestGoogle();if(drawing)overlays.push(new google.maps.Polyline({map,path:draft,strokeColor:'#f0b548',clickable:false}));googleDraftVertices();points.forEach(addGooglePoint);return;}
const W=svg.clientWidth||1000,H=svg.clientHeight||650;svg.setAttribute('viewBox','0 0 '+W+' '+H);
for(let x=0;x<W;x+=50)svg.append(svgEl('line',{x1:x,y1:0,x2:x,y2:H,stroke:'#d5e1d9','stroke-width':1}));for(let y=0;y<H;y+=50)svg.append(svgEl('line',{x1:0,y1:y,x2:W,y2:y,stroke:'#d5e1d9','stroke-width':1}));
if(!geom)return;
const g=geom,s=Math.min(Math.max(100,W-110)/(g.maxX-g.minX),Math.max(100,H-160)/(g.maxY-g.minY))*camera.zoom,cx=(g.minX+g.maxX)/2,cy=(g.minY+g.maxY)/2,x0=W/2+camera.panX,y0=H/2+camera.panY;
view={s,cx,cy,x0,y0};const to=p=>({x:x0+(p.x-cx)*s,y:y0-(p.y-cy)*s});
svg.append(svgEl('polygon',{points:g.xy.map(p=>{let q=to(p);return q.x+','+q.y;}).join(' '),fill:'#21835718',stroke:'#288d5c','stroke-width':2.5}));
renderForestSvg(svg,to);if(drawing)svg.append(svgEl('polyline',{points:draft.map(p=>{let q=to(g.proj.to(p));return q.x+','+q.y;}).join(' '),fill:'none',stroke:'#bc8222','stroke-width':3}));
svgDraftVertices(svg,to);const radius=pointDiameter()/2;
points.forEach(p=>{let q=to(pointDrag?.pointId===p.id?geom.proj.to(pointDrag.position):p);svg.append(svgEl('circle',{cx:q.x,cy:q.y,r:radius,fill:'#14704d',stroke:'white','stroke-width':1.5}));if($('showLabels').checked)svg.append(svgEl('text',{x:q.x+radius+5,y:q.y+4,fill:'#164d33','font-size':12,'font-weight':700,stroke:'#ffffffdd','stroke-width':3,'paint-order':'stroke','pointer-events':'none'},p.id));if(canMovePoints())svg.append(svgEl('circle',{cx:q.x,cy:q.y,r:Math.max(radius+4,12),fill:'transparent','data-point-id':p.id,style:'cursor:move;touch-action:none','aria-label':'Mover '+p.id}));});
}
function number(id,min,max,integer=false){const v=Number($(id).value);if(!$(id).value.trim()||!Number.isFinite(v)||v<min||v>max||(integer&&!Number.isInteger(v)))throw Error('Revise '+$(id).previousElementSibling.textContent+'.');return v;}
async function generate(){
  if(busy)return;
  try{
    if(drawing)throw Error('Conclua ou cancele o desenho antes de gerar pontos.');
    if(!geom)throw Error('Defina a área primeiro.');
    const count=number('count',1,100,true),spacing=number('spacing',0,10000),margin=number('margin',0,10000),use=$('terrain').checked,buffer=number('forestBuffer',0,200),automatic=$('avoidForest').checked;
    if(use&&!map)throw Error('Conecte o Google Maps antes de considerar elevação.');
    busy=true;setBusy(true);clearPlan();const rev=revision;
    if(automatic)await analyzeForest(rev);
    let c=Planner.candidates(geom,margin,2500),original=c.length;
    const manual=exclusions.map(r=>r.map(geom.proj.to));
    c=c.filter(p=>(!automatic||!Forest.blocked(p,forestRaster,buffer))&&!Forest.manualBlocked(p,manual,buffer));
    const removed=original-c.length;
    if(!c.length)throw Error('Nenhum candidato elegível. Revise as exclusões, o recuo ou o afastamento; nenhuma restrição foi ignorada.');
    if(use){
      if(c.length>400)c=Array.from({length:400},(_,i)=>c[Math.floor(i*c.length/400)]);
      status('Consultando '+c.length+' amostras de elevação no Google Maps…');
      const data=await new Promise((resolve,reject)=>{const timer=setTimeout(()=>reject(Error('A consulta de elevação excedeu 30 segundos.')),30000);new google.maps.ElevationService().getElevationForLocations({locations:c.map(p=>({lat:p.lat,lng:p.lng}))},(results,s)=>{clearTimeout(timer);s==='OK'?resolve(results):reject(Error(elevationFailure(s)));});});
      if(rev!==revision)throw Error('A área ou os parâmetros mudaram. Gere novamente.');
      if(data.length!==c.length||data.some(p=>!Number.isFinite(p.elevation)))throw Error('O Google retornou elevações incompletas.');
      c=c.map((p,i)=>({...p,z:data[i].elevation}));
    }
    if(rev!==revision)throw Error('A área ou os parâmetros mudaram. Gere novamente.');
    points=Planner.select(c,count,spacing,use);terrainUsed=use;render();
    const exclusionsText=(automatic?' Matas: Sentinel-2 '+forestRaster.year+', afastamento de '+buffer+' m.':' Matas automáticas desativadas.')+(exclusions.length?' '+exclusions.length+' exclusão(ões) adicional(is).':'')+' '+removed+' candidatos excluídos.';
    status(points.length+' de '+count+' pontos distribuídos.'+exclusionsText+(points.length<count?' A quantidade não foi atingida com as restrições atuais.':'')+(use?' Relevo considerado.':' Topografia não consultada.'),points.length<count);
  }catch(e){status(e.message,true);}finally{busy=false;setBusy(false);updateAltitudeInfo();if(map&&points.some(p=>!Number.isFinite(p.z)))void loadPointAltitudes();}
}
$('generate').onclick=generate;$('example').onclick=$('emptyExample').onclick=sample;$('apply').onclick=()=>{try{setArea($('coords').value.trim().split(/\n+/).map(l=>{let v=l.trim().split(/[;,\s]+/);if(v.length!==2)throw Error('Use latitude, longitude em graus decimais por linha (ponto decimal).');return{lat:Number(v[0]),lng:Number(v[1])};}));}catch(e){status(e.message,true);}};$('help').onclick=()=>$('guide').showModal();
['count','spacing','margin','terrain'].forEach(id=>$(id).addEventListener('change',()=>{clearPlan();status('Parâmetros alterados. Distribua os pontos novamente.');}));
$('import').onclick=()=>$('file').click();$('file').onchange=async e=>{try{const f=e.target.files[0];if(!f)return;if(f.size>5e6)throw Error('Use um arquivo de até 5 MB.');let text=await f.text(),ring;if(f.name.toLowerCase().endsWith('.kml')){let doc=new DOMParser().parseFromString(text,'application/xml');if(doc.querySelector('parsererror'))throw Error('KML inválido.');let polys=doc.getElementsByTagNameNS('*','Polygon');if(polys.length!==1)throw Error('O arquivo deve conter exatamente um polígono. Exporte apenas a área desejada.');if(polys[0].getElementsByTagNameNS('*','innerBoundaryIs').length)throw Error('Áreas com furos não são suportadas.');let outer=polys[0].getElementsByTagNameNS('*','outerBoundaryIs')[0],node=outer?.getElementsByTagNameNS('*','coordinates')[0];if(!node)throw Error('Coordenadas do contorno não encontradas.');ring=node.textContent.trim().split(/\s+/).map(t=>{let a=t.split(',').map(Number);return{lat:a[1],lng:a[0]};});}else{let j=JSON.parse(text);if(j.crs)throw Error('Use GeoJSON WGS84 sem definição de CRS alternativo.');if(j.type==='FeatureCollection'){let p=j.features.filter(f=>f.geometry?.type==='Polygon');if(p.length!==1)throw Error('Inclua exatamente um Polygon no GeoJSON.');j=p[0];}if(j.type==='Feature')j=j.geometry;if(j.type!=='Polygon'||j.coordinates.length!==1)throw Error('Use um Polygon GeoJSON sem furos.');ring=j.coordinates[0].map(p=>({lat:p[1],lng:p[0]}));}setArea(ring);$('folderName').value=f.name.replace(/\.(kml|geojson|json)$/i,'').replace(/plano de voo/i,'Pontos de Controle');}catch(e){status('Importação: '+e.message,true);}finally{e.target.value='';}};
$('draw').onclick=()=>{if(!map&&!geom){status('Para desenhar sobre imagem, conecte o Google Maps. Na vista geométrica, carregue um exemplo ou informe uma área para definir a referência.',true);return;}drawKind='area';drawing=true;draft=[];clearPlan();$('finish').hidden=$('undo').hidden=false;status('Clique no mapa para inserir vértices em sequência e depois em Concluir desenho.');};$('undo').onclick=()=>{draft.pop();render();};$('finish').onclick=()=>{try{if(drawKind==='exclusion'){const r=Planner.prepare(draft).ring;exclusions.push(r);drawing=false;draft=[];$('finish').hidden=$('undo').hidden=true;clearPlan();status('Exclusão adicional salva. Distribua os pontos novamente.');}else setArea(draft);}catch(e){status(e.message,true);}};$('plot').onclick=e=>{if(suppressClick){suppressClick=false;return;}if(drawing&&e.target?.getAttribute?.('data-close-polygon')==='true'){if(draft.length<3){status('Insira pelo menos três vértices.',true);return;}$('finish').onclick();return;}if(!drawing||!view||!geom)return;let pt=$('plot').createSVGPoint();pt.x=e.clientX;pt.y=e.clientY;pt=pt.matrixTransform($('plot').getScreenCTM().inverse());draft.push(geom.proj.from({x:(pt.x-view.x0)/view.s+view.cx,y:(view.y0-pt.y)/view.s+view.cy}));render();};
window.gm_authFailure=()=>{status('Google Maps não autorizou a chave. Confira restrições de endereço, APIs e faturamento.',true);$('connect').disabled=false;};$('connect').onclick=async()=>{try{if(map){status('Google Maps já está conectado nesta sessão.');return;}const key=$('key').value.trim();if(!key)throw Error('Informe sua chave de API.');saveApiKey();$('connect').disabled=true;status('Conectando ao Google Maps…');await new Promise((resolve,reject)=>{let script=document.createElement('script');const timeout=setTimeout(()=>reject(Error('A conexão demorou demais. Recarregue a página para tentar novamente.')),20000);window.droneMapsReady=()=>{clearTimeout(timeout);resolve();};script.src='https://maps.googleapis.com/maps/api/js?key='+encodeURIComponent(key)+'&callback=droneMapsReady&loading=async&v=quarterly&language=pt-BR';script.onerror=()=>{clearTimeout(timeout);reject(Error('Não foi possível carregar Google Maps. Confira sua conexão.'));};document.head.append(script);});$('googlemap').hidden=false;$('plot').hidden=true;fitGoogle=true;map=new google.maps.Map($('googlemap'),{center:geom?geom.ring[0]:{lat:-22.711,lng:-47.638},zoom:15,mapTypeId:'hybrid',mapTypeControlOptions:{position:google.maps.ControlPosition.LEFT_CENTER},streetViewControl:false,fullscreenControl:false,gestureHandling:'greedy',scrollwheel:true});map.addListener('click',e=>{if(drawing){draft.push(e.latLng.toJSON());render();}});$('empty').hidden=true;$('mapMode').textContent='Google Maps · satélite e terreno';render();$('empty').hidden=true;status('Google Maps conectado. Você pode desenhar a área e ativar a consulta de relevo.');if(points.length)void loadPointAltitudes();}catch(e){status(e.message,true);$('connect').disabled=false;}};
function download(name,type,body){let url=URL.createObjectURL(new Blob([body],{type})),a=document.createElement('a');a.href=url;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);}
$('csv').onclick=()=>{if(!points.length||moveInProgress)return;download('pontos-planejados-wgs84.csv','text/csv;charset=utf-8','\ufeffid,latitude_wgs84,longitude_wgs84,utm_e_m,utm_n_m,utm_zona,utm_hemisferio,utm_epsg,datum,tipo\r\n'+points.map(p=>{const u=UTM.fromLatLng(p.lat,p.lng);return [p.id,p.lat.toFixed(8),p.lng.toFixed(8),u.easting.toFixed(3),u.northing.toFixed(3),u.zone,u.hemisphere,u.epsg,'WGS84','planejado_nao_medido'].join(',');}).join('\r\n'));};$('kml').onclick=()=>{if(!points.length||moveInProgress)return;const result=exportPlanKml();download(result.filename,'application/vnd.google-earth.kml+xml',result.body);};
if(document.modelContext?.registerTool){try{Promise.resolve(document.modelContext.registerTool({name:'read_control_plan',description:'Lê os pontos planejados e a área atual, sem alterar o plano.',inputSchema:{type:'object',properties:{},additionalProperties:false},annotations:{readOnlyHint:true},execute:()=>({areaHa:geom?geom.area/10000:null,terrainConsidered:terrainUsed,forestEnabled:$('avoidForest').checked,forestYear:forestRaster?.year??null,additionalExclusions:exclusions.length,points:points.map(p=>({id:p.id,lat:p.lat,lng:p.lng,utm:UTM.fromLatLng(p.lat,p.lng)}))})})).catch(()=>{});}catch{}}
function setBusy(value){$('generate').disabled=$('analyzeForest').disabled=value;$('movePoints').disabled=value||drawing||!points.length;}
function renderForestInfo(){
  $('cancelDrawing').hidden=!drawing;
  const info=$('forestInfo');
  if(forestRaster){info.className='muted';info.textContent='Sentinel-2 '+forestRaster.year+' · pixels de aproximadamente 10 m. '+fmt(forestRaster.coverage*100,1)+'% da área amostrada com classificação válida; '+fmt(forestRaster.trees/forestRaster.insideCount*100,1)+'% com árvores. '+(forestRaster.unknown?'Pixels sem classificação ou com nuvens serão excluídos. ':'')+(!$('avoidForest').checked?'Camada desativada.':'');}
  else if(!info.classList.contains('error'))info.textContent=$('avoidForest').checked?'Ainda não consultado. A análise será feita antes de distribuir.':'Exclusão automática desligada.';
  const list=$('exclusionList');list.replaceChildren();exclusions.forEach((r,i)=>{const row=document.createElement('div');row.className='exclusion-item';const text=document.createElement('span');text.textContent='Exclusão adicional '+(i+1);const button=document.createElement('button');button.textContent='Remover';button.onclick=()=>{exclusions.splice(i,1);clearPlan();status('Exclusão removida. Distribua novamente.');};row.append(text,button);list.append(row);});
}
async function analyzeForest(rev){
  const buffer=number('forestBuffer',0,200),year=$('forestYear').value,key=JSON.stringify([geom.ring,buffer,year]);
  if(forestKey===key&&forestRaster)return;
  status('Consultando classificação de árvores Sentinel-2…');$('forestInfo').className='muted';$('forestInfo').textContent='Consultando classificação anual…';
  try{
    const result=await Forest.load(geom,buffer,year);
    if(rev!==revision)throw Error('A área ou os parâmetros mudaram durante a consulta. Analise novamente.');
    forestRaster=result;forestKey=key;forestImage=Forest.overlay(result);render();
  }catch(e){if(rev===revision){forestRaster=null;forestKey=null;forestImage=null;$('forestInfo').className='muted error';$('forestInfo').textContent='Análise indisponível: '+e.message;}throw e;}
}
function renderForestGoogle(){
  if(forestRaster&&forestImage&&$('avoidForest').checked){const e=forestRaster.extent;overlays.push(new google.maps.GroundOverlay(forestImage,{south:e.ymin,north:e.ymax,west:e.xmin,east:e.xmax},{map,clickable:false,opacity:.8}));}
  exclusions.forEach(r=>overlays.push(new google.maps.Polygon({map,paths:r,strokeColor:'#bd641e',strokeWeight:2,fillColor:'#db8b37',fillOpacity:.3,clickable:false})));
}
function renderForestSvg(svg,to){
  if(forestRaster&&forestImage&&$('avoidForest').checked){const r=forestRaster,a=to({x:r.sw.x,y:r.ne.y}),b=to({x:r.ne.x,y:r.sw.y});svg.append(svgEl('image',{href:forestImage,x:a.x,y:a.y,width:b.x-a.x,height:b.y-a.y,preserveAspectRatio:'none',style:'image-rendering:pixelated;pointer-events:none'}));}
  exclusions.forEach(r=>svg.append(svgEl('polygon',{points:r.map(p=>{let q=to(geom.proj.to(p));return q.x+','+q.y;}).join(' '),fill:'#db8b374d',stroke:'#bd641e','stroke-width':2})));
}
function forestExportNote(){return ($('avoidForest').checked&&forestRaster?'Matas excluídas com Sentinel-2 '+forestRaster.year+' (Esri, Impact Observatory, Microsoft), resolução 10 m; afastamento '+Number($('forestBuffer').value)+' m.':'Exclusão automática de matas desativada.')+' Exclusões adicionais: '+exclusions.length+'.';}
$('analyzeForest').onclick=async()=>{if(busy)return;try{if(!geom)throw Error('Defina uma área primeiro.');if(drawing)throw Error('Conclua ou cancele o desenho primeiro.');if(!$('avoidForest').checked)throw Error('Ative a exclusão automática para analisar.');busy=true;setBusy(true);clearPlan();await analyzeForest(revision);status('Classificação carregada. Confira as matas destacadas e distribua os pontos.');}catch(e){status(e.message,true);}finally{busy=false;setBusy(false);}};
['avoidForest','forestBuffer','forestYear'].forEach(id=>$(id).addEventListener('change',()=>{if(id!=='avoidForest'){forestRaster=null;forestKey=null;forestImage=null;}$('forestInfo').className='muted';clearPlan();status('Configuração de exclusão alterada. Distribua novamente.');}));
$('drawExclusion').onclick=()=>{if(!geom){status('Defina a área primeiro.',true);return;}drawKind='exclusion';drawing=true;draft=[];clearPlan();$('finish').hidden=$('undo').hidden=false;status('Clique nos vértices da exclusão no mapa e em Concluir desenho. A exclusão recebe o mesmo afastamento configurado para matas.');};
$('cancelDrawing').onclick=()=>{drawing=false;draft=[];drawKind='area';$('finish').hidden=$('undo').hidden=true;render();status('Desenho cancelado.');};

function pointDiameter(){return Math.max(6,Math.min(36,Number($('markerSize').value)||14));}
function googlePointIcon(){const d=pointDiameter(),r=d/2;return{url:'data:image/svg+xml,'+encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" width="'+d+'" height="'+d+'"><circle cx="'+r+'" cy="'+r+'" r="'+(r-1)+'" fill="#14704d" stroke="white" stroke-width="1.5"/></svg>'),scaledSize:new google.maps.Size(d,d),anchor:new google.maps.Point(r,r),labelOrigin:new google.maps.Point(r,-8)};}
function resetCamera(){camera={zoom:1,panX:0,panY:0};fitGoogle=true;render();}
$('fitArea').onclick=resetCamera;
$('markerSize').oninput=()=>{$('markerSizeValue').textContent=pointDiameter()+' px';render();};
$('showLabels').onchange=render;
$('toggleSettings').onclick=()=>{const hidden=document.body.classList.toggle('settings-hidden');$('toggleSettings').textContent=hidden?'Mostrar painel':'Ocultar painel';$('toggleSettings').setAttribute('aria-expanded',String(!hidden));requestAnimationFrame(()=>{if(map)google.maps.event.trigger(map,'resize');render();});};
function toggleExpanded(){const expanded=$('mapwrap').classList.toggle('expanded-map');$('expandMap').textContent=expanded?'Voltar ao painel':'Ampliar mapa';$('expandMap').setAttribute('aria-pressed',String(expanded));requestAnimationFrame(()=>{if(map)google.maps.event.trigger(map,'resize');render();});}
$('expandMap').onclick=toggleExpanded;
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&$('mapwrap').classList.contains('expanded-map'))toggleExpanded();});
$('mapFinish').onclick=()=>$('finish').click();$('mapUndo').onclick=()=>$('undo').click();$('mapCancel').onclick=()=>$('cancelDrawing').click();
function svgPosition(e){let p=$('plot').createSVGPoint();p.x=e.clientX;p.y=e.clientY;return p.matrixTransform($('plot').getScreenCTM().inverse());}
$('plot').addEventListener('wheel',e=>{
 if(!geom||map||!view)return;e.preventDefault();if(pointDrag)return;
 const p=svgPosition(e),next=Math.max(.25,Math.min(100,camera.zoom*Math.exp(-Math.max(-250,Math.min(250,e.deltaY*(e.deltaMode===1?16:e.deltaMode===2?600:1)))*.002))),ratio=next/camera.zoom;
 const w=$('plot').clientWidth||1000,h=$('plot').clientHeight||650;
 camera.panX=p.x-w/2-(p.x-w/2-camera.panX)*ratio;camera.panY=p.y-h/2-(p.y-h/2-camera.panY)*ratio;camera.zoom=next;render();
},{passive:false});
$('plot').addEventListener('pointerdown',e=>{if(e.button!==0||!geom||map)return;if(startPointDrag(e))return;panDrag={id:e.pointerId,x:e.clientX,y:e.clientY,panX:camera.panX,panY:camera.panY,moved:false};$('plot').setPointerCapture(e.pointerId);});
$('plot').addEventListener('pointermove',e=>{if(previewPointDrag(e))return;if(!panDrag||panDrag.id!==e.pointerId)return;const dx=e.clientX-panDrag.x,dy=e.clientY-panDrag.y;if(Math.hypot(dx,dy)>4)panDrag.moved=true;if(panDrag.moved){camera.panX=panDrag.panX+dx;camera.panY=panDrag.panY+dy;render();}});
function stopPan(e){if(finishPointDrag(e))return;if(!panDrag||panDrag.id!==e.pointerId)return;suppressClick=panDrag.moved;panDrag=null;if($('plot').hasPointerCapture(e.pointerId))$('plot').releasePointerCapture(e.pointerId);setTimeout(()=>{suppressClick=false;},0);}
$('plot').addEventListener('pointerup',stopPan);$('plot').addEventListener('pointercancel',stopPan);
if(typeof ResizeObserver!=='undefined'){let timer;new ResizeObserver(()=>{clearTimeout(timer);timer=setTimeout(()=>render(),60);}).observe($('mapwrap'));}


function xmlText(value){return String(value).replace(/[\u0000-\u0008\u000B\u000C\u000E-\u001F]/g,'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&apos;'}[c]));}
function exportPlanKml(){
 const name=$('folderName').value.trim()||'Pontos de Controle';
 const pointXml=points.map(p=>'    <Placemark>\n      <name>'+xmlText(p.id)+'</name>\n      <description>Ponto planejado; medir com RTK.</description>\n      <Point><altitudeMode>clampToGround</altitudeMode><coordinates>'+p.lng.toFixed(8)+','+p.lat.toFixed(8)+',0</coordinates></Point>\n    </Placemark>').join('\n');
 let area='';
 if($('includeArea').checked&&geom){const closed=[...geom.ring,geom.ring[0]].map(p=>p.lng+','+p.lat+',0').join(' ');area='\n  <Folder><name>Área de levantamento</name><Placemark><name>Limite da área</name><Style><LineStyle><color>ff58a82a</color><width>2</width></LineStyle><PolyStyle><color>2258a82a</color></PolyStyle></Style><Polygon><altitudeMode>clampToGround</altitudeMode><outerBoundaryIs><LinearRing><coordinates>'+closed+'</coordinates></LinearRing></outerBoundaryIs></Polygon></Placemark></Folder>';}
 return{filename:name.replace(/[<>:"/\\|?*\u0000-\u001F]/g,'_').replace(/[. ]+$/g,'').slice(0,160)+'.kml',body:'<?xml version="1.0" encoding="UTF-8"?>\n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\n  <name>'+xmlText(name)+'.kml</name>\n  <description>'+xmlText('Posições planejadas WGS84. Validar e medir com RTK. '+forestExportNote())+'</description>\n  <Folder>\n    <name>'+xmlText(name)+'</name>\n    <open>1</open>\n'+pointXml+'\n  </Folder>'+area+'\n</Document>\n</kml>'};
}
const API_KEY_STORAGE='dronecontrol.googleMapsApiKey.v1';
function saveApiKey(){
 const key=$('key').value.trim();
 if(!key)return false;
 try{localStorage.setItem(API_KEY_STORAGE,key);$('keyStorageInfo').textContent='Chave guardada neste navegador. Será preenchida na próxima abertura.';return true;}
 catch{$('keyStorageInfo').textContent='Este navegador bloqueou o armazenamento. A chave funcionará apenas nesta sessão.';return false;}
}
function restoreApiKey(){
 try{const key=localStorage.getItem(API_KEY_STORAGE);if(key){$('key').value=key;$('keyStorageInfo').textContent='Chave guardada recuperada. Clique em Conectar Google Maps para usar.';}}
 catch{$('keyStorageInfo').textContent='Armazenamento indisponível neste navegador. A chave funcionará apenas nesta sessão.';}
}
$('key').addEventListener('change',saveApiKey);
$('saveKey').onclick=()=>{if(!$('key').value.trim()){$('keyStorageInfo').textContent='Digite a chave antes de guardar.';return;}saveApiKey();};
$('forgetKey').onclick=()=>{try{localStorage.removeItem(API_KEY_STORAGE);$('key').value='';$('keyStorageInfo').textContent='Chave apagada do navegador.'+(map?' A conexão atual continua até fechar ou recarregar a página.':'');}catch{$('keyStorageInfo').textContent='Não foi possível apagar a chave. Verifique as permissões de armazenamento do navegador.';}};
restoreApiKey();


function canMovePoints(){return $('movePoints').checked&&!drawing&&!busy;}
function moveControlPoint(id,latlng,expectedRevision=revision){
 try{
  if(!canMovePoints())throw Error('Ative Mover pontos e conclua qualquer operação em andamento.');
  if(expectedRevision!==revision)throw Error('O plano mudou durante o ajuste. Tente novamente.');
  const i=points.findIndex(p=>p.id===id);if(i<0||!geom)throw Error('Ponto não encontrado no plano atual.');
  if(!latlng||!Number.isFinite(latlng.lat)||!Number.isFinite(latlng.lng)||Math.abs(latlng.lat)>80||Math.abs(latlng.lng)>180)throw Error('Posição inválida.');
  const xy=geom.proj.to(latlng),margin=number('margin',0,10000),spacing=number('spacing',0,10000),buffer=number('forestBuffer',0,200);
  if(!Planner.inside(xy,geom.xy))throw Error('O ponto deve ficar dentro da área.');
  if(Math.min(...geom.xy.map((p,j)=>Planner.segment(xy,p,geom.xy[(j+1)%geom.xy.length])))+1e-6<margin)throw Error('Mantenha o recuo de '+margin+' m da borda.');
  if($('avoidForest').checked&&(!forestRaster||Forest.blocked(xy,forestRaster,buffer)))throw Error('Esta posição está em mata, em sua faixa de afastamento ou sem classificação válida.');
  if(Forest.manualBlocked(xy,exclusions.map(r=>r.map(geom.proj.to)),buffer))throw Error('Esta posição está em uma exclusão adicional ou em sua faixa de afastamento.');
  if(points.some((p,j)=>j!==i&&Planner.distance(p,xy)+1e-6<spacing))throw Error('Mantenha a distância mínima de '+spacing+' m dos outros pontos.');
  if(Planner.distance(points[i],xy)<.001){render();return true;}
  moveHistory.push({points:points.map(p=>({...p})),terrainUsed,terrainNeedsReview});if(moveHistory.length>30)moveHistory.shift();
  const updated={...points[i],...xy,lat:latlng.lat,lng:latlng.lng,manuallyAdjusted:true};delete updated.z;points[i]=updated;
  if(terrainUsed||terrainNeedsReview){terrainNeedsReview=true;terrainUsed=false;}
  revision++;render();
  status(id+' ajustado. Coordenadas geográficas, UTM e exportações atualizadas.'+(terrainNeedsReview?' A seleção por relevo não foi recalculada após o ajuste.':''));if(map)void loadPointAltitudes();
  return true;
 }catch(e){render();status('Ajuste não aplicado: '+e.message,true);return false;}
}
function cancelPointMove(){pointDrag=null;moveInProgress=false;render();}
$('movePoints').onchange=()=>{cancelPointMove();status($('movePoints').checked?'Arraste um ponto para ajustar. Limite, recuo, exclusões e distância mínima continuam ativos.':'Movimentação de pontos desativada.');};
$('undoMove').onclick=()=>{if(busy||drawing||moveInProgress)return;const previous=moveHistory.pop();if(!previous)return;points=previous.points;terrainUsed=previous.terrainUsed;terrainNeedsReview=previous.terrainNeedsReview;revision++;render();status('Último ajuste desfeito.');if(map)void loadPointAltitudes();};
function addGooglePoint(p){
 const marker=new google.maps.Marker({map,position:{lat:p.lat,lng:p.lng},draggable:canMovePoints(),label:$('showLabels').checked?{text:p.id,color:'#164d33',fontSize:'12px',className:'point-label'}:null,icon:googlePointIcon(),title:p.id+(canMovePoints()?' · arraste para ajustar':'')});
 let dragRevision=revision;
 marker.addListener('dragstart',()=>{dragRevision=revision;moveInProgress=true;$('csv').disabled=$('kml').disabled=true;$('undoMove').disabled=true;});
 marker.addListener('dragend',e=>{moveInProgress=false;moveControlPoint(p.id,e.latLng?.toJSON(),dragRevision);});
 overlays.push(marker);
}
function startPointDrag(e){
 const id=e.target?.getAttribute?.('data-point-id');
 if(!id||!canMovePoints())return false;
 const p=points.find(p=>p.id===id);if(!p)return false;
 e.preventDefault();pointDrag={pointerId:e.pointerId,pointId:id,rev:revision,position:{lat:p.lat,lng:p.lng}};moveInProgress=true;
 $('plot').setPointerCapture(e.pointerId);render();return true;
}
function previewPointDrag(e){
 if(!pointDrag||pointDrag.pointerId!==e.pointerId)return false;
 const q=svgPosition(e);pointDrag.position=geom.proj.from({x:(q.x-view.x0)/view.s+view.cx,y:(view.y0-q.y)/view.s+view.cy});render();return true;
}
function finishPointDrag(e){
 if(!pointDrag||pointDrag.pointerId!==e.pointerId)return false;
 const drag=pointDrag;pointDrag=null;moveInProgress=false;
 if($('plot').hasPointerCapture(e.pointerId))$('plot').releasePointerCapture(e.pointerId);
 suppressClick=true;setTimeout(()=>{suppressClick=false;},0);
 if(e.type==='pointercancel'){render();status('Ajuste cancelado.');}
 else moveControlPoint(drag.pointId,drag.position,drag.rev);
 return true;
}
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&pointDrag){cancelPointMove();status('Ajuste cancelado.');}});


function updateAltitudeInfo(){
 const known=points.filter(p=>Number.isFinite(p.z)).length;
 $('pointElevations').disabled=!points.length||busy||altitudeBusy||moveInProgress;
 $('altitudeInfo').textContent=altitudeBusy?'Consultando as altitudes dos pontos no Google…':altitudeError||(!points.length?'Altitude estimada do terreno · fonte: Google Elevation.':known===points.length?'Altitudes consultadas: '+known+' pontos · Google Elevation.':!map?'Conecte o Google Maps para consultar as altitudes. — significa cota ainda não consultada.':known+' de '+points.length+' pontos com altitude. Clique em Consultar altitudes para completar.');
}
async function loadPointAltitudes(){
 if(busy||moveInProgress)return false;
 if(!points.length)return false;
 if(!map){altitudeError='Conecte o Google Maps com a Elevation API habilitada para consultar as altitudes.';updateAltitudeInfo();return false;}
 const pending=points.filter(p=>!Number.isFinite(p.z)).map(p=>({id:p.id,lat:p.lat,lng:p.lng}));
 if(!pending.length){altitudeError='';updateAltitudeInfo();return true;}
 const job=++altitudeJob;altitudeBusy=true;altitudeError='';render();
 try{
  const result=await new Promise((resolve,reject)=>{const timer=setTimeout(()=>reject(Error('A consulta de altitude excedeu 30 segundos. Tente novamente.')),30000);
   try{new google.maps.ElevationService().getElevationForLocations({locations:pending.map(p=>({lat:p.lat,lng:p.lng}))},(values,s)=>{clearTimeout(timer);s==='OK'?resolve(values):reject(Error(elevationFailure(s)));});}catch(e){clearTimeout(timer);reject(e);}
  });
  if(job!==altitudeJob)return false;
  if(!Array.isArray(result)||result.length!==pending.length||result.some(p=>!Number.isFinite(p.elevation)))throw Error('O Google retornou altitudes incompletas. Tente novamente.');
  pending.forEach((original,i)=>{const p=points.find(p=>p.id===original.id&&p.lat===original.lat&&p.lng===original.lng);if(p)p.z=result[i].elevation;});
  return true;
 }catch(e){if(job===altitudeJob)altitudeError=e.message||'Não foi possível consultar as altitudes.';return false;}
 finally{if(job===altitudeJob){altitudeBusy=false;render();}}
}
$('pointElevations').onclick=()=>loadPointAltitudes();


async function ensureMapForLocation(){
 if(map)return true;
 if($('connect').disabled)throw Error('A conexão com o Google Maps está em andamento. Aguarde e tente novamente.');
 if(!$('key').value.trim()){
  $('key').closest?.('details')?.setAttribute('open','');$('key').focus?.();
  throw Error('Informe sua chave em Google Maps e elevação. Para buscar cidades, habilite também a Geocoding API.');
 }
 await $('connect').onclick();
 if(!map)throw Error('Não foi possível conectar o Google Maps. Confira a chave e as APIs habilitadas.');
 return true;
}
async function startAreaDrawing(){
 try{
  if(busy||moveInProgress||cityBusy)throw Error('Aguarde a operação em andamento.');
  if(!map&&!geom)await ensureMapForLocation();
  drawKind='area';drawing=true;draft=[];clearPlan();$('finish').hidden=$('undo').hidden=false;
  status('Desenhe no mapa: clique em cada vértice. Para fechar, clique no primeiro vértice ou em Concluir desenho. Arraste o fundo para mover e use a roda para aproximar.');
 }catch(e){status(e.message,true);}
}
function selectCity(result){
 if(drawing||moveInProgress||busy){$('cityStatus').textContent='Conclua a operação atual antes de mudar a localização.';return;}
 if(!result.geometry?.location){$('cityStatus').textContent='A cidade não possui localização utilizável.';return;}
 fitGoogle=false;
 if(result.geometry.viewport)map.fitBounds(result.geometry.viewport,{top:100,right:40,bottom:60,left:40});
 else {map.setCenter(result.geometry.location);map.setZoom(13);}
 $('cityResults').replaceChildren();$('cityStatus').textContent=(result.formatted_address||$('cityName').value)+' — aproxime a área e clique em Desenhar área.';
 $('empty').hidden=true;
 status('Localização encontrada. O mapa foi reposicionado; o plano existente não foi alterado.');
}
async function searchCity(){
 if(cityBusy)return;
 try{
  const address=$('cityName').value.trim();if(!address)throw Error('Digite o nome da cidade, de preferência com UF ou país.');
  if(drawing||moveInProgress||busy)throw Error('Conclua ou cancele a operação atual antes de buscar outra cidade.');
  cityBusy=true;$('citySearchButton').disabled=true;$('cityResults').replaceChildren();$('cityStatus').textContent='Localizando cidade…';
  await ensureMapForLocation();
  const results=await new Promise((resolve,reject)=>{
   const timer=setTimeout(()=>reject(Error('A busca excedeu 20 segundos. Tente novamente.')),20000);
   try{new google.maps.Geocoder().geocode({address,region:'br'},(values,s)=>{clearTimeout(timer);
    if(s==='OK'&&values?.length)resolve(values);
    else reject(Error(s==='ZERO_RESULTS'?'Cidade não encontrada. Acrescente a UF ou o país.':s==='REQUEST_DENIED'?'Busca não autorizada. Habilite a Geocoding API no projeto da chave e confira as restrições.':'Não foi possível buscar a cidade ('+s+').'));
   });}catch(e){clearTimeout(timer);reject(e);}
  });
  if($('cityName').value.trim()!==address){$('cityStatus').textContent='O nome foi alterado durante a busca. Clique em Buscar novamente.';return;}
  if(results.length===1)selectCity(results[0]);
  else{
   $('cityStatus').textContent='Selecione a localização correta:';
   results.slice(0,5).forEach(result=>{const b=document.createElement('button');b.type='button';b.textContent=result.formatted_address;b.onclick=()=>selectCity(result);$('cityResults').append(b);});
  }
 }catch(e){$('cityStatus').textContent=e.message;status(e.message,true);}
 finally{cityBusy=false;$('citySearchButton').disabled=false;}
}
$('cityForm').onsubmit=e=>{e.preventDefault();void searchCity();};
$('draw').onclick=startAreaDrawing;
$('mapDrawArea').onclick=startAreaDrawing;
function googleDraftVertices(){
 if(!drawing)return;
 draft.forEach((p,i)=>{
  const marker=new google.maps.Marker({map,position:p,icon:{path:google.maps.SymbolPath.CIRCLE,scale:i===0?8:5,fillColor:i===0?'#14704d':'#bd852c',fillOpacity:1,strokeColor:'#fff',strokeWeight:2},title:i===0?'Clique para fechar o polígono':'Vértice '+(i+1),clickable:i===0});
  if(i===0)marker.addListener('click',()=>{if(draft.length<3){status('Insira pelo menos três vértices.',true);return;}$('finish').onclick();});
  overlays.push(marker);
 });
}
function svgDraftVertices(svg,to){
 if(!drawing)return;
 draft.forEach((p,i)=>{const q=to(geom.proj.to(p));svg.append(svgEl('circle',{cx:q.x,cy:q.y,r:i===0?8:5,fill:i===0?'#14704d':'#bd852c',stroke:'#fff','stroke-width':2,'data-close-polygon':i===0?'true':'false',style:i===0?'cursor:pointer':''}));});
}

render();

function elevationFailure(code){
 if(code==='REQUEST_DENIED')return 'Google recusou a consulta de elevação (REQUEST_DENIED). Confira se a Maps Elevation API está ativada no projeto da chave em uso e permitida nessa chave, e se o faturamento está ativo. Se tudo estiver correto, consulte o Console do navegador para o motivo detalhado. Para planejar sem relevo, desmarque Considerar variação de elevação e distribua novamente.';
 if(code==='OVER_QUERY_LIMIT')return 'Limite de consultas de elevação atingido (OVER_QUERY_LIMIT). Confira a cota da Elevation API e tente novamente mais tarde.';
 return 'Consulta de elevação falhou ('+code+'). Tente novamente e confira o Console do navegador se persistir.';
}