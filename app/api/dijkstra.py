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
            "Universidad del Valle"
        ]
    },
    "Bulevar del Río": {
        "latitud": 3.4528374462960167,
        "longitud": -76.5347951337262,
        "adyacentes": [
            "Banco de Bogotá",
            "UNICOC"
        ]
    },
    "Universidad del Valle": {
        "latitud": 3.376762549737823,
        "longitud": -76.53472029139806,
        "adyacentes": [
            "Universidad ICESI",
            "Instituto Humboldt"
        ]
    },
    "Centro Cultural de Cali": {
        "latitud": 3.4499164810651934,
        "longitud": -76.53617706256205,
        "adyacentes": [
            "Centro Cultural del Banco de la República",
            "Biblioteca Departamental Jorge Garcés Borrero"
        ]
    },
    "Cámara de Comercio de Cali": {
        "latitud": 3.451508290689324,
        "longitud": -76.53552364435075,
        "adyacentes": [
            "Banco de Bogotá",
            "Centro Cultural del Banco de la República"
        ]
    },
    "Banco de Bogotá": {
        "latitud": 3.452573287034155,
        "longitud": -76.53534363128803,
        "adyacentes": [
            "Bulevar del Río",
            "Cámara de Comercio de Cali"
        ]
    },
    "UNICOC": {
        "latitud": 3.456180458393561,
        "longitud": -76.53294739536896,
        "adyacentes": [
            "Universidad ECCI",
            "Bulevar del Río"
        ]
    },
    "Universidad ECCI": {
        "latitud": 3.4567914151485253,
        "longitud": -76.5330726030404,
        "adyacentes": [
            "UNICOC",
            "Ecoparque Pisamos"
        ]
    },
    "Centro Cultural del Banco de la República": {
        "latitud": 3.450110346790639,
        "longitud": -76.53559510304052,
        "adyacentes": [
            "Cámara de Comercio de Cali",
            "Centro Cultural de Cali"
        ]
    },
    "Ecoparque Pisamos": {
        "latitud": 3.441450666657592,
        "longitud": -76.48172469162074,
        "adyacentes": [
            "Universidad ECCI",
            "Biblioteca Departamental Jorge Garcés Borrero"
        ]
    },
    "Biblioteca Departamental Jorge Garcés Borrero": {
        "latitud": 3.436426530173853,
        "longitud": -76.53922341838341,
        "adyacentes": [
            "Centro Cultural de Cali",
            "Instituto Humboldt",
            "Ecoparque Pisamos"
        ]
    },
    "Instituto Humboldt": {
        "latitud": 3.429120017986491,
        "longitud": -76.54139602023353,
        "adyacentes": [
            "Biblioteca Departamental Jorge Garcés Borrero",
            "Universidad del Valle"
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