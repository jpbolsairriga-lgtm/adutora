(function(root){
'use strict';
function fromLatLng(lat,lng){
 if(!Number.isFinite(lat)||!Number.isFinite(lng)||lat < -80||lat >84||lng < -180||lng>180)throw Error('Coordenadas fora do domínio UTM.');
 let zone=Math.min(60,Math.floor((lng+180)/6)+1);
 if(lat>=56&&lat<64&&lng>=3&&lng<12)zone=32;
 if(lat>=72&&lat<84&&lng>=0&&lng<42)zone=lng<9?31:lng<21?33:lng<33?35:37;
 const d=Math.PI/180,a=6378137,f=1/298.257222101,e2=f*(2-f),ep=e2/(1-e2),phi=lat*d,lam=lng*d,lam0=((zone-1)*6-177)*d;
 const s=Math.sin(phi),c=Math.cos(phi),t=Math.tan(phi),N=a/Math.sqrt(1-e2*s*s),T=t*t,C=ep*c*c,A=c*(lam-lam0);
 const M=a*((1-e2/4-3*e2**2/64-5*e2**3/256)*phi-(3*e2/8+3*e2**2/32+45*e2**3/1024)*Math.sin(2*phi)+(15*e2**2/256+45*e2**3/1024)*Math.sin(4*phi)-35*e2**3/3072*Math.sin(6*phi));
 const easting=500000+.9996*N*(A+(1-T+C)*A**3/6+(5-18*T+T*T+72*C-58*ep)*A**5/120);
 const northing=.9996*(M+N*t*(A*A/2+(5-T+9*C+4*C*C)*A**4/24+(61-58*T+T*T+600*C-330*ep)*A**6/720))+(lat<0?10000000:0);
 return{zone,hemisphere:lat<0?'S':'N',easting,northing,datum:'SIRGAS 2000'};
}
root.Sirgas={fromLatLng};if(typeof module!=='undefined')module.exports=root.Sirgas;
})(globalThis);