def maxOnes(a, n):
      res = 0
      c_1 = c_0 = 0
      
      for i in a:
          if i == 1:
              c_1 += 1
              c_0 -= 1
          
          else:
              c_0 += 1
      
          res = max(res, c_0)
          c_0 = max(0, c_0)
      
      return res + c_1
