class Solution:
    def posOfRightMostDiffBit(self, m, n):
         if m == n:
           return -1
        
         ans = 1
         m1, n1 = 0, 0
        
         while m and n:
           m1, n1 = m % 2, n % 2
           if m1 != n1:
             return ans
           ans += 1
           m //= 2
           n //= 2
        
         return ans
            
