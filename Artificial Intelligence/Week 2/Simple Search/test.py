from algorithm import SimpleSearch

GRAPH = {
    'S': ('A', 'B', 'C'),
    'A': ('S', 'B', 'D'),
    'B': ('S', 'A', 'D'),
    'C': ('S', 'G'),
    'D': ('A', 'B', 'E'),
    'E': ('D', 'G'),
    'G': ('C', 'E')
}

print(SimpleSearch(GRAPH, 'S', 'G'))