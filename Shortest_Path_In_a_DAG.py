from typing import List
from collections import deque 

class Solution:
    def dfs(self,i, vis, stack, adj):
        vis[i] = True
        for v,weight in adj[i]:
            if vis[v] == False:
                self.dfs(v, vis, stack, adj)
        stack.append(i)
        
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v, weight in edges:
            adj[u].append([v,weight])

        vis = [0]*n
        stack = []*n
        
        for i in range(n):
            if vis[i] == 0:
                self.dfs(i, vis,stack,adj)

        distance = [float('inf')]*n
        distance[0] = 0

        while stack:
            i = stack.pop()
            if distance[i] < float('inf'):
                
                for node,weight in adj[i]:
                    newWeight = weight+distance[i]
                    if distance[node] > newWeight:
                        distance[node] = newWeight
                    
        for i in range(n):
            if distance[i]== float('inf'):
                distance[i] = -1
        return distance
