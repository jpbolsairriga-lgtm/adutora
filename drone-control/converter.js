(function(){
'use strict';
const el=id=>document.getElementById(id);let results=[];
const example=`ID;Latitude;Longitude;Altitude
Wpt2;-21,805788350;-48,577717250;483,500
Wpt3;-21,804207333;-48,578225967;491,600
Wpt4;-21,806469567;-48,581631217;471,500
Wpt5;-21,808029567;-48,579311833;469,100
Wpt7;-21,807138400;-48,578040967;475,600
Wpt8;-21,809379883;-48,576611550;463,300
MB;-21,808577433;-48,575766867;460,900`;
function gnssRows(text){
 const rows=[];let row=[],field='',quoted=false;
 for(let i=0;i<text.length;i++){const c=text[i];if(c==='"'){if(quoted&&text[i+1]==='"'){field+='"';i++;}else quoted=!quoted;}else if(c===','&&!quoted){row.push(field);field='';}else if((c==='\n'||c==='\r')&&!quoted){if(c==='\r'&&text[i+1]==='\n')i++;row.push(field);if(row.some(v=>v.trim()))rows.push(row);row=[];field='';}else field+=c;}
 if(quoted)throw Error('CSV GNSS com aspas não fechadas.');row.push(field);if(row.some(v=>v.trim()))rows.push(row);return rows;
}
function normalizeGnss(text){
 const clean=text.replace(/^\uFEFF/,'').trim();
 if(!/^"?Name"?\s*,/i.test(clean))return null;
 const rows=gnssRows(clean),header=rows.shift().map(v=>v.trim().toLowerCase());
 const idx=['name','latitude','longitude','altitude'].map(k=>header.indexOf(k));
 if(idx.slice(0,3).some(i=>i<0))throw Error('CSV GNSS precisa das colunas Name, Latitude e Longitude.');
 return rows.map((r,i)=>{if(r.length!==header.length)throw Error('Registro GNSS '+(i+1)+': número de colunas diferente do cabeçalho.');const c=idx.map(j=>j<0?'':r[j].trim());if(/[;\r\n\t]/.test(c[0]))throw Error('Registro GNSS '+(i+1)+': nome contém separador ou quebra de linha.');return c.join(';');}).join('\n');
}
function parse(text){
 const normalized=normalizeGnss(text);if(normalized!==null)text=normalized;
 const lines=text.replace(/^\uFEFF/,'').split(/\r?\n/);const out=[],ids=new Set();
 const number=(s)=>{if(!/^[+-]?(?:\d+(?:[.,]\d*)?|[.,]\d+)$/.test(s))throw Error('Número inválido: '+s);const n=Number(s.replace(',','.'));if(!Number.isFinite(n))throw Error('Número fora do limite.');return n;};
 for(let i=0;i<lines.length;i++){
  const line=lines[i].trim();if(!line)continue;const cols=line.split(line.includes(';')?';':line.includes('\t')?'\t':/\s+/).map(s=>s.trim());
  if(!out.length&&cols[0].toUpperCase()==='ID'&&/^lat/i.test(cols[1]||''))continue;
  try{if(cols.length<3||cols.length>4||!cols[0])throw Error('Use ID; Latitude; Longitude; Altitude (opcional).');
   if(ids.has(cols[0]))throw Error('ID duplicado: '+cols[0]);
   const lat=number(cols[1]),lng=number(cols[2]),alt=cols[3]?number(cols[3]):null;
   const u=Sirgas.fromLatLng(lat,lng);out.push({id:cols[0],lat,lng,alt,...u});ids.add(cols[0]);
   if(out.length>10000)throw Error('Limite de 10.000 pontos.');
  }catch(e){throw Error('Linha '+(i+1)+': '+e.message);}
 }
 if(!out.length)throw Error('Informe pelo menos um ponto.');return out;
}
const fmt=(n,d)=>n===null?'':n.toFixed(d).replace('.',',');
const values=p=>[p.id,fmt(p.lat,9),fmt(p.lng,9),fmt(p.alt,3),fmt(p.easting,3),fmt(p.northing,3),String(p.zone),p.hemisphere];
function invalidate(){results=[];el('convertRows').replaceChildren();el('convertDownload').disabled=true;el('convertMetashape').disabled=true;el('convertStatus').className='';el('convertStatus').textContent='Dados alterados. Clique em Converter para UTM.';}
function run(){invalidate();try{results=parse(el('convertInput').value);for(const p of results){const tr=document.createElement('tr');for(const v of values(p)){const td=document.createElement('td');td.textContent=v;tr.append(td);}el('convertRows').append(tr);}el('convertDownload').disabled=false;el('convertMetashape').disabled=false;el('convertStatus').textContent=results.length+' pontos convertidos em SIRGAS 2000. Altitudes preservadas.'+(normalizeGnss(el('convertInput').value)!==null?' CSV GNSS reconhecido. O arquivo não informa o datum: o cálculo pressupõe entrada em SIRGAS 2000; não transforma WGS84 em SIRGAS 2000.':'');}catch(e){el('convertStatus').className='error';el('convertStatus').textContent=e.message;}}
function showConverter(show){el('planningPanel').hidden=show;el('converterPanel').hidden=!show;el('toggleSettings').hidden=show;el('converterTab').setAttribute('aria-pressed',String(show));el('planningTab').setAttribute('aria-pressed',String(!show));if(show)el('convertInput').focus();else window.dispatchEvent(new Event('resize'));}
el('converterTab').onclick=()=>showConverter(true);el('planningTab').onclick=()=>showConverter(false);
el('convertInput').oninput=invalidate;el('convertRun').onclick=run;el('convertExample').onclick=()=>{el('convertInput').value=example;run();};
el('convertFile').onchange=async()=>{const f=el('convertFile').files[0];if(!f)return;invalidate();try{if(f.size>3000000)throw Error('Arquivo maior que 3 MB.');el('convertInput').value=await f.text();run();}catch(e){el('convertStatus').textContent=e.message;el('convertStatus').className='error';}finally{el('convertFile').value='';}};
el('convertDownload').onclick=()=>{if(!results.length)return;const quote=v=>'"'+String(v).replace(/^[=+@-]/,"'$&").replaceAll('"','""')+'"';const rows=['ID;Latitude;Longitude;Altitude (m);Leste SIRGAS2000 (m);Norte SIRGAS2000 (m);Fuso;Hemisferio',...results.map(p=>values(p).map((v,i)=>i===0?quote(v):v).join(';'))];const url=URL.createObjectURL(new Blob(['\uFEFF'+rows.join('\r\n')],{type:'text/csv;charset=utf-8'}));const a=document.createElement('a');a.href=url;a.download='Coordenadas-SIRGAS2000-UTM.csv';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);};

function metashapeText(points){
 if(!points.length)throw Error('Converta os pontos primeiro.');
 if(points.some(p=>!Number.isFinite(p.alt)))throw Error('O TXT para Metashape exige altitude em todos os pontos. Complete as altitudes e converta novamente.');
 if(points.some(p=>/\s/.test(p.id)))throw Error('O formato separado por espaços exige nomes de pontos sem espaços. Ajuste os IDs e converta novamente.');
 if(new Set(points.map(p=>p.zone+p.hemisphere)).size!==1)throw Error('Os pontos estão em fusos ou hemisférios diferentes. Exporte um grupo por fuso e hemisfério.');
 const decimal=n=>String(Number(n.toFixed(3)));
 return ['ID Leste Norte Altitude',...points.map(p=>[p.id,decimal(p.easting),decimal(p.northing),decimal(p.alt)].join(' '))].join('\r\n')+'\r\n';
}
el('convertMetashape').onclick=()=>{try{const txt=metashapeText(results),url=URL.createObjectURL(new Blob([txt],{type:'text/plain;charset=utf-8'}));const a=document.createElement('a');a.href=url;a.download='Pontos-UTM-Metashape.txt';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);el('convertStatus').className='';el('convertStatus').textContent='TXT exportado: ID, Leste, Norte, Altitude. Referencial: SIRGAS 2000 / UTM fuso '+results[0].zone+' '+results[0].hemisphere+'. Use esse referencial na importação. Altitudes mantidas como informadas.';}catch(e){el('convertStatus').className='error';el('convertStatus').textContent=e.message;}};

if(typeof module!=='undefined')module.exports={parse,metashapeText};
})();
