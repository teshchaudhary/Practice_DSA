def sumMatrix(A,B):
      m,n = len(A),len(A[0])
      p,q = len(B),len(B[0])
      
      if m!=p or n!=q:
          return []
          
      res = [[0 for i in range(n)] for i in range(m)]
      for i in range(m):
          for j in range(n):
              res[i][j] = A[i][j]+B[i][j]
              
      return res
