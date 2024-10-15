import pytest
from geopy.distance import geodesic
from app.api.models import Coordenada, Ruta
from app.api.dijkstra import calculate_shortest_path

@pytest.fixture
def setup_dijkstra():
    """ Configuración inicial para las pruebas. """
    # coordenadas de ejemplo
    initial = Coordenada(latitud=40.7128, longitud=-74.0060)
    coord1 = Coordenada(latitud=34.0522, longitud=-118.2437)
    coord2 = Coordenada(latitud=41.8781, longitud=-87.6298)
    final = Coordenada(latitud=37.7749, longitud=-122.4194)

    # Definir adyacentes
    initial.adyacentes = [coord1, coord2]
    coord1.adyacentes = [initial, final]
    coord2.adyacentes = [initial, final]
    final.adyacentes = [coord1, coord2]

    # Definir ruta con las coordenadas
    route = Ruta(initial=initial, coordinates=[coord1, coord2], final=final)
    
    return route, initial, coord1, coord2, final

@pytest.mark.asyncio
async def test_dijkstra_algorithm(setup_dijkstra):
    """ Probar que el algoritmo de Dijkstra calcula correctamente la ruta más corta. """
    route, initial, coord1, coord2, final = setup_dijkstra
    shortest_path = await calculate_shortest_path(route)

    expected_path = [
        (initial.latitud, initial.longitud),
        (coord2.latitud, coord2.longitud), 
        (final.latitud, final.longitud)
    ]
    
    # Verificar que la ruta más corta calculada sea la esperada
    assert shortest_path["shortest_path"] == expected_path, "El camino más corto no coincide con el esperado."


import pytest
from geopy.distance import geodesic
from app.api.models import Coordenada, Ruta
from app.api.dijkstra import calculate_shortest_path

@pytest.fixture
def setup_short_path():
    """ Configuración inicial para la prueba de camino corto. """
    # coordenadas de ejemplo
    initial = Coordenada(latitud=40.7128, longitud=-74.0060)  # Nueva York
    final = Coordenada(latitud=34.0522, longitud=-118.2437)  # Los Ángeles

    # Definir adyacentes
    initial.adyacentes = [final]
    final.adyacentes = [initial]

    # Definir ruta con las coordenadas
    route = Ruta(initial=initial, coordinates=[final], final=final)
    
    return route, initial, final

@pytest.mark.asyncio
async def test_short_path(setup_short_path):
    """ Probar que el algoritmo de Dijkstra calcula correctamente un camino corto. """
    route, initial, final = setup_short_path
    shortest_path = await calculate_shortest_path(route)

    expected_path = [
        (initial.latitud, initial.longitud),
        (final.latitud, final.longitud)
    ]

    # Verificar que la ruta más corta calculada sea la esperada
    assert shortest_path["shortest_path"] == expected_path, "El camino más corto no coincide con el esperado."

@pytest.fixture
def setup_long_path():
    """ Configuración inicial para la prueba de camino largo. """
    # coordenadas de ejemplo
    initial = Coordenada(latitud=40.7128, longitud=-74.0060)  # Nueva York
    coord1 = Coordenada(latitud=34.0522, longitud=-118.2437)  # Los Ángeles
    coord2 = Coordenada(latitud=41.8781, longitud=-87.6298)  # Chicago
    final = Coordenada(latitud=37.7749, longitud=-122.4194)  # San Francisco

    # Definir adyacentes
    initial.adyacentes = [coord2]
    coord2.adyacentes = [initial, coord1, final]
    coord1.adyacentes = [coord2, final]
    final.adyacentes = [coord1, coord2]

    # Definir ruta con las coordenadas
    route = Ruta(initial=initial, coordinates=[coord2, coord1], final=final)

    return route, initial, coord1, coord2, final

@pytest.mark.asyncio
async def test_long_path(setup_dijkstra):
    """ Probar el comportamiento con una ruta larga. """
    route, initial, coord1, coord2, final = setup_dijkstra
    
    shortest_path = await calculate_shortest_path(route)

    expected_path = [
        (initial.latitud, initial.longitud),
        (coord2.latitud, coord2.longitud),  # `coord2` es Chicago
        (final.latitud, final.longitud)
    ]
    
    # Verificar que la ruta más corta calculada sea la esperada
    assert shortest_path["shortest_path"] == expected_path, "El camino más corto no coincide con el esperado."

