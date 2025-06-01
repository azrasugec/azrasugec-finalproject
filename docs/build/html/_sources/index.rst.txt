.. Shortest Path Project - Azra Sugeç documentation master file, created by
   sphinx-quickstart on Sun Jun  1 23:41:36 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Shortest Path Project - Azra Sugeç documentation
================================================
Welcome to Shortest Path Project!
=================================

.. image:: https://img.shields.io/badge/Author-Azra%20Sugeç-purple
   :target: https://test.pypi.org/project/sp211-2220674062/0.0.1/
   :align: right


📍 **Shortest Path Project**, kullanıcıların harita üzerindeki noktalar arasında en kısa yürüme mesafesini hesaplamasını sağlayan bir Python paketidir. Hacettepe Üniversitesi Beytepe Kampüsü üzerinde test edilmiştir.

-----------------------------

📦 Kurulum
----------

.. code-block:: bash

   pip install --index-url https://test.pypi.org/simple/ --no-deps sp211-2220674062

-----------------------------

🚀 Kullanım Örneği
------------------

.. code-block:: python

   from sp211_2220674062.shortest_path import calculate_shortest_path_and_map_from_names

   distance = calculate_shortest_path_and_map_from_names(
       origin_name="Geomatik Mühendisliği",
       destination_name="Kütüphane",
       csv_path="coordinates.csv"
   )

   print(f"En kısa mesafe: {distance} km")

-----------------------------

🌐 Örnek Harita
------------------
Harita linki, seçilen noktalara göre dinamik olarak oluşur.
Örnek kullanımda şu şekilde görünebilir:

.. image:: https://img.shields.io/badge/Harita-Görüntüle-blue?logo=OpenStreetMap
   :target: https://www.openstreetmap.org/directions?engine=fossgis_osrm_walk&route=39.8657%2C32.7336%3B39.8708%2C32.7348


-----------------------------

📝 Notlar
------------------

- CSV dosyanızın şu şekilde olması gerekir:

.. code-block:: csv

   name,lat,lon
   Geomatik Mühendisliği,39.86570,32.73369
   Kütüphane,39.87081,32.73482

- Kullanıcı girişleri otomatik düzeltilir (örneğin `küütüphane` → `Kütüphane`).
- Rota `map.html` olarak kaydedilir.

-----------------------------

📚 İçindekiler

Add your content using ``reStructuredText`` syntax. See the
`reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
documentation for details.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   modules