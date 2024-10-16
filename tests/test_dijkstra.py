import pytest
from fastapi.testclient import TestClient
from app.api.dijkstra import dijkstra
from app.api.models import PathRequest

# cliente para pruebas
client = TestClient(dijkstra)

def test_dijkstra_short_path():
    path_request = PathRequest(source="Universidad ICESI", destination="Universidad del Valle")
    
    response = client.post('/path', json=path_request.model_dump())
    assert response.status_code == 200, "No se pudo calcular la ruta."
    
    data = response.json()
    expected_path = ["Universidad ICESI", "Universidad del Valle"]
    assert data["path"] == expected_path, "El camino más corto no coincide con el esperado."


def test_dijkstra_medium_path():
    path_request = PathRequest(source="Bulevar del Río", destination="Universidad ECCI")
    
    response = client.post('/path', json=path_request.model_dump())
    assert response.status_code == 200, "No se pudo calcular la ruta."
    
    data = response.json()
    expected_path = ["Bulevar del Río", "UNICOC", "Universidad ECCI"]
    assert data["path"] == expected_path, "El camino más corto no coincide con el esperado."


def test_dijkstra_large_path():
    path_request = PathRequest(source="Bulevar del Río", destination="Universidad ICESI")
    
    response = client.post('/path', json=path_request.model_dump())
    expected_path = [
        "Bulevar del Río",
        "Banco de Bogotá",
        "Cámara de Comercio de Cali",
        "Centro Cultural del Banco de la República",
        "Centro Cultural de Cali",
        "Biblioteca Departamental Jorge Garcés Borrero",
        "Instituto Humboldt",
        "Universidad del Valle",
        "Universidad ICESI"
    ]
    
    data = response.json()
    assert data["path"] == expected_path, "El camino más corto no coincide con el esperado."

def test_dijkstra_no_path():
    path_request = PathRequest(source="No Source", destination="Universidad ICESI")

    try:
        response = client.post('/path', json=path_request.model_dump())
    except Exception as e:
        assert e.status_code == 404
        assert e.detail == "Source or destination not found in the graph"

    