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
    

def df(adj,s):
    visited = [False]*len(adj)

    stack = []
    stack.append(s)

    while stack:
        s = stack.pop()

        # Stack may contain same vertex twice. So
        # we need to print the popped item only
        # if it is not visited.
        if not visited[s]:
            print(s,end=' ')
            visited[s] = True

        # Get all adjacent vertices of the popped vertex s
        # If a adjacent has not been visited, then push it
        # to the stack.
        for u in adj[s]:
            if not visited[u]:
                stack.append(u)

adj = [[1, 2], [0, 3, 4], [0, 3], [1, 2, 4], [1, 3]]

df(adj,0)
adj = [[1, 2], [0, 3, 4], [0, 3], [1, 2, 4], [1, 3]]
DFS(adj,0)
