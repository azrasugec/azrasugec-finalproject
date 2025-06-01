import os
from sp211_2220674062.shortest_path import calculate_shortest_path_and_map_from_names

def test_shortest_path_and_map_generation():
    origin = "Geomatik Mühendisliği"
    destination = "Kütüphane"
    csv_file = "coordinates.csv"
    output_file = "test_map.html"

    # Fonksiyonu çağır
    distance = calculate_shortest_path_and_map_from_names(origin, destination, csv_file, filename=output_file)

    # Mesafe pozitif olmalı
    assert distance > 0

    # Harita dosyası oluşturulmuş olmalı
    assert os.path.exists(output_file)

    # Testten sonra dosyayı sil
    os.remove(output_file)
