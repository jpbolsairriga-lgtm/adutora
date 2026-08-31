// Service worker mínimo — só existe pra satisfazer o critério de "instalável" dos navegadores
// (Chrome/Edge) e cachear o "esqueleto" do app (o próprio HTML + ícones), pra abrir mais rápido
// e sobreviver a uma queda de conexão momentânea. NÃO tenta deixar o mapa/satélite offline —
// isso depende de rede (tiles ESRI/Google), fora do controle deste cache.
//
// v2: os HTML (plantio3/4.html) viraram network-first — o app muda com frequência (correções de
// bug saem em minutos) e a estratégia antiga (cache-first pra TODO GET, sem nunca popular esse
// cache com o HTML) deixava a porta aberta pro navegador servir uma versão desatualizada da
// lógica a partir do cache HTTP comum sem o usuário perceber, mesmo com hard refresh — o service
// worker intercepta o fetch antes da página, então quem manda na estratégia de cache é ele, não o
// Ctrl+F5. Ícones/manifest continuam cache-first (mudam raramente, ok servir rápido do cache).
const CACHE = 'plantio-shell-v2';
const ASSETS = ['plantio3.html', 'plantio4.html', 'manifest.json', 'icons/icon-192.png', 'icons/icon-512.png'];

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
  const isDoc = e.request.mode === 'navigate' || (e.request.headers.get('accept') || '').includes('text/html');
  if (isDoc) {
    // HTML sempre tenta a rede primeiro, ignorando qualquer cache HTTP (cache:'no-store') — só cai
    // pro cache salvo (versão anterior) se a rede falhar de verdade (offline).
    e.respondWith(
      fetch(e.request, { cache: 'no-store' })
        .then((resp) => { caches.open(CACHE).then((c) => c.put(e.request, resp.clone())); return resp; })
        .catch(() => caches.match(e.request))
    );
    return;
  }
  e.respondWith(
    caches.match(e.request).then((cached) => cached || fetch(e.request).then((resp) => {
      caches.open(CACHE).then((c) => c.put(e.request, resp.clone()));
      return resp;
    }).catch(() => cached))
  );
});
