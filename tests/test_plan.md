
# Test Plan for Dijkstra's Algorithm (English)

This document outlines the tests to validate the implementation of Dijkstra's algorithm in finding the shortest path between geographic coordinates. Inputs are provided in JSON format for ease of reading and efficiency when testing with Postman. Additionally, unit tests, found in the file `test_dijkstra.py`, clearly implement this plan by calling the necessary functions and creating the required objects.

## **Test 1:**

### **Input:**

```json
{
    "initial": {
        "latitude": 40.7128,
        "longitude": -74.0060,
        "adjacents": [
            {
                "latitude": 34.0522,
                "longitude": -118.2437
            },
            {
                "latitude": 41.8781,
                "longitude": -87.6298
            }
        ]
    },
    "coordinates": [
        {
            "latitude": 34.0522,
            "longitude": -118.2437,
            "adjacents": [
                {
                    "latitude": 40.7128,
                    "longitude": -74.0060
                },
                {
                    "latitude": 37.7749,
                    "longitude": -122.4194
                }
            ]
        },
        {
            "latitude": 41.8781,
            "longitude": -87.6298,
            "adjacents": [
                {
                    "latitude": 40.7128,
                    "longitude": -74.0060
                },
                {
                    "latitude": 37.7749,
                    "longitude": -122.4194
                }
            ]
        }
    ],
    "final": {
        "latitude": 37.7749,
        "longitude": -122.4194,
        "adjacents": [
            {
                "latitude": 34.0522,
                "longitude": -118.2437
            },
            {
                "latitude": 41.8781,
                "longitude": -87.6298
            }
        ]
    }
}
```

### **Expected Output:**

```json
{
    "shortest_path": [
        [40.7128, -74.006],
        [41.8781, -87.6298],
        [37.7749, -122.4194]
    ]
}
```

### **Description:**
This test includes an initial node in New York, a final node in San Francisco, and three adjacent cities. The Dijkstra implementation should select the shortest path that passes through Chicago before reaching San Francisco.

---

## **Test 2:**

### **Input:**

```json
{
    "initial": {
        "latitude": 40.7128,
        "longitude": -74.0060,
        "adjacents": [
            {
                "latitude": 34.0522,
                "longitude": -118.2437
            }
        ]
    },
    "coordinates": [
        {
            "latitude": 34.0522,
            "longitude": -118.2437,
            "adjacents": [
                {
                    "latitude": 40.7128,
                    "longitude": -74.0060
                }
            ]
        }
    ],
    "final": {
        "latitude": 34.0522,
        "longitude": -118.2437,
        "adjacents": [
            {
                "latitude": 40.7128,
                "longitude": -74.0060
            }
        ]
    }
}
```

### **Expected Output:**

```json
{
    "shortest_path": [
        [40.7128, -74.006],
        [34.0522, -118.2437]
    ]
}
```

### **Description:**
In this case, there are only two nodes: the initial in New York and the final in Los Angeles. The shortest route is direct, with no intermediate nodes.

---

## **Test 3:**

### **Input:**

```json
{
    "initial": {
        "latitude": 40.7128,
        "longitude": -74.0060,
        "adjacents": [
            {
                "latitude": 41.8781,
                "longitude": -87.6298
            }
        ]
    },
    "coordinates": [
        {
            "latitude": 41.8781,
            "longitude": -87.6298,
            "adjacents": [
                {
                    "latitude": 40.7128,
                    "longitude": -74.0060
                },
                {
                    "latitude": 34.0522,
                    "longitude": -118.2437
                },
                {
                    "latitude": 37.7749,
                    "longitude": -122.4194
                }
            ]
        },
        {
            "latitude": 34.0522,
            "longitude": -118.2437,
            "adjacents": [
                {
                    "latitude": 41.8781,
                    "longitude": -87.6298
                },
                {
                    "latitude": 37.7749,
                    "longitude": -122.4194
                }
            ]
        }
    ],
    "final": {
        "latitude": 37.7749,
        "longitude": -122.4194,
        "adjacents": [
            {
                "latitude": 41.8781,
                "longitude": -87.6298
            },
            {
                "latitude": 34.0522,
                "longitude": -118.2437
            }
        ]
    }
}
```

### **Expected Output:**

```json
{
    "shortest_path": [
        [40.7128, -74.006],
        [41.8781, -87.6298],
        [37.7749, -122.4194]
    ]
}
```

### **Description:**
Here, a path is tested where Chicago is between New York and San Francisco, and the algorithm should choose the optimal path that passes through Chicago before reaching the final destination.


---

# Plan de Pruebas para el Algoritmo de Dijkstra (Español)

Este documento detalla las pruebas para validar la implementación del algoritmo de Dijkstra en la búsqueda del camino más corto entre coordenadas geográficas. Los inputs están dados en formato JSON con el fin de facilidad en su lectura y eficiencia a la hora de probar con Postman. Por otro lado, las pruebas unitarias, que se encuentran en el archivo `test_dijkstra.py`, claramente implementan este plan llamando a las funciones y creando los objetos necesarios. 

## **Test 1:**

### **Input:**

```json
{
    "initial": {
        "latitud": 40.7128,
        "longitud": -74.0060,
        "adyacentes": [
            {
                "latitud": 34.0522,
                "longitud": -118.2437
            },
            {
                "latitud": 41.8781,
                "longitud": -87.6298
            }
        ]
    },
    "coordinates": [
        {
            "latitud": 34.0522,
            "longitud": -118.2437,
            "adyacentes": [
                {
                    "latitud": 40.7128,
                    "longitud": -74.0060
                },
                {
                    "latitud": 37.7749,
                    "longitud": -122.4194
                }
            ]
        },
        {
            "latitud": 41.8781,
            "longitud": -87.6298,
            "adyacentes": [
                {
                    "latitud": 40.7128,
                    "longitud": -74.0060
                },
                {
                    "latitud": 37.7749,
                    "longitud": -122.4194
                }
            ]
        }
    ],
    "final": {
        "latitud": 37.7749,
        "longitud": -122.4194,
        "adyacentes": [
            {
                "latitud": 34.0522,
                "longitud": -118.2437
            },
            {
                "latitud": 41.8781,
                "longitud": -87.6298
            }
        ]
    }
}
```

### **Expected Output:**

```json
{
    "shortest_path": [
        [40.7128, -74.006],
        [41.8781, -87.6298],
        [37.7749, -122.4194]
    ]
}
```

### **Descripción:**
Esta prueba incluye un nodo inicial en Nueva York, un nodo final en San Francisco, y tres ciudades adyacentes. La implementación de Dijkstra debe seleccionar el camino más corto que pasa por Chicago antes de llegar a San Francisco.

---

## **Test 2:**

### **Input:**

```json
{
    "initial": {
        "latitud": 40.7128,
        "longitud": -74.0060,
        "adyacentes": [
            {
                "latitud": 34.0522,
                "longitud": -118.2437
            }
        ]
    },
    "coordinates": [
        {
            "latitud": 34.0522,
            "longitud": -118.2437,
            "adyacentes": [
                {
                    "latitud": 40.7128,
                    "longitud": -74.0060
                }
            ]
        }
    ],
    "final": {
        "latitud": 34.0522,
        "longitud": -118.2437,
        "adyacentes": [
            {
                "latitud": 40.7128,
                "longitud": -74.0060
            }
        ]
    }
}
```

### **Expected Output:**

```json
{
    "shortest_path": [
        [40.7128, -74.006],
        [34.0522, -118.2437]
    ]
}
```

### **Descripción:**
En este caso, solo existen dos nodos: el inicial en Nueva York y el final en Los Ángeles. La ruta más corta es directa, sin nodos intermedios.

---

## **Test 3:**

### **Input:**

```json
{
    "initial": {
        "latitud": 40.7128,
        "longitud": -74.0060,
        "adyacentes": [
            {
                "latitud": 41.8781,
                "longitud": -87.6298
            }
        ]
    },
    "coordinates": [
        {
            "latitud": 41.8781,
            "longitud": -87.6298,
            "adyacentes": [
                {
                    "latitud": 40.7128,
                    "longitud": -74.0060
                },
                {
                    "latitud": 34.0522,
                    "longitud": -118.2437
                },
                {
                    "latitud": 37.7749,
                    "longitud": -122.4194
                }
            ]
        },
        {
            "latitud": 34.0522,
            "longitud": -118.2437,
            "adyacentes": [
                {
                    "latitud": 41.8781,
                    "longitud": -87.6298
                },
                {
                    "latitud": 37.7749,
                    "longitud": -122.4194
                }
            ]
        }
    ],
    "final": {
        "latitud": 37.7749,
        "longitud": -122.4194,
        "adyacentes": [
            {
                "latitud": 41.8781,
                "longitud": -87.6298
            },
            {
                "latitud": 34.0522,
                "longitud": -118.2437
            }
        ]
    }
}
```

### **Expected Output:**

```json
{
    "shortest_path": [
        [40.7128, -74.006],
        [41.8781, -87.6298],
        [37.7749, -122.4194]
    ]
}
```

### **Descripción:**
Aquí se prueba un camino donde Chicago está entre Nueva York y San Francisco, y el algoritmo debe elegir el camino óptimo que pasa por Chicago antes de llegar al destino final.

---
