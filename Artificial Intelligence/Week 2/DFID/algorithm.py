from functions import DBDFS2

def DFID(GRAPH, S, G):
    count, previousCount, path, depthBound = -1, -2, [], 0

    while not path or previousCount == count:
        previousCount=count
        count, path = DBDFS2(GRAPH, S, G, depthBound)
        depthBound+=1
    return path