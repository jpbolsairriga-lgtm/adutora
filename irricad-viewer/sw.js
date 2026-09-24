/* Service worker - app e projetos abertos funcionam offline em campo */
var CACHE = "irricad-viewer-v3";
var TILES = "tiles-esri-v1"; /* imagens de satelite ja vistas; nao apaga nas atualizacoes */
var ARQS = ["./", "./irricad-viewer.html", "./manifest.json", "./icon-192.png", "./icon-512.png", "./icon-maskable.png",
  "./tophofarm-simbolo.png", "./tophofarm-logo-completo.png", "./irricad-logo.png",
  "https://unpkg.com/leaflet@1.9.4/dist/leaflet.css",
  "https://unpkg.com/leaflet@1.9.4/dist/leaflet-src.js",
  "https://unpkg.com/leaflet-rotate@0.2.8/dist/leaflet-rotate-src.js",
  "https://cdnjs.cloudflare.com/ajax/libs/jszip/3.10.1/jszip.min.js"];

self.addEventListener("install", function(e){
  self.skipWaiting();
  e.waitUntil(caches.open(CACHE).then(function(c){
    return Promise.all(ARQS.map(function(u){ return c.add(new Request(u,{mode:"cors"})).catch(function(){}); }));
  }));
});

self.addEventListener("activate", function(e){
  e.waitUntil(caches.keys().then(function(ks){
    return Promise.all(ks.map(function(k){ return (k===CACHE||k===TILES)?null:caches.delete(k); }));
  }).then(function(){ return self.clients.claim(); }));
});

self.addEventListener("fetch", function(e){
  var req=e.request;
  if(req.method!=="GET") return;
  var url=new URL(req.url);

  /* imagens de satelite: usa o que ja foi visto em campo, senao busca na rede */
  if(/arcgisonline\.com|maptiles\.arcgis\.com/.test(url.hostname)){
    e.respondWith(caches.open(TILES).then(function(c){
      return c.match(req.url).then(function(m){
        if(m) return m;
        return fetch(req).then(function(r){ if(r&&r.ok) c.put(req,r.clone()); return r; }).catch(function(){ return m; });
      });
    }));
    return;
  }

  /* mapa de ruas (OSM) e bibliotecas CDN: cache-first, atualiza em segundo plano */
  e.respondWith(caches.open(CACHE).then(function(c){
    return c.match(req).then(function(m){
      var rede=fetch(req).then(function(r){
        if(r&&r.ok) c.put(req,r.clone());
        return r;
      }).catch(function(){ return null; });
      if(m){ e.waitUntil(rede); return m; }
      return rede.then(function(r){ return r||(url.origin===self.location.origin ? c.match("./irricad-viewer.html") : undefined); });
    });
  }));
});
