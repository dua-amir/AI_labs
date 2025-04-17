# This is a graph where each city connects to others with certain travel costs
graph = {
    "Arad": {"Zerind": 75, "Timisoara": 118, "Sibiu": 140},
    "Zerind": {"Arad": 75, "Oradea": 71},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Sibiu": {"Arad": 140, "Oradea": 151, "Fagaras": 99, "Rimnicu Vilcea": 80},
    "Fagaras": {"Sibiu": 99, "Bucharest": 211},
    "Rimnicu Vilcea": {"Sibiu": 80, "Pitesti": 97, "Craiova": 146},
    "Pitesti": {"Rimnicu Vilcea": 97, "Bucharest": 101, "Craiova": 138},
    "Craiova": {"Drobeta": 120, "Rimnicu Vilcea": 146, "Pitesti": 138},
    "Drobeta": {"Craiova": 120, "Mehadia": 75},
    "Mehadia": {"Drobeta": 75, "Lugoj": 70},
    "Lugoj": {"Mehadia": 70, "Timisoara": 111},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Bucharest": {"Fagaras": 211, "Pitesti": 101},
}

# Function to find the shortest path from start city to goal city
def dijkstra(graph, start, goal):
    # Set initial distances: all cities have infinite distance except the starting city (distance 0)
    distances = {city: float('inf') for city in graph}
    distances[start] = 0  # Starting city has zero cost to reach

    visited = set()  # Set to store already visited cities
    parent = {start: None}  # Dictionary to track the path (where we came from)

    # Loop until we've visited all cities
    while len(visited) < len(graph):
        current = None  # This will store the city with the smallest distance

        # Find the closest unvisited city
        for city in graph:
            if city not in visited:
                if current is None or distances[city] < distances[current]:
                    current = city

        # If there's no reachable unvisited city left, stop the loop
        if current is None:
            break

        # If we've reached the goal city, we can stop early
        if current == goal:
            break

        # Mark the current city as visited
        visited.add(current)

        # Check each neighbor of the current city
        for neighbor, cost in graph[current].items():
            if neighbor not in visited:
                # Calculate new distance to neighbor through current city
                new_dist = distances[current] + cost

                # If new distance is shorter, update the distance and parent
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist  # Update shorter distance
                    parent[neighbor] = current  # Track path for reconstruction

    # Reconstruct the shortest path from goal back to start
    path = []  # To store the path
    node = goal  # Start from the goal and move backwards using parent

    while node is not None:
        path.insert(0, node)  # Insert current node at the beginning of path
        node = parent.get(node)  # Move to the parent of current node

    # Return the path and total cost to reach goal
    return path, distances[goal]

# Call the function to find path from Arad to Bucharest
path, cost = dijkstra(graph, "Arad", "Bucharest")

# Print the final result
print("Path:", " -> ".join(path))  # Show the cities in path order
print("Total Cost:", cost)  # Show total travel cost
