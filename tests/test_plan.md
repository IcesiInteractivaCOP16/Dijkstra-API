
# Test Plan for Dijkstra's Algorithm (English)

This document outlines the tests to validate the implementation of Dijkstra's algorithm in finding the shortest path between geographic coordinates. Inputs are provided in JSON format for ease of reading and efficiency when testing with Postman. Additionally, unit tests, found in the file `test_dijkstra.py`, clearly implement this plan by calling the necessary functions and creating the required objects.

## **Test 1: Short Path**

### **Description:**  
Tests the algorithm's ability to compute the shortest path between two directly connected locations, "Universidad ICESI" and "Universidad del Valle."

### **Input:**  
```json
{
    "source": "Universidad ICESI",
    "destination": "Universidad del Valle"
}
```

### **Output:**
```json
{
    "message": "Shortest path calculated",
    "path": [
        "Universidad ICESI",
        "Universidad del Valle"
    ]
}
```

## **Test 2: Medium Path**

### **Description:**  
This test verifies the algorithm can select the optimal path that passes through "UNICOC" on the way from "Bulevar del Río" to "Universidad ECCI."

### **Input:**  
```json
{
    "source": "Bulevar del Río",
    "destination": "Universidad ECCI"
}
```

### **Output:**
```json
{
    "message": "Shortest path calculated",
    "path": [
        "Bulevar del Río",
        "UNICOC",
        "Universidad ECCI"
    ]
}
```

## **Test 3: Long Path**

### **Description:**  
Tests a complex route with several intermediate points between "Bulevar del Río" and "Universidad ICESI." It ensures that all intermediate nodes are visited in the correct order.

### **Input:**  
```json
{
    "source": "Bulevar del Río",
    "destination": "Universidad ICESI"
}
```

### **Output:**
```json
{
    "message": "Shortest path calculated",
    "path": [
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
}
```

## **Test 4: No Path**

### **Description:**  
Validates that the API correctly handles cases where the source location does not exist in the graph.

### **Input:**  
```json
{
    "source": "No Source",
    "destination": "Universidad ICESI"
}
```

### **Output:**
Status `404`
```json
{
    "detail": "Source or destination not found in the graph"
}
```

## **Conclusion**
This test plan ensures that the Dijkstra's algorithm implementation can correctly identify paths across simple, medium, and complex scenarios, while also handling error cases gracefully. These tests align with the current API design, ensuring smooth functionality when integrated into a larger system.

---

# Plan de Pruebas para el Algoritmo de Dijkstra (Español)

Este documento describe las pruebas para validar la implementación del algoritmo de Dijkstra en la búsqueda del camino más corto entre coordenadas geográficas. Las entradas se proporcionan en formato JSON para facilitar la lectura y la eficiencia al realizar pruebas con Postman. Además, las pruebas unitarias, que se encuentran en el archivo `test_dijkstra.py`, implementan claramente este plan llamando a las funciones necesarias y creando los objetos requeridos.

## **Prueba 1: Camino Corto**

### **Descripción:**
Prueba la capacidad del algoritmo para calcular el camino más corto entre dos ubicaciones directamente conectadas, "Universidad ICESI" y "Universidad del Valle".

### **Entrada:**

```json
{
    "source": "Universidad ICESI",
    "destination": "Universidad del Valle"
}
```

### **Salida:**

```json
{
    "message": "Shortest path calculated",
    "path": [
        "Universidad ICESI",
        "Universidad del Valle"
    ]
}
```

## **Prueba 2: Camino Medio**

### **Descripción:**
Esta prueba verifica que el algoritmo pueda seleccionar el camino óptimo que pasa por "UNICOC" en el trayecto del "Bulevar del Río" a la "Universidad ECCI".

### **Entrada:**  
```json
{
    "source": "Bulevar del Río",
    "destination": "Universidad ECCI"
}
```

### **Salida:**
```json
{
    "message": "Shortest path calculated",
    "path": [
        "Bulevar del Río",
        "UNICOC",
        "Universidad ECCI"
    ]
}
```

## **Prueba 3: Camino Largo**

### **Descripción:**
Prueba un recorrido complejo con varios puntos intermedios entre el "Bulevar del Río" y la "Universidad ICESI". Garantiza que todos los nodos intermedios se visiten en el orden correcto.

### **Entrada:**  
```json
{
    "source": "Bulevar del Río",
    "destination": "Universidad ICESI"
}
```

### **Salida:**
```json
{
    "message": "Shortest path calculated",
    "path": [
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
}
```

## **Prueba 4: No Hay Camino**

### **Descripción:**
Valida que la API maneje correctamente los casos en los que la ubicación de origen no existe en el gráfico.

### **Entrada:**  
```json
{
    "source": "No Source",
    "destination": "Universidad ICESI"
}
```

### **Salida:**
Status `404`
```json
{
    "detail": "Source or destination not found in the graph"
}
```

## **Conclusión**
Este plan de prueba garantiza que la implementación del algoritmo de Dijkstra pueda identificar correctamente rutas en escenarios simples, medianos y complejos, al mismo tiempo que maneja los casos de error con elegancia. Estas pruebas se alinean con el diseño de API actual, lo que garantiza una funcionalidad fluida cuando se integra en un sistema más grande.