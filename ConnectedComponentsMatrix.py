from collections import deque

def bfs(row, col, adj, visited):
    visited[row][col] = True
    q = deque()
    q.append([row, col])
    rows, columns = len(adj), len(adj[0])

    while q:
        row, col = q.popleft()
        
        for delrow in range(-1, 2):
            for delcol in range(-1, 2):
                nrow = row + delrow
                ncol = col + delcol

                if (nrow >= 0 and nrow < rows) and \
                    (ncol >= 0 and ncol < columns) and \
                    adj[nrow][ncol] == 1 and \
                    not visited[nrow][ncol]:
                    q.append([nrow, ncol])
                    visited[row][col] = True

def numIslands(adj):
                        
    rows, columns = len(adj), len(adj[0])
    visited = [[0] * columns for _ in range(rows)]
    res = 0

    for row in range(rows):
        for column in range(columns):
            if not visited[row][column] and adj[row][column] == 1:
                res += 1
                bfs(row, column, adj, visited)
    
    return res
