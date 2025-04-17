graph = {
    "A": ["B", "C", "H"],
    "B": ["A"],
    "C": ["A", "D"],
    "D": ["C", "E", "F"],
    "E": ["D", "G", "H"],
    "F": ["D", "G"],
    "G": ["E", "F"],
    "H": ["A", "E"]
}

def bfs(graph, start_node):
    queue = [start_node]  # Initialize queue with the start node
    visited_nodes = set([start_node])  # Track visited nodes
    while queue:
        current_node = queue.pop(0)  # Remove the first element (FIFO)
        print(current_node, end=" ")

        for neighbor in graph[current_node]:
            if neighbor not in visited_nodes:
                queue.append(neighbor)  # Add unvisited neighbors to queue
                visited_nodes.add(neighbor)

print("BFS Traversal (Modified):")
bfs(graph, start_node='A')