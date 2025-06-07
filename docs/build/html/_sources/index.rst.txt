.. Shortest Path Project - Azra Sugeç documentation master file, created by
   sphinx-quickstart on Sun Jun  1 23:41:36 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Shortest Path Project - Azra Sugeç
==================================

Welcome to the official documentation for the **Shortest Path Project**, a Python package that calculates the shortest walking route between locations using OpenStreetMap (OSM) data. It was developed and tested on Hacettepe University's Beytepe Campus.

.. image:: https://img.shields.io/badge/Author-Azra%20Sugeç-purple
   :target: https://test.pypi.org/project/sp211-2220674062/
   :align: right

-----------------------------

📦 Installation
-----------------------------

You can install the latest version of the package from **TestPyPI** using the following command:

.. code-block:: bash

   pip install -i https://test.pypi.org/simple/ sp211-2220674062


-----------------------------

🚀 Basic Usage
-----------------------------

.. code-block:: python

   from sp211_2220674062.shortest_path import calculate_shortest_path_and_map_from_names

   distance = calculate_shortest_path_and_map_from_names(
       origin_name="Geomatik Mühendisliği",
       destination_name="Kütüphane",
       csv_path="coordinates.csv"
   )

   print(f"En kısa mesafe: {distance} km")

-----------------------------

✨ New Features (Phase 2)
-----------------------------

- `get_route_summary(origin, destination, csv_path)`  
  → Returns total distance, number of steps, and estimated walking time.
  
- `calculate_multi_stop_route([A, B, C], csv_path)`  
  → Calculates a route that passes through multiple user-defined stops in order.

- `main.py` CLI updated to support multi-stop input and return summary results.

- CI/CD pipeline set up via GitHub Actions.

-----------------------------

🌐 Example Route Map
-----------------------------

The OpenStreetMap route is dynamically generated between selected coordinates.

In the example below, the path goes from **Geomatik Mühendisliği** to **Kütüphane**:

.. image:: https://img.shields.io/badge/Harita-Görüntüle-blue?logo=OpenStreetMap
   :target: https://www.openstreetmap.org/directions?engine=fossgis_osrm_walk&route=39.8657%2C32.73369%3B39.87081%2C32.73482

-----------------------------

📁 CSV Format Example
-----------------------------

The routing system uses a CSV file with real latitude/longitude pairs.  
Below is an actual sample from this project:

.. code-block:: csv

   name,lat,lon
   Geomatik Mühendisliği,39.86570,32.73369
   Kütüphane,39.87081,32.73482
   YDYO,39.86905,32.73200
   Rektörlük,39.86660,32.73540
   Öğrenci Evleri,39.86800,32.73620
   Yemekhane,39.86850,32.73590


-----------------------------

🤖 AI-Based Input Handling
-----------------------------

- User input is auto-corrected using `difflib.get_close_matches()`
- Prevents route calculation errors due to typos or casing issues  
  (e.g., `"küütüphane"` → `"Kütüphane"`)

-----------------------------

🧪 Testing & CI
-----------------------------

- Unit tests are written using `pytest`
- Tests are automatically triggered via GitHub Actions on each push
- Code coverage includes routing, summaries, and map generation

-----------------------------

📚 Contents

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   usage
   modules
   advanced_usage
