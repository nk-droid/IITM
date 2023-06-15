### DFID Algorithm

```
1   count 🡨 -1
2   path 🡨 empty list
3   depthBound 🡨 0
4   repeat
5       previousCount 🡨 count
6       (count, path) 🡨 DBDFS2(S, depthBound)
7       depthBound 🡨 depthBound + 1
8   until (path is not empty) or (previousCount = count)
9   return path
```

**Function used**

- DBDFS2 - Implements [DBDFS2 algorithm](../DBDFS2/).