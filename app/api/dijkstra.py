from fastapi import APIRouter, HTTPException
from geopy.distance import geodesic
import heapq
from app.api.models import PathRequest

dijkstra = APIRouter()


graph = {
    "Universidad ICESI": {
        "latitud": 3.342076976663357,
        "longitud": -76.53063419139824,
        "adyacentes": [
            "Universidad del Valle",
            "Fundación Universitaria San Martín"
        ]
    },
    "Bulevar del Río": {
        "latitud": 3.4528374462960167,
        "longitud": -76.5347951337262,
        "adyacentes": [
            "Biblioteca del Centenario",
            "Biblioteca Departamental Jorge Garcés Borrero"
        ]
    },
    "Universidad del Valle": {
        "latitud": 3.376762549737823,
        "longitud": -76.52159697790536,
        "adyacentes": [
            "Universidad ICESI",
            "Unidad Deportiva Alberto Galindo"
        ]
    },
    "Fundación Universitaria San Martín": {
        "latitud": 3.418830555134766,
        "longitud": -76.53472029139806,
        "adyacentes": [
            "Universidad ICESI",
            "Universidad del Valle"
        ]
    },
    "Biblioteca del Centenario": {
        "latitud": 3.4509470750225484,
        "longitud": -76.5436671910903,
        "adyacentes": [
            "Biblioteca Departamental Jorge Garcés Borrero",
            "Bulevar del Río"
        ]
    },
    "Polideportivo Los Almendros": {
        "latitud": 3.4710467990599017,
        "longitud": -76.49330558817636,
        "adyacentes": [
            "Bulevar de Oriente",
            "Bulevar del Río"
        ]
    },
    "Unidad Deportiva Alberto Galindo": {
        "latitud": 3.412247224167538,
        "longitud": -76.5508290067407,
        "adyacentes": [
            "Universidad del Valle",
            "Instituto Humboldt"
        ]
    },
    "Bulevar de Oriente": {
        "latitud": 3.4271549432353434,
        "longitud": -76.48409539801399,
        "adyacentes": [
            "Universidad del Valle",
            "Polideportivo Los Almendros"
        ]
    },
    "Biblioteca Departamental Jorge Garcés Borrero": {
        "latitud": 3.436426530173853,
        "longitud": -76.53922341838341,
        "adyacentes": [
            "Instituto Humboldt",
            "Bulevar del Río"
        ]
    },
    "Instituto Humboldt": {
        "latitud": 3.429120017986491,
        "longitud": -76.54139602023353,
        "adyacentes": [
            "Unidad Deportiva Alberto Galindo",
            "Biblioteca Departamental Jorge Garcés Borrero"
        ]
    }
}

@dijkstra.post('/path', status_code=200)
async def calculate_shortest_path(path_request: PathRequest):
    if path_request.source not in graph or path_request.destination not in graph:
        raise HTTPException(status_code=404, detail="Source or destination not found in the graph")
    
    
    adjacency_list = {}
    for node, data in graph.items():
        adjacency_list[node] = []
        for adj in data["adyacentes"]:
            distance = geodesic((data["latitud"], data["longitud"]), (graph[adj]["latitud"], graph[adj]["longitud"])).kilometers
            adjacency_list[node].append((adj, distance))
    
    
    def dijkstra_algorithm(start, goal):
        queue = [(0, start)]
        distances = {start: 0}
        previous_nodes = {start: None}
        
        while queue:
            current_distance, current_node = heapq.heappop(queue)
            
            if current_node == goal:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = previous_nodes[current_node]
                return path[::-1]
            
            for neighbor, weight in adjacency_list.get(current_node, []):
                distance = current_distance + weight
                if distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(queue, (distance, neighbor))
        
        return None
    
    shortest_path = dijkstra_algorithm(path_request.source, path_request.destination)
    
    if shortest_path is None:
        raise HTTPException(status_code=404, detail="No path found between source and destination")
    
    return {"message": "Shortest path calculated", "path": shortest_path}