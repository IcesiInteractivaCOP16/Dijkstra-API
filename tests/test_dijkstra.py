import pytest
from geopy.distance import geodesic
from app.api.dijkstra import calculate_shortest_path
from app.api.models import Coordenada, Ruta

