# MapIntegration.py

import folium

def generate_map(location, zoom_start=12):
    m = folium.Map(location=location, zoom_start=zoom_start)
    return m

def add_marker(map_obj, location, popup=None):
    folium.Marker(location=location, popup=popup).add_to(map_obj)

if __name__ == "__main__":
    loc = [40.7128, -74.0060]  # Example location (New York City)
    map_obj = generate_map(loc)
    add_marker(map_obj, loc, "New York City")
    map_obj.save("map.html")
