# Test Plan: Dijkstra's Shortest Path Algorithm

**Project Name:** Pathfinding with Dijkstra's Algorithm  
**Prepared By:** ICESI Interactiva Backend Team
**Date:** 10/10/2024

---

## 1. Objective

The objective of this test plan is to validate the functionality of the Dijkstra-based shortest path algorithm implemented in Python. The algorithm calculates the shortest path between a set of coordinates. We will ensure the correctness of the results by testing various scenarios, including normal cases, edge cases, and invalid conditions.

---

## 2. Scope

The tests will focus on the following functionalities:

- Shortest path calculation between coordinates.
- Proper handling of disconnected graphs.
- Handling of graphs with adyacent coordinates.
- Performance with large distances.
- Handling identical initial and final coordinates.

---

## 3. Test Cases

### Test Case 1: Simple Shortest Path

**Description:**  
Test the calculation of the shortest path with a basic route where no adjacent coordinates are defined.  

**Input:**  
- Initial Coordinate: `(40.7128, -74.0060)`  
- Final Coordinate: `(48.8566, 2.3522)`  
- Intermediate Coordinates:  
  - `(34.0522, -118.2437)`  
  - `(41.8781, -87.6298)`  

**Expected Result:**  
A valid shortest path should be returned as a list of coordinates.

---

### Test Case 2: Route with Adjacent Coordinates

**Description:**  
Test a route where each coordinate has defined adjacent nodes. Ensure the algorithm handles adjacency correctly.  

**Input:**  
- Initial Coordinate: `(40.7128, -74.0060)`  
- Final Coordinate: `(48.8566, 2.3522)`  
- Intermediate Coordinates with Adjacents:  
  - `(34.0522, -118.2437)` (adjacent to final)  
  - `(41.8781, -87.6298)` (adjacent to final)  

**Expected Result:**  
The shortest path should include the correct adjacent nodes and both the initial and final points.

---

### Test Case 3: Non-Connected Graph

**Description:**  
Test a case where the graph is disconnected, meaning there is no path between the initial and final coordinates.  

**Input:**  
- Initial Coordinate: `(40.7128, -74.0060)`  
- Final Coordinate: `(48.8566, 2.3522)`  
- Intermediate Coordinate:  
  - `(34.0522, -118.2437)` (no adjacencies)  

**Expected Result:**  
The algorithm should return `None` as there is no path between the initial and final coordinates.

---

### Test Case 4: Identical Initial and Final Coordinates

**Description:**  
Test the scenario where the initial and final coordinates are the same. This tests if the algorithm handles such cases correctly without unnecessary calculations.  

**Input:**  
- Initial and Final Coordinate: `(40.7128, -74.0060)`  

**Expected Result:**  
The returned path should contain only the single point `(40.7128, -74.0060)`.

---

### Test Case 5: Large Distances

**Description:**  
Test the algorithm's ability to handle large distances between coordinates (e.g., New York to Paris). Ensure the path is correctly calculated and no errors occur due to the large geographic area.  

**Input:**  
- Initial Coordinate: `(40.7128, -74.0060)`  
- Final Coordinate: `(48.8566, 2.3522)`  

**Expected Result:**  
The shortest path should include the initial and final points without errors.

---

## 4. Assumptions

- The coordinates are well-formed with valid latitude and longitude values.
- The geodesic distance calculation uses the `geopy` library to compute real-world distances.
- The system should not crash or produce invalid results for any input scenarios.

---
