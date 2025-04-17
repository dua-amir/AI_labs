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

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node, end=" ")  # Print the node when visited
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Example Usage
start_node = "A"
print("DFS Traversal starting from node", start_node)
dfs(graph, start_node)
