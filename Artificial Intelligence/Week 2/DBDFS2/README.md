### DBDFS2 Algorithm

```
1   count 🡨 0
2   OPEN 🡨 (S, null, 0) : []
3   CLOSED 🡨 empty list
4   while OPEN is not empty
5       nodeTriplet 🡨 head OPEN
6       (N, _, depth) 🡨 nodeTriplet
7       if GoalTest(N) = True
8           return (count, ReconstructPath(nodePair, CLOSED))
9        else CLOSED 🡨 nodeTriplet : CLOSED
10          if depth < depthBound
11              children 🡨 MoveGen(N)
12              newNodes 🡨 RemoveSeen(children, OPEN, CLOSED)
13              newTriplets 🡨 MakeTriplets(NewNodes, N)
14              OPEN 🡨 newTriplets ++ (tail OPEN)
15              count 🡨 count + length newTriplets
16          else OPEN 🡨 tail OPEN
17  return (count, empty list)
```

**Functions used**

-   RemoveSeen - Removes from nodeList any nodes that are already in OPEN or in CLOSED
-   MakePairs - Makes a triplet (head(nodeList), parent, depth)
-   ReconstructPath - Traces back through Parent links and reconstructs the path found.