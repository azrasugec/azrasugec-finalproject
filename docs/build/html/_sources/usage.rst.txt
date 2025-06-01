Kütüphane Kullanım Mantığı
===========================

Bu Python paketi, kullanıcıdan alınan başlangıç ve varış noktalarına göre
Hacettepe Üniversitesi Beytepe Kampüsü'nde en kısa yürüyüş yolunu hesaplar
ve bir harita oluşturur.

Adım Adım Nasıl Çalışır?
-------------------------

1. Kullanıcı `main.py` aracılığıyla başlangıç ve varış noktası girer.
2. Bu noktaların koordinatları `coordinates.csv` dosyasından alınır.
3. Noktalar OpenStreetMap (OSM) üzerinde en yakın düğümlere eşlenir.
4. `osmnx` ile kampüsün yürüme ağı (`network_type='walk'`) çıkarılır.
5. `networkx` ile Dijkstra algoritmasıyla en kısa yol bulunur.
6. Harita `folium` ile çizilir ve `map.html` olarak kaydedilir.
7. Terminalde ayrıca gerçek OSM linki gösterilir.
8. Yapılan işlem `logs/log.txt` dosyasına kaydedilir.

Dinamik Özellikler
-------------------

- Kullanıcı yanlış isim girerse sistem düzeltme önerisi sunar.
  Örn: `küütüphane → Kütüphane`


Gereken Dosyalar
------------------

- `coordinates.csv` — Konum isimleri ve koordinatlarını içerir.
- `main.py` — Paketin örnek kullanım arayüzüdür.
- `shortest_path.py` — Asıl algoritmaların bulunduğu modüldür.

