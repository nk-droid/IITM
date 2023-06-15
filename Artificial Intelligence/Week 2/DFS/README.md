### DFS Algorithm

```
1   OPEN 🡨 (S, null) : []
2   CLOSED 🡨 empty list
3   while OPEN is not empty
4       nodePair 🡨 head OPEN
5       (N, _) 🡨 nodePair
6       if GoalTest(N) = True
7           return ReconstructPath(nodePair, CLOSED)
8        else CLOSED 🡨 nodePair : CLOSED
9           children 🡨 MoveGen(N)
10          newNodes 🡨 RemoveSeen(children, OPEN, CLOSED)
11          newPairs 🡨 MakePairs(NewNodes, N)
12          OPEN 🡨 NewPairs ++ (tail OPEN)
13  return empty list

```

**Functions used**

-   RemoveSeen - Removes from nodeList any nodes that are already in OPEN or in CLOSED
-   MakePairs - Makes a pair (head(nodeList), parent)
-   ReconstructPath - Traces back through Parent links and reconstructs the path found.
