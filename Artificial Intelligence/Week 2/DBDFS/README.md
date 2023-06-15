### DBDFS Algorithm

```
1   OPEN 🡨 (S, null) : []
2   CLOSED 🡨 empty list
3   while OPEN is not empty
4       nodePair 🡨 head OPEN
5       (N, _, depth) 🡨 nodeTriplet
6       if GoalTest(N) = True
7           return ReconstructPath(nodePair, CLOSED)
8        else CLOSED 🡨 nodeTriplet : CLOSED
9           children 🡨 MoveGen(N)
10          newNodes 🡨 RemoveSeen(children, OPEN, CLOSED)
11          newTriplets 🡨 MakeTriplets(NewNodes, N)
12          OPEN 🡨 newTriplets ++ (tail OPEN)
13  return empty list
```

**Functions used**

-   RemoveSeen - Removes from nodeList any nodes that are already in OPEN or in CLOSED
-   MakePairs - Makes a triplet (head(nodeList), parent, depth)
-   ReconstructPath - Traces back through Parent links and reconstructs the path found.