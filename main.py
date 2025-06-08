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

    print("📍 Available Locations:")
    for loc in valid_names:
        print(f" - {loc}")

    user_input = input("\nEnter your route (comma-separated, e.g., A, B, C): ").strip()
    raw_points = [x.strip() for x in user_input.split(",")]

    corrected_points = []
    for name in raw_points:
        corrected, msg = auto_correct_input(name, valid_names)
        if corrected is None:
            print(f"❌ '{name}' could not be recognized or corrected.")
            return
        if msg:
            print(f"🔁 Corrected: {msg}")
        corrected_points.append(corrected)

    if len(corrected_points) < 2:
        print("❌ You must enter at least two valid locations.")
        return

    try:
        if len(corrected_points) == 2:
            distance = calculate_shortest_path_and_map_from_names(
                corrected_points[0], corrected_points[1], csv_path
            )
            summary = get_route_summary(corrected_points[0], corrected_points[1], csv_path)
            print(f"\n✅ Distance: {summary['distance_km']} km")
            print(f"👣 Steps: {summary['steps']}")
            print(f"⏱️ Estimated time: {summary['estimated_time_min']} minutes")
            print("🗺️ Map saved as 'map.html'")
        else:
            distance = calculate_multi_stop_route(corrected_points, csv_path)
            print(f"\n✅ Multi-stop route distance: {distance} km")
            print("🗺️ Map saved as 'multi_map.html'")

    except ValueError as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()
