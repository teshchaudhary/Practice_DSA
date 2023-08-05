def findMinDiff(A,N,M):
      A.sort()
      
      curr_diff = A[M-1] - A[0]
      res = curr_diff
  
      for i in range(1,len(A)-M+1):
          j = (M-1)+i
          curr_diff = A[j] - A[i]
          res = min(res, curr_diff)
  
      return res
