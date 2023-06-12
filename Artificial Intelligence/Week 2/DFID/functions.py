def GoalTest(GOAL, N):
    return GOAL == N

def ReconstructPath(nodeTriplet, CLOSED):
    
    def SkipTo(parent, nodeTriplets):
        if parent == nodeTriplets[0][0]:
            return nodeTriplets
        return SkipTo(parent, nodeTriplets[1:])
    
    node, parent, depth = nodeTriplet
    path = [node]

    while parent:
        path = [parent]+path
        CLOSED = SkipTo(parent, CLOSED)
        _, parent, depth = CLOSED[0]

    return path

def MoveGen(GRAPH, N):
    return list(GRAPH[N])

def RemoveSeen(nodeList, OPEN, CLOSED):

    def OccursIn(node, nodePairs):
        if not nodePairs:
            return 1==0
        elif node == nodePairs[0][0]:
            return 1==1
        else:
            return OccursIn(node, nodePairs[1:])
    
    if not nodeList:
        return []
    else:
        node = nodeList[0]
        if OccursIn(node, OPEN) or OccursIn(node, CLOSED):
            return RemoveSeen(nodeList[1:], OPEN, CLOSED)
        return [node]+RemoveSeen(nodeList[1:], OPEN, CLOSED)

def MakeTriplets(nodeList, parent, depth):
    if nodeList:
        return [(nodeList[0], parent, depth)]+MakeTriplets(nodeList[1:], parent, depth)
    return []

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