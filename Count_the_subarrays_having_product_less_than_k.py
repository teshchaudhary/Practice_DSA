def countSubArrayProductLessThanK(a, n, k):
      res = 0
      curr = 1
      si = ei = 0
      
      while ei < n:
          curr *= a[ei]
  
          while si <= ei and curr >= k:
              curr //= a[si]
              si += 1
          
          res += (ei - si + 1)
          ei += 1
      
      return res
