import osmnx as ox
import networkx as nx
from geopy.distance import geodesic
import folium
import csv
import logging
import os
from difflib import get_close_matches

# logs klasörü yoksa oluştur
if not os.path.exists("logs"):
    os.makedirs("logs")

# Logging ayarları
logging.basicConfig(
    filename="logs/log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def read_coordinates_from_csv(csv_path):
    locations = {}
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            locations[row['name']] = (float(row['lat']), float(row['lon']))
    return locations

def auto_correct_input(input_name, valid_names):
    for name in valid_names:
        if name.lower() == input_name.lower():
            return name, None  # Doğrudan eşleşti
    suggestion = get_close_matches(input_name, valid_names, n=1, cutoff=0.6)
    if suggestion:
        return suggestion[0], f"{input_name} → {suggestion[0]}"
    else:
        return None, f"{input_name} tanınmadı ve düzeltilemedi."

def calculate_shortest_path_and_map_from_names(origin_name, destination_name, csv_path, filename="map.html"):
    coordinates = read_coordinates_from_csv(csv_path)

    if origin_name not in coordinates or destination_name not in coordinates:
        raise ValueError("Seçilen isimler CSV'de bulunamadı.")

    origin = coordinates[origin_name]
    destination = coordinates[destination_name]

    G = ox.graph_from_place("Hacettepe Üniversitesi Beytepe Kampüsü, Ankara, Türkiye", network_type='walk')

    orig_node = ox.distance.nearest_nodes(G, origin[1], origin[0])
    dest_node = ox.distance.nearest_nodes(G, destination[1], destination[0])

    route = nx.shortest_path(G, orig_node, dest_node, weight='length')
    route_coords = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in route]

    distance_km = round(sum(geodesic(route_coords[i], route_coords[i+1]).km for i in range(len(route_coords)-1)), 2)

    # Harita oluştur
    m = folium.Map(location=origin, zoom_start=15)
    folium.PolyLine(route_coords, color="blue", weight=5, opacity=0.7).add_to(m)
    folium.Marker(location=origin, popup=origin_name).add_to(m)
    folium.Marker(location=destination, popup=destination_name).add_to(m)
    mid_point = route_coords[len(route_coords)//2]
    folium.Marker(mid_point, popup=f"{distance_km} km", icon=folium.Icon(color="green")).add_to(m)

    # OSM bağlantısını yazdır
    osm_url = f"https://www.openstreetmap.org/directions?engine=fossgis_osrm_walk&route={origin[0]}%2C{origin[1]}%3B{destination[0]}%2C{destination[1]}"
    print("🧭 Harita bağlantısı:", osm_url)

    m.save(filename)

    # Logla
    logging.info(f"{origin_name} → {destination_name} | Mesafe: {distance_km} km | Harita: {filename}")

    return distance_km
