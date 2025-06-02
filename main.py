from sp211_2220674062.shortest_path import (
    calculate_shortest_path_and_map_from_names,
    read_coordinates_from_csv,
    auto_correct_input
)

def main():
    csv_path = "coordinates.csv"
    locations = read_coordinates_from_csv(csv_path)
    valid_names = list(locations.keys())

    print("📍 Available Locations:")
    for loc in valid_names:
        print(f" - {loc}")

    origin_input = input("\nEnter starting location: ").strip()
    destination_input = input("Enter destination location: ").strip()

    origin, origin_msg = auto_correct_input(origin_input, valid_names)
    destination, dest_msg = auto_correct_input(destination_input, valid_names)

    if origin_msg:
        print(f"🔁 Start corrected: {origin_msg}")
    if dest_msg:
        print(f"🔁 Destination corrected: {dest_msg}")

    if origin is None or destination is None:
        print("❌ Error: Could not interpret input.")
        return

    try:
        distance = calculate_shortest_path_and_map_from_names(origin, destination, csv_path)
        print(f"\n✅ Shortest distance: {distance} km")
        print("🗺️ Map saved as 'map.html'")
    except ValueError as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
