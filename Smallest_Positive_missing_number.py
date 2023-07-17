def missingNumber(self,arr,n):
      visited = [False]*(n+1)
      
      for i in range(n):
          if arr[i] > 0 and arr[i] <= n:
              visited[arr[i]] = True
      
      for i in range(1,n+1):
          if visited[i] == False:
              return i
      
      return n + 1
