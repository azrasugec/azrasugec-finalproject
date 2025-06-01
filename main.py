from sp211_2220674062.shortest_path import (
    calculate_shortest_path_and_map_from_names,
    read_coordinates_from_csv,
    auto_correct_input
)

def main():
    csv_path = "coordinates.csv"
    locations = read_coordinates_from_csv(csv_path)
    valid_names = list(locations.keys())

    print("📍 Kullanılabilir Noktalar:")
    for loc in valid_names:
        print(f" - {loc}")

    origin_input = input("\nBaşlangıç noktasını yazınız: ").strip()
    destination_input = input("Varış noktasını yazınız: ").strip()

    origin, origin_msg = auto_correct_input(origin_input, valid_names)
    destination, dest_msg = auto_correct_input(destination_input, valid_names)

    if origin_msg:
        print(f"🔁 Başlangıç düzeltildi: {origin_msg}")
    if dest_msg:
        print(f"🔁 Varış düzeltildi: {dest_msg}")

    if origin is None or destination is None:
        print("❌ Hata: Girdiğiniz isim(ler) bulunamadı ve düzeltilemedi.")
        return

    try:
        distance = calculate_shortest_path_and_map_from_names(origin, destination, csv_path)
        print(f"\n✅ En kısa mesafe: {distance} km")
        print("🗺️ Harita 'map.html' olarak kaydedildi.")
    except ValueError as e:
        print(f"\n❌ Hata: {e}")

if __name__ == "__main__":
    main()
