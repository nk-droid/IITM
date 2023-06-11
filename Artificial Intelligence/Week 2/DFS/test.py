from algorithm import DFS

GRAPH = {
    'S': ('A', 'B', 'C'),
    'A': ('S', 'B', 'D'),
    'B': ('S', 'A', 'D'),
    'C': ('S', 'G'),
    'D': ('A', 'B', 'E'),
    'E': ('D', 'G'),
    'G': ('C', 'E')
}

print(DFS(GRAPH, 'S', 'G'))