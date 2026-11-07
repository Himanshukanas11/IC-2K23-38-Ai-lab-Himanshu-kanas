# Breadth First Search (BFS)

from collections import deque

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

def bfs(graph, start):

    visited = set()
    queue = deque([start])

    while queue:

        node = queue.popleft()

        if node not in visited:

            print(node, end=" ")

            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)


# Starting BFS
print("BFS Traversal:")
bfs(graph, 'A')