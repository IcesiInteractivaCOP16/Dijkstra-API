from fastapi import Header, APIRouter

from app.api.models import Ruta

dijkstra = APIRouter()

@dijkstra.post('/path', status_code=200)
async def calculate_shortest_path(route: Ruta):
    initial = route.initial
    coordinates = route.coordinates
    
    return {"message": "Shortest path calculated"}