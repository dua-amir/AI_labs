class Graph:
    def __init__(self):
        self.nodes = {}  # To store the graph (nodes and edges)

    def add_edge(self, node1, node2, cost):
        # Add an edge between two nodes with a cost
        if node1 not in self.nodes:
            self.nodes[node1] = []
        if node2 not in self.nodes:
            self.nodes[node2] = []

        self.nodes[node1].append((node2, cost))  # Directed edge
        self.nodes[node2].append((node1, cost))  # Undirected edge

    def a_star(self, start, goal, heuristic):
        # Initialize open list with start node
        open_list = [(start, 0)]  # Contains (node, g_score)

        # Initialize g_score (cost to reach a node)
        g_score = {node: float('inf') for node in self.nodes}  # Set initial cost to infinity
        g_score[start] = 0  # Cost to reach start node is 0

        # Initialize the path tracker (came_from)
        came_from = {}

        while open_list:
            # Get the node with the smallest f_score (g_score + heuristic)
            current_node, current_g = open_list.pop(0)

            # If we reach the goal, return the path
            if current_node == goal:
                return self.reconstruct_path(came_from, start, goal), g_score[goal]

            # Explore the neighbors of the current node
            for neighbor, cost in self.nodes[current_node]:
                # Calculate new g_score for the neighbor
                tentative_g = g_score[current_node] + cost

                # If the new g_score is better, update it
                if tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    open_list.append((neighbor, tentative_g))  # Add the neighbor to open list
                    came_from[neighbor] = current_node  # Record the path

        return None, float('inf')  # Return None if no path found

    def reconstruct_path(self, came_from, start, goal):
        # Reconstruct the path from goal to start by following the 'came_from' tracker
        path = []
        current = goal
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)  # Add the start node
        path.reverse()  # Reverse the path to get the correct order
        return path


# Example Graph Setup
graph = Graph()
graph.add_edge('A', 'B', 1)  # Add an edge between A and B with cost 1
graph.add_edge('A', 'C', 4)  # Add an edge between A and C with cost 4
graph.add_edge('B', 'C', 2)  # Add an edge between B and C with cost 2
graph.add_edge('B', 'D', 5)  # Add an edge between B and D with cost 5
graph.add_edge('C', 'D', 1)  # Add an edge between C and D with cost 1
graph.add_edge('D', 'E', 3)  # Add an edge between D and E with cost 3
graph.add_edge('C', 'E', 6)  # Add an edge between C and E with cost 6

# Example heuristic (straight-line distances to goal E)
heuristic = {
    'A': 7,  # Heuristic for A
    'B': 6,  # Heuristic for B
    'C': 2,  # Heuristic for C
    'D': 1,  # Heuristic for D
    'E': 0  # Heuristic for E (goal)
}

# Run A* Search
start_node = 'A'
goal_node = 'E'
path, cost = graph.a_star(start_node, goal_node, heuristic)

# Output the results
print("Shortest Path using A*:", path)
print("Total Cost:", cost)
