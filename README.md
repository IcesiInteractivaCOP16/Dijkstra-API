# Dijkstra-API (English)

## Description

This project implements a RESTful API using Python with Flask. The system applies Dijkstra's algorithm to calculate the shortest path between an initial geographic coordinate and a list of other coordinates, based on their latitude and altitude.

The input is provided via a POST request in JSON format, containing the initial coordinates and a list of additional coordinates as pairs of latitude and altitude values. The output will be a sorted list of coordinates, with the starting point as the first element, ordered by the shortest path according to Dijkstra's algorithm.

The system is designed to handle around 100 simultaneous requests, with a maximum of 10 coordinates per request.

## Technologies

- Python 3.x
- Flask
- Dijkstra's Algorithm

## API Endpoints

### POST `/path`

- **Description**: Receives a set of coordinates and returns the shortest path starting from the initial point, calculated using Dijkstra’s algorithm.
  
- **Input**: JSON object containing:
  - `initial`: A list of two values representing the starting point `[latitude, altitude]`.
  - `coordinates`: A list of lists, where each inner list represents a coordinate `[latitude, altitude]`.

  Example of request body:
  ```json
  {
    "initial": [40.7128, -74.0060],
    "coordinates": [
      [34.0522, -118.2437],
      [51.5074, -0.1278]
    ]
  }
  ```

- **Output**: A list of coordinates starting from the initial point, ordered by the shortest path calculated via Dijkstra's algorithm.

  Example of response body:
  ```json
  [
    [40.7128, -74.0060],
    [51.5074, -0.1278],
    [34.0522, -118.2437]
  ]
  ```

## Notes

- The system is designed to handle up to 100 simultaneous requests, with a maximum of 10 coordinates per request.
- This project is not optimized for very high loads, but it can be expanded if needed.

---

# Dijkstra-API (Spanish)

## Descripción

Este proyecto implementa una API RESTful usando Python con Flask. El sistema utiliza el algoritmo de Dijkstra para calcular la ruta más corta entre un punto inicial y una lista de otras coordenadas geográficas, basadas en su latitud y altitud.

La entrada se proporciona a través de una solicitud POST en formato JSON que contiene las coordenadas iniciales y una lista de coordenadas adicionales como pares de valores de latitud y altitud. La salida será una lista ordenada de coordenadas, con el punto inicial como el primer elemento, ordenadas según el camino más corto calculado con el algoritmo de Dijkstra.

El sistema está diseñado para manejar alrededor de 100 solicitudes simultáneas, con un máximo de 10 coordenadas por solicitud.

## Tecnologías

- Python 3.x
- Flask
- Algoritmo de Dijkstra

## Endpoints de la API

### POST `/path`

- **Descripción**: Recibe un conjunto de coordenadas y devuelve la ruta más corta comenzando desde el punto inicial, calculada mediante el algoritmo de Dijkstra.
  
- **Entrada**: Objeto JSON que contiene:
  - `initial`: Una lista de dos valores que representa el punto inicial `[latitud, altitud]`.
  - `coordinates`: Una lista de listas, donde cada lista interna representa una coordenada `[latitud, altitud]`.

  Ejemplo de cuerpo de la solicitud:
  ```json
  {
    "initial": [40.7128, -74.0060],
    "coordinates": [
      [34.0522, -118.2437],
      [51.5074, -0.1278]
    ]
  }
  ```

- **Salida**: Una lista de coordenadas que comienza con el punto inicial, ordenada por la ruta más corta calculada mediante el algoritmo de Dijkstra.

  Ejemplo de cuerpo de la respuesta:
  ```json
  [
    [40.7128, -74.0060],
    [51.5074, -0.1278],
    [34.0522, -118.2437]
  ]
  ```

## Notas

- El sistema está diseñado para manejar hasta 100 solicitudes simultáneas, con un máximo de 10 coordenadas por solicitud.
- Este proyecto no está optimizado para cargas muy altas, pero puede ampliarse si es necesario.
