import random

from functions import GoalTest, MoveGen

def SimpleSearch(GRAPH, SOURCE, GOAL):
    OPEN, CLOSED = MoveGen(GRAPH, SOURCE), set()

    while OPEN:
        N = {random.choice(list(OPEN))}
        OPEN = OPEN - N
        CLOSED = CLOSED.union(N)
        if GoalTest(GOAL, list(N)[0]):
            return "YAY!!! FINALLY REACHED THE GOAL!"
        else:
            OPEN=OPEN.union(MoveGen(GRAPH, list(N)[0]) - CLOSED)
    return "NOT FOUND"