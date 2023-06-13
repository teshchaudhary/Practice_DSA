def DFSrec(adj, s, visited):
    visited[s] = True
    print(s, end = " ")

    for u in adj[s]:
        if visited[u] == False:
            # Going to their connected components in depth
            DFSrec(adj, u, visited)

def DFS(adj,s):
    visited = [False] * len(adj)
    DFSrec(adj, s, visited)

adj = [[1, 2], [0, 3, 4], [0, 3], [1, 2, 4], [1, 3]]
DFS(adj,0)
