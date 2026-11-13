(function(root){
  'use strict';
  const SERVICE='https://ic.imagery1.arcgis.com/arcgis/rest/services/Sentinel2_10m_LandCover/ImageServer';
  const CLASSES=[1,2,4,5,7,8,9,10,11];
  const known=v=>CLASSES.includes(v)&&v!==10;
  const forest=v=>v===2;
  function request(g,buffer,year){
    const pad=buffer+25,sw=g.proj.from({x:g.minX-pad,y:g.minY-pad}),ne=g.proj.from({x:g.maxX+pad,y:g.maxY+pad});
    const width=Math.ceil((g.maxX-g.minX+2*pad)/10),height=Math.ceil((g.maxY-g.minY+2*pad)/10);
    if(width>4000||height>4000||width*height>2000000)throw Error('Área muito grande para a análise a 10 m no navegador. Divida o levantamento em áreas menores.');
    const params=new URLSearchParams({f:'json',bbox:[sw.lng,sw.lat,ne.lng,ne.lat].join(','),bboxSR:'4326',imageSR:'4326',size:width+','+height,format:'png32',interpolation:'RSP_NearestNeighbor',adjustAspectRatio:'false',time:Date.UTC(year,0,1)+','+(Date.UTC(year+1,0,1)-1),renderingRule:JSON.stringify({rasterFunction:'Colormap',rasterFunctionArguments:{Colormap:[0,...CLASSES].map(v=>[v,v,0,0])}})});
    return SERVICE+'/exportImage?'+params;
  }
  function decode(rgba,width,height,extent,g,year){
    if(!Number.isInteger(width)||!Number.isInteger(height)||width<1||height<1||width*height>2000000||rgba.length!==width*height*4)throw Error('Dimensões inválidas na classificação.');
    if((extent.spatialReference?.latestWkid||extent.spatialReference?.wkid)!==4326||![extent.xmin,extent.xmax,extent.ymin,extent.ymax].every(Number.isFinite)||extent.xmin>=extent.xmax||extent.ymin>=extent.ymax)throw Error('Referência espacial inválida na classificação.');
    const sw=g.proj.to({lng:extent.xmin,lat:extent.ymin}),ne=g.proj.to({lng:extent.xmax,lat:extent.ymax}),dx=(ne.x-sw.x)/width,dy=(ne.y-sw.y)/height;
    const cells=new Uint8Array(width*height);let valid=0,trees=0,insideCount=0,unknown=0;
    for(let i=0;i<cells.length;i++){
      const v=rgba[i*4];if(rgba[i*4+3]>0&&(rgba[i*4+1]!==0||rgba[i*4+2]!==0||(!CLASSES.includes(v)&&v!==0)))throw Error('O serviço retornou uma legenda inesperada. A análise foi interrompida.');
      cells[i]=rgba[i*4+3]===255?v:0;
      if(root.Planner.inside({x:sw.x+(i%width+.5)*dx,y:ne.y-(Math.floor(i/width)+.5)*dy},g.xy)){insideCount++;if(known(cells[i]))valid++;else unknown++;if(forest(cells[i]))trees++;}
    }
    if(!valid)throw Error('Não há classificação válida dentro da área para este ano. Tente outro ano ou uma área maior.');
    return{width,height,extent,sw,ne,dx,dy,cells,year,trees,unknown,insideCount,coverage:valid/insideCount};
  }
  function blocked(p,r,buffer){
    const col=Math.floor((p.x-r.sw.x)/r.dx),row=Math.floor((r.ne.y-p.y)/r.dy);
    if(col<0||row<0||col>=r.width||row>=r.height)return true;
    const rx=Math.ceil(buffer/r.dx)+1,ry=Math.ceil(buffer/r.dy)+1;
    // Unknown and cloud pixels are treated conservatively, including the same setback.
    for(let y=Math.max(0,row-ry);y<=Math.min(r.height-1,row+ry);y++)for(let x=Math.max(0,col-rx);x<=Math.min(r.width-1,col+rx);x++){
      const v=r.cells[y*r.width+x];if(!forest(v)&&known(v))continue;
      const left=r.sw.x+x*r.dx,right=left+r.dx,top=r.ne.y-y*r.dy,bottom=top-r.dy;
      const dx=Math.max(left-p.x,0,p.x-right),dy=Math.max(bottom-p.y,0,p.y-top);
      if(Math.hypot(dx,dy)<=buffer+1e-8)return true;
    }
    return false;
  }
  function manualBlocked(p,polygons,buffer){return polygons.some(r=>root.Planner.inside(p,r)||r.some((a,i)=>root.Planner.segment(p,a,r[(i+1)%r.length])<=buffer));}
  async function json(url,signal){const res=await fetch(url,{signal,credentials:'omit'});if(!res.ok)throw Error('Serviço de vegetação indisponível (HTTP '+res.status+').');const data=await res.json();if(data.error)throw Error('Serviço de vegetação: '+data.error.message);return data;}
  async function load(g,buffer,requestedYear){
    const abort=new AbortController(),timer=setTimeout(()=>abort.abort(),45000);
    try{
      const meta=await json(SERVICE+'?f=json',abort.signal),times=meta.timeInfo?.timeExtent;
      if(!times||!Number.isFinite(times[1]))throw Error('Não foi possível verificar o ano da classificação.');
      const latest=new Date(times[1]).getUTCFullYear(),first=new Date(times[0]).getUTCFullYear(),year=requestedYear==='latest'?latest:Number(requestedYear);
      if(!Number.isInteger(year)||year<first||year>latest)throw Error('Ano não disponível. A fonte oferece '+first+' a '+latest+'.');
      const info=await json(request(g,buffer,year),abort.signal);
      if(!info.href||!info.extent)throw Error('O serviço não retornou uma classificação georreferenciada.');
      const url=new URL(info.href);if(url.origin!==new URL(SERVICE).origin||!url.pathname.startsWith('/arcgis/rest/directories/arcgisoutput/'))throw Error('Endereço inesperado na resposta de vegetação.');
      const response=await fetch(url,{signal:abort.signal,credentials:'omit'});if(!response.ok)throw Error('Falha ao baixar a classificação.');
      const bitmap=await createImageBitmap(await response.blob(),{colorSpaceConversion:'none',premultiplyAlpha:'none'});
      try{if(bitmap.width!==info.width||bitmap.height!==info.height)throw Error('Dimensões divergentes na classificação.');const canvas=document.createElement('canvas');canvas.width=bitmap.width;canvas.height=bitmap.height;const ctx=canvas.getContext('2d',{willReadFrequently:true});ctx.drawImage(bitmap,0,0);return decode(ctx.getImageData(0,0,canvas.width,canvas.height).data,canvas.width,canvas.height,info.extent,g,year);}finally{bitmap.close();}
    }catch(e){if(e.name==='AbortError')throw Error('A consulta de vegetação excedeu 45 segundos. Tente novamente.');if(e instanceof TypeError)throw Error('Não foi possível acessar a classificação. Confira a conexão; os pontos não serão gerados sem análise.');throw e;}finally{clearTimeout(timer);}
  }
  function overlay(r){const canvas=document.createElement('canvas');canvas.width=r.width;canvas.height=r.height;const ctx=canvas.getContext('2d'),im=ctx.createImageData(r.width,r.height);for(let i=0;i<r.cells.length;i++){let color=forest(r.cells[i])?[10,83,48,175]:!known(r.cells[i])?[90,99,110,155]:[0,0,0,0];im.data.set(color,i*4);}ctx.putImageData(im,0,0);return canvas.toDataURL('image/png');}
  const api={SERVICE,request,decode,blocked,manualBlocked,load,overlay,known,forest};root.Forest=api;if(typeof module!=='undefined')module.exports=api;
})(globalThis);
