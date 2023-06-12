from functions import GoalTest, ReconstructPath, MoveGen, MakeTriplets, RemoveSeen

def DBDFS(GRAPH, S, G, depthbound):
    OPEN, CLOSED = [(S, None, 0)], []

    while OPEN:
        nodeTriplet = OPEN[0]
        N, _, depth = nodeTriplet

        if GoalTest(G, N):
            return ReconstructPath(nodeTriplet, CLOSED)
        else:
            CLOSED.insert(0, nodeTriplet)
            if depth<depthbound:
                children = MoveGen(GRAPH, N)
                newNodes = RemoveSeen(children, OPEN, CLOSED)
                newTriplets = MakeTriplets(newNodes, N, depth+1)
                OPEN = newTriplets + OPEN[1:]
            else:
                OPEN = OPEN[1:]

    return "NOT ABLE TO REACH THE GOAL. EITHER DEPTH VALUE IS LOW OR GOAL IS DISJOINT."