from algorithm import DBDFS2

GRAPH = {
    'S': ('A', 'B', 'C'),
    'A': ('S', 'B', 'D'),
    'B': ('S', 'A', 'D'),
    'C': ('S', 'G'),
    'D': ('A', 'B', 'E'),
    'E': ('D', 'G'),
    'G': ('C', 'E')
}

print(DBDFS2(GRAPH, 'S', 'G', 4))