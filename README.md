# TSP Solver Report - Roll No. 21f3000611

## Introduction
In this report, I share my approach, implementation, and reflections on solving the Traveling Salesman Problem (TSP). The goal was to create a program finding the shortest tour among a set of cities, visiting each city once and returning to the starting city.

## Approach
### Algorithm Selection
After careful consideration, I opted for the Nearest Neighbor Algorithm due to its simplicity and reasonable computational efficiency. The algorithm starts from a chosen city, iteratively selecting the nearest unvisited city until all cities are visited, forming a cycle.

## Implementation
### Data Representation
Cities were represented using 2D coordinates, and a distance matrix stored the distances between each pair of cities, facilitating easy access during algorithm execution.
### Nearest Neighbor Algorithm
The core of the solution lies in the Nearest Neighbor Algorithm. The algorithm starts from the initial city, iteratively selecting the nearest unvisited city until a complete tour is formed. To ensure correctness, I implemented the `is_valid_tour` function.
### Input Processing
The program reads input from standard input, handling both Euclidean and non-Euclidean distances. Input includes metric type, the number of cities, 2D coordinates, and the distance matrix.
### Output
The output follows the specified format, printing the path representation of the tour. Validation is done using the `is_valid_tour` function.

## Improvements
While the Nearest Neighbor Algorithm is effective, potential enhancements include:
1. **Optimization Techniques:** Investigate optimizations for improved performance, especially with larger datasets.
2. **Alternate Algorithms:** Explore Genetic Algorithms, Simulated Annealing, or Ant Colony Optimization for comparison and potential improvements.
3. **User-Friendly Features:** Enhance the user interface by allowing data input from external files and providing informative messages during execution.

## Conclusion
In conclusion, the implemented Nearest Neighbor Algorithm forms a robust foundation for solving the TSP. The program successfully processes input, executes the algorithm, and outputs the optimal tour. Further exploration of optimizations and alternative algorithms could elevate the solution's capabilities.
