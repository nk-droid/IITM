### Simple Search Algorithm

```
1 	OPEN  🡨 {S}
2 	while OPEN is not empty
3 	   do pick some node N from OPEN
4 		OPEN 🡨  OPEN − {N}
5 		if GoalTest(N) = TRUE
6 		  then 	return N
7 		  else 	OPEN 🡨  OPEN ∪ MoveGen(N)
8 	return FAILURE
```