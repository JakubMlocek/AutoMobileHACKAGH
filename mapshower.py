import osmnx as ox
import networkx as nx
import folium
import time

# pobieramy graf drogowy dla Katowic i Sosnowca
place_name = ['Katowice', 'Sosnowiec']
G = ox.graph_from_place(place_name, network_type='drive')

# znajdujemy najkrótszą trasę między dwoma punktami
origin_point = (50.2599, 19.0228)  # punkt startowy
destination_point = (50.2860, 19.1033)  # punkt końcowy
origin_node = ox.distance.nearest_nodes(G, origin_point[1], origin_point[0])
destination_node = ox.distance.nearest_nodes(G, destination_point[1], destination_point[0])
route = nx.shortest_path(G, origin_node, destination_node)

# tworzymy mapę i dodajemy na niej trasę
map_center = [50.2738, 19.0546]  # środek trasy
my_map = folium.Map(location=map_center, zoom_start=12)
folium.PolyLine(locations=[(G.nodes[node]['y'], G.nodes[node]['x']) for node in route]).add_to(my_map)

# tworzymy marker i ustawiamy go na pozycji początkowej
marker = folium.Marker(location=origin_point, icon=folium.Icon(color='red'))
marker.add_to(my_map)

my_map.save("map.html")

# przesuwamy marker po trasie
for node in route:
    point = (G.nodes[node]['y'], G.nodes[node]['x'])  # pobieramy współrzędne wierzchołka
    marker.location = point  # ustawiamy marker na aktualnej pozycji
    time.sleep(0.1)  # opóźniamy animację
