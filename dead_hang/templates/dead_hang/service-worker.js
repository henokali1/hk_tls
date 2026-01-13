{% load static %}
const CACHE_NAME = 'dead-hang-v1';
const ASSETS = [
  '/',
  '{% url "dead_hang:stats" %}',
  '{% url "dead_hang:manifest" %}',
  '{% static "dead_hang/icon-192.png" %}',
  'https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap',
  'https://cdn.jsdelivr.net/npm/chart.js'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(ASSETS))
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => response || fetch(event.request))
  );
});
