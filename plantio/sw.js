// Service worker mínimo — só existe pra satisfazer o critério de "instalável" dos navegadores
// (Chrome/Edge) e cachear o "esqueleto" do app (o próprio HTML + ícones), pra abrir mais rápido
// e sobreviver a uma queda de conexão momentânea. NÃO tenta deixar o mapa/satélite offline —
// isso depende de rede (tiles ESRI/Google), fora do controle deste cache.
const CACHE = 'plantio-shell-v1';
const ASSETS = ['plantio3.html', 'manifest.json', 'icons/icon-192.png', 'icons/icon-512.png'];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(CACHE).then((c) => c.addAll(ASSETS)));
  self.skipWaiting();
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keys) => Promise.all(keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))))
  );
  self.clients.claim();
});

self.addEventListener('fetch', (e) => {
  if (e.request.method !== 'GET') return;
  e.respondWith(
    caches.match(e.request).then((cached) => cached || fetch(e.request).catch(() => cached))
  );
});
