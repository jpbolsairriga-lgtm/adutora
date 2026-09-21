/* Service worker - cache do app para uso offline em campo */
var CACHE = "pontos-gps-v4";
var ARQS = ["./", "./index.html", "./manifest.json", "./icon.png", "./icon-maskable.png", "./logo.png",
  "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.css",
  "https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.9.4/leaflet.min.js"];

self.addEventListener("install", function(e){
  self.skipWaiting();
  e.waitUntil(caches.open(CACHE).then(function(c){ return Promise.all(ARQS.map(function(u){return c.add(u).catch(function(){});})); }));
});

self.addEventListener("activate", function(e){
  e.waitUntil(caches.keys().then(function(ks){
    return Promise.all(ks.map(function(k){ return k===CACHE?null:caches.delete(k); }));
  }).then(function(){ return self.clients.claim(); }));
});

self.addEventListener("fetch", function(e){
  if(e.request.method!=="GET") return;
  e.respondWith(
    fetch(e.request).then(function(r){
      var copia = r.clone();
      caches.open(CACHE).then(function(c){ c.put(e.request, copia).catch(function(){}); });
      return r;
    }).catch(function(){
      return caches.match(e.request).then(function(m){
        return m || caches.match("./index.html");
      });
    })
  );
});
