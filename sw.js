/* Course Tracker by The Altitude Mindset — service worker */
const CACHE = 'course-tracker-v17';

const ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './icon-192.png',
  './icon-512.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE)
      .then((cache) => cache.addAll(ASSETS))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(
        keys.filter((k) => k !== CACHE).map((k) => caches.delete(k))
      ))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;

  const url = new URL(req.url);
  if (url.origin !== self.location.origin) return;

  /* Navigations are network-first.
     Cache-first here meant a deployed fix only reached installed users if I
     remembered to bump CACHE — one forgotten bump and everyone is frozen on an
     old build with no way to tell. Going to the network first costs a moment
     on launch when online and removes that whole failure mode; the cache still
     answers instantly when there is no connection. */
  if (req.mode === 'navigate') {
    event.respondWith(
      fetch(req)
        .then((res) => {
          /* Store under the REQUEST's own key, never a fixed './index.html'.
             Writing every navigation to that one key meant visiting any other
             page in scope — demo.html, say — overwrote the cached app shell,
             so the next offline launch of the app served that other page
             instead. Keyed by request, each page caches as itself. */
          const copy = res.clone();
          caches.open(CACHE).then((c) => c.put(req, copy)).catch(() => {});
          return res;
        })
        .catch(() => caches.match(req, { ignoreSearch: true })
          .then((hit) => hit || caches.match('./index.html', { ignoreSearch: true }))
          .then((hit) => hit || caches.match('./', { ignoreSearch: true })))
    );
    return;
  }

  /* Everything else — icons, manifest — is cache-first. These change rarely and
     are worth having instantly offline. */
  event.respondWith(
    caches.match(req, { ignoreSearch: true }).then((hit) => {
      if (hit) return hit;
      return fetch(req)
        .then((res) => {
          if (res && res.ok && res.type === 'basic') {
            const copy = res.clone();
            caches.open(CACHE).then((c) => c.put(req, copy)).catch(() => {});
          }
          return res;
        })
        .catch(() => Response.error());
    })
  );
});
