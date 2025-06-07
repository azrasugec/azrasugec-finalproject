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

    logging.info(f"{origin_name} → {destination_name} | Mesafe: {distance_km} km | Harita: {filename}")

    return distance_km

def get_route_summary(origin_name, destination_name, csv_path):
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
    steps = len(route_coords)
    estimated_time_min = round((distance_km / 5) * 60)

    return {
        "distance_km": distance_km,
        "steps": steps,
        "estimated_time_min": estimated_time_min
    }

def calculate_multi_stop_route(stop_names, csv_path, filename="multi_map.html"):
    if len(stop_names) < 2:
        raise ValueError("En az iki durak gerekli.")

    coordinates = read_coordinates_from_csv(csv_path)
    for name in stop_names:
        if name not in coordinates:
            raise ValueError(f"{name} CSV'de bulunamadı.")

    G = ox.graph_from_place("Hacettepe Üniversitesi Beytepe Kampüsü, Ankara, Türkiye", network_type='walk')

    full_route = []
    total_distance = 0

    for i in range(len(stop_names) - 1):
        origin = coordinates[stop_names[i]]
        destination = coordinates[stop_names[i + 1]]

        orig_node = ox.distance.nearest_nodes(G, origin[1], origin[0])
        dest_node = ox.distance.nearest_nodes(G, destination[1], destination[0])

        route = nx.shortest_path(G, orig_node, dest_node, weight='length')
        route_coords = [(G.nodes[n]['y'], G.nodes[n]['x']) for n in route]

        if i != 0:
            route_coords = route_coords[1:]  # İlk düğüm zaten önceki rotada

        full_route.extend(route_coords)
        distance_km = sum(geodesic(route_coords[j], route_coords[j+1]).km for j in range(len(route_coords)-1))
        total_distance += distance_km

    # Harita çizimi
    m = folium.Map(location=coordinates[stop_names[0]], zoom_start=15)
    folium.PolyLine(full_route, color="purple", weight=5, opacity=0.7).add_to(m)

    for name in stop_names:
        folium.Marker(location=coordinates[name], popup=name).add_to(m)

    mid_point = full_route[len(full_route)//2]
    folium.Marker(mid_point, popup=f"{round(total_distance, 2)} km", icon=folium.Icon(color="green")).add_to(m)

    m.save(filename)

    logging.info(f"{' → '.join(stop_names)} | Toplam Mesafe: {round(total_distance, 2)} km | Harita: {filename}")

    return round(total_distance, 2)
