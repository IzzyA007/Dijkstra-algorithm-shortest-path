graph = {
    'College Square': {'Lewis Science Center': 200, 'Prince Center': 300},
    'Lewis Science Center': {'Speech Language Hearing': 250, 'Computer Science': 150},
    'Speech Language Hearing': {'Maintenance College': 120, 'Burdick': 100},
    'Computer Science': {'Burdick': 30, 'Prince Center': 80, 'Torreyson Library': 40},
    'Burdick': {'Torreyson Library': 80, 'McAlister Hall': 200, 'Maintenance College': 300},
    'Prince Center': {'Torreyson Library': 30, 'Police Dept.': 100},
    'Torreyson Library': {'Old Main': 30},
    'Maintenance College': {'McAlister Hall': 150, 'Wingo': 100, 'New Buisness Building': 30, 'Oak Tree Apt.': 160},
    'Old Main': {'Police Dept.': 200, 'Fine Art': 90, 'McAlister Hall': 100},
    'Police Dept.': {'Fine Art': 50, 'Student Health Center': 100},
    'Fine Art': {'Student Center': 80, 'McAlister Hall': 180},
    'McAlister Hall': {'Student Center': 100, 'Wingo': 50},
    'Student Center': {'Student Health Center': 50, 'New Buisness Building': 110, 'Wingo': 100},
    'Wingo': {'New Buisness Building': 50},
    'Student Health Center': {'Brewer-Hegeman': 200},
    'New Buisness Building': {'Brewer-Hegeman': 20, 'Oak Tree Apt.': 30},
    'Oak Tree Apt.': {'Brewer-Hegeman': 40},
    'Brewer-Hegeman': {'Bear village Apt.': 350},
    'Bear village Apt.': {},
}

import heapq # priority que implementation of the sequence


def dijkstra(graph, start, end): # Function of choice to perform Dijkstra Algorithim
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority = [(0, start)] # stores the distance nodes
    previous_nodes = {node: None for node in graph} # keeps a record of previous nodes in the shortest path

    while priority:
        current_distance, current_node = heapq.heappop(priority)

        # Checks to see if the current path is shorter than the path that has been shown
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items(): # checks neighbor distances and if shorter updates it
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority, (distance, neighbor))

    # Prints all of the  distances
    for node, distance in distances.items():
        print(f"Distance from {start} to {node}: {distance} meters")

    # Resructures the path
    order = []
    current = end
    while previous_nodes[current] is not None:
        order.insert(0, current)
        current = previous_nodes[current]
    order.insert(0, start)

    return distances[end], order

def bellman_ford(graph, start, end): # function of choice to perform Bellman ford
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph} # Keeps track of the last nodes.

    # Relax the edges
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node].items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    previous_nodes[neighbor] = node

    # Check for negative cycles
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains a negative cycle")

    # Prints up all the distances
    for node, distance in distances.items():
        print(f"Distance from {start} to {node}: {distance} meters")

    # Reconstruct the order
    order = []
    current = end
    while previous_nodes[current] is not None:
        order.insert(0, current)
        current = previous_nodes[current]
    order.insert(0, start)

    return distances[end], order

start_location = 'Computer Science' # Starting Path
end_location = input("Enter the destination building: ") # Ending Path
algorithm_choice = input("Choose algorithm (type Dijkstra or Bellman): ") # Chooses an Algorithim and updates it
 # Loop to make sure the algorithim selects a destination in the graph and one of the 2 alogrithims are chosen.
if end_location not in graph:
    print(f"Invalid destination: {end_location}")
else:
    try:
        if algorithm_choice == 'Dijkstra':
            shortest_distance, shortest_path = dijkstra(graph, start_location, end_location)
            print(f"Using Dijkstra's algorithm:")
        elif algorithm_choice == 'Bellman':
            shortest_distance, shortest_path = bellman_ford(graph, start_location, end_location)
            print(f"Using Bellman-Ford algorithm:")
        else:
            print("Invalid algorithm choice. Please enter Dijkstra or Bellman.")
            exit(1)
# Prints all of the results.
        print(f"The shortest distance from {start_location} to {end_location} is {shortest_distance} meters.")
        print(f"The shortest path is: {' -> '.join(shortest_path)}")
    except ValueError as e:
        print(f"Error: {e}")

