### DBDFS Algorithm

```
1   OPEN 🡨 (S, null) : []
2   CLOSED 🡨 empty list
3   while OPEN is not empty
4       nodePair 🡨 head OPEN
5       (N, _, depth) 🡨 nodeTriplet
6       if GoalTest(N) = True
7           return ReconstructPath(nodePair, CLOSED)
8       else CLOSED 🡨 nodeTriplet : CLOSED
9           if depth < depthBound
10               children 🡨 MoveGen(N)
11              newNodes 🡨 RemoveSeen(children, OPEN, CLOSED)
12              newTriplets 🡨 MakeTriplets(NewNodes, N)
13              OPEN 🡨 newTriplets ++ (tail OPEN)
14          else OPEN 🡨 tail OPEN
15  return empty list
```

**Functions used**

-   RemoveSeen - Removes from nodeList any nodes that are already in OPEN or in CLOSED
-   MakePairs - Makes a triplet (head(nodeList), parent, depth)
-   ReconstructPath - Traces back through Parent links and reconstructs the path found.