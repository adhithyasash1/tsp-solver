def nearest_neighbor_algorithm(distance_matrix):
    n = len(distance_matrix)
    unvisited_cities = set(range(1, n))
    tour = [0]  # Start from city 0
    total_cost = 0.0

    while unvisited_cities:
        current_city = tour[-1]
        nearest_city = min(unvisited_cities, key=lambda city: distance_matrix[current_city][city])
        tour.append(nearest_city)
        unvisited_cities.remove(nearest_city)
        total_cost += distance_matrix[current_city][nearest_city]

    # The entire tour is returned, including the start node
    return tour, total_cost


def parse_input():
    metric_type = input().strip()
    n = int(input())
    coordinates = [tuple(map(float, input().split())) for _ in range(n)]
    distance_matrix = [[float(val) for val in input().split()] for _ in range(n)]

    return metric_type, n, coordinates, distance_matrix


def print_tour(tour):
    print(" ".join(map(str, tour)))


def main():
    metric_type, n, coordinates, distance_matrix = parse_input()
    tour, total_cost = nearest_neighbor_algorithm(distance_matrix)
    print_tour(tour)

if __name__ == "__main__":
    main()
