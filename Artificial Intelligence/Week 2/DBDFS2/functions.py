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