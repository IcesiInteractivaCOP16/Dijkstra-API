from fastapi import Header, APIRouter
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from app.api.models import Ruta
import heapq

dijkstra = APIRouter()

@dijkstra.post('/path', status_code=200)
async def calculate_shortest_path(route: Ruta):
    initial = route.initial
    coordinates = route.coordinates
    final = route.final
    
    # create weights and adjacency list
    
    # Crear lista de adyacencia
    adjacency_list = {coord: [] for coord in coordinates}
    adjacency_list[initial] = []
    adjacency_list[final] = []

    all_points = [initial] + coordinates + [final]

    for coord in all_points:
        for adj in coord.adyacentes:
            distance = geodesic((coord.latitud, coord.longitud), (adj.latitud, adj.longitud)).kilometers
            adjacency_list[coord].append((adj, distance))

    # Implementar el algoritmo de Dijkstra
    def dijkstra_algorithm(start, goal):
        queue = [(0, start)]
        distances = {start: 0}
        previous_nodes = {start: None}
        
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            
            if current_node == goal:
                path = []
                while current_node is not None:
                    # Añadir solo las coordenadas (latitud, longitud) al camino
                    path.append((current_node.latitud, current_node.longitud))
                    current_node = previous_nodes[current_node]
                return path[::-1]  # Devolvemos el camino al revés, desde inicio a fin
            
            for neighbor, weight in adjacency_list.get(current_node, []):
                distance = current_distance + weight
                if distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(queue, (distance, neighbor))
        
        return None

    shortest_path = dijkstra_algorithm(initial, final)
    
    return {"shortest_path": shortest_path}