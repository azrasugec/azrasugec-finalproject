import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))

from sp211_2220674062.shortest_path import (
    calculate_shortest_path_and_map_from_names,
    calculate_multi_stop_route,
    get_route_summary,
    read_coordinates_from_csv,
    auto_correct_input
)


def main():
    csv_path = "coordinates.csv"
    locations = read_coordinates_from_csv(csv_path)
    valid_names = list(locations.keys())

    print("📍 Mevcut Lokasyonlar:")
    for loc in valid_names:
        print(f" - {loc}")

    user_input = input("\nLütfen güzergâhı girin (virgülle ayırarak, örn: A, B, C): ").strip()
    raw_points = [x.strip() for x in user_input.split(",")]

    corrected_points = []
    for name in raw_points:
        corrected, msg = auto_correct_input(name, valid_names)
        if corrected is None:
            print(f"❌ '{name}' tanınmadı ve düzeltilemedi.")
            return
        if msg:
            print(f"🔁 Düzeltilmiş: {msg}")
        corrected_points.append(corrected)

    if len(corrected_points) < 2:
        print("❌ En az iki geçerli nokta girilmelidir.")
        return

    try:
        if len(corrected_points) == 2:
            distance = calculate_shortest_path_and_map_from_names(
                corrected_points[0], corrected_points[1], csv_path
            )
            summary = get_route_summary(corrected_points[0], corrected_points[1], csv_path)
            print(f"\n✅ En kısa mesafe: {summary['distance_km']} km")
            print(f"👣 Adım sayısı: {summary['steps']}")
            print(f"⏱️ Tahmini süre: {summary['estimated_time_min']} dakika")
            print("🗺️ Harita 'map.html' olarak kaydedildi.")
        else:
            distance = calculate_multi_stop_route(corrected_points, csv_path)
            print(f"\n✅ Çok noktalı rota mesafesi: {distance} km")
            print("🗺️ Harita 'multi_map.html' olarak kaydedildi.")

    except ValueError as e:
        print(f"\n❌ Hata: {e}")

if __name__ == "__main__":
    main()
