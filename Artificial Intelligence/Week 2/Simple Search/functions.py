def GoalTest(GOAL, N):
    return GOAL == N

def MoveGen(GRAPH, N):
    print('{} ===> {}'.format(N, GRAPH[N]))
    return set(GRAPH[N])