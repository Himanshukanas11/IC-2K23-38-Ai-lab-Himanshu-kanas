
# Depth First Search (DFS)

# Creating a graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# DFS function
def dfs(graph, node, visited):

    if node not in visited:

        print(node, end=" ")
        visited.add(node)

        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)


# Starting DFS
print("DFS Traversal:")
visited = set()
dfs(graph, 'A', visited)