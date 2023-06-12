from functions import GoalTest, ReconstructPath, MoveGen, MakeTriplets, RemoveSeen

def DBDFS2(GRAPH, S, G, depthbound):
    count, OPEN, CLOSED = 0, [(S, None, 0)], []

    while OPEN:
        nodeTriplet = OPEN[0]
        N, _, depth = nodeTriplet

        if GoalTest(G, N):
            return count, ReconstructPath(nodeTriplet, CLOSED)
        else:
            CLOSED.insert(0, nodeTriplet)
            if depth<depthbound:
                children = MoveGen(GRAPH, N)
                newNodes = RemoveSeen(children, OPEN, CLOSED)
                newTriplets = MakeTriplets(newNodes, N, depth+1)
                OPEN = newTriplets + OPEN[1:]
                count+=len(newTriplets)
            else:
                OPEN = OPEN[1:]

    return count, []