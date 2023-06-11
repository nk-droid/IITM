from functions import GoalTest, ReconstructPath, MoveGen, MakePairs, RemoveSeen

def BFS(GRAPH, S, G):
    OPEN, CLOSED = [(S, None)], []
    while OPEN:
        nodePair = OPEN[0]
        N, _ = nodePair

        if GoalTest(G, N):
            return ReconstructPath(nodePair, CLOSED)
        else:
            CLOSED.insert(0, nodePair)
            children = MoveGen(GRAPH, N)
            newNodes = RemoveSeen(children, OPEN, CLOSED)
            newPairs = MakePairs(newNodes, N)
            OPEN = OPEN[1:] + newPairs

    return []