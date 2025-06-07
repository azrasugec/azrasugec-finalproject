import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from sp211_2220674062.shortest_path import (
    calculate_shortest_path_and_map_from_names,
    get_route_summary,
    calculate_multi_stop_route
)


def test_shortest_path_and_map_generation():
    origin = "Geomatik Mühendisliği"
    destination = "Kütüphane"
    csv_file = "coordinates.csv"
    output_file = "test_map.html"

    distance = calculate_shortest_path_and_map_from_names(origin, destination, csv_file, filename=output_file)

    assert distance > 0
    assert os.path.exists(output_file)

    os.remove(output_file)

def test_get_route_summary_keys():
    csv_file = "coordinates.csv"
    summary = get_route_summary("Kütüphane", "Yemekhane", csv_file)

    assert isinstance(summary, dict)
    assert "distance_km" in summary
    assert "steps" in summary
    assert "estimated_time_min" in summary
    assert summary["distance_km"] > 0
    assert summary["steps"] > 0

def test_multi_stop_route_generation():
    csv_file = "coordinates.csv"
    output_file = "multi_test_map.html"
    stops = ["Geomatik Mühendisliği", "Kütüphane", "Yemekhane"]

    distance = calculate_multi_stop_route(stops, csv_file, filename=output_file)

    assert distance > 0
    assert os.path.exists(output_file)

    os.remove(output_file)
