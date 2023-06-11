### Simple Search Algorithm

```
1   OPEN 🡨  {start}
2   CLOSED 🡨   { }
3   while OPEN is not empty
4      do Pick some node N from open
5           OPEN 🡨  OPEN − {N}
6           CLOSED 🡨  CLOSED ∪ {N}
7           if GoalTest(N) = TRUE
8              then return N
9           else OPEN 🡨 OPEN ∪ {MoveGen(N) − CLOSED}
10  return FAILURE
```