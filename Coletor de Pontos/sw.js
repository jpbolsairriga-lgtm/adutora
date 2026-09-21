/* Service worker - app e mapa funcionam offline em campo */
var CACHE = "tophofarm-v13";
var TILES = "tiles-esri-v1";   /* mapa baixado pelo usuário; não é apagado nas atualizações */
var ARQS = ["./", "./index.html", "./manifest.json", "./icon.png", "./icon-maskable.png", "./logo.png", "./logo-splash.png",
  "./lib/leaflet.min.css", "./lib/leaflet.min.js", "./lib/jszip.min.js",
  "./lib/images/layers.png", "./lib/images/layers-2x.png", "./lib/images/marker-icon.png",
  "./lib/images/marker-icon-2x.png", "./lib/images/marker-shadow.png"];

self.addEventListener("install", function(e){
  self.skipWaiting();
  e.waitUntil(caches.open(CACHE).then(function(c){
    return Promise.all(ARQS.map(function(u){ return c.add(new Request(u,{cache:"reload"})).catch(function(){}); }));
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

  /* imagens de satélite: primeiro o que foi baixado, senão a rede */
  if(url.hostname==="server.arcgisonline.com"){
    e.respondWith(caches.open(TILES).then(function(c){
      return c.match(req.url).then(function(m){ return m||fetch(req); });
    }));
    return;
  }
  /* demais domínios: deixa passar */
  if(url.origin!==self.location.origin) return;

  /* arquivos do app: usa o guardado (rápido, funciona sem sinal) e atualiza em segundo plano */
  e.respondWith(caches.open(CACHE).then(function(c){
    return c.match(req).then(function(m){
      var rede=fetch(req).then(function(r){
        if(r&&r.ok) c.put(req,r.clone());
        return r;
      }).catch(function(){ return null; });
      if(m){ e.waitUntil(rede); return m; }
      return rede.then(function(r){ return r||c.match("./index.html"); });
    });
  }));
});
