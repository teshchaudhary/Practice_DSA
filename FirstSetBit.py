# This works because -n is the two's complement of n, which flips all bits and adds 1.
# The result has all bits cleared except the rightmost set bit of 𝑛.

def getFirstSetBit(self,n):
      res = 0
      isolated_first_set_bit =  n&(-n)
      
      while isolated_first_set_bit:
          res += 1
          isolated_first_set_bit >>= 1
      
      return res
