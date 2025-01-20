# You are given a number n. Find the total count of set bits for all numbers from 1 to n (both inclusive).

# Solution:
# Eg 11
# 0: 0000
# 1: 0001
# 2: 0010
# 3: 0011
# 4: 0100
# 5: 0101
# 6: 0110
# 7: 0111
# 8: 1000
# 9: 1001
# 10: 1010
# 11: 1011

# Pattern:
# for number 0 - 2**(x-1) where x is the highest power of 2 such that 2**x <= n.
# the above calculates to 7 in our case.
# x can be caluclated by int(math.log2(n)).
# x for the above example will be 3.
# the number of set bits 0-7 will be: x*(2**(x-1))
# so from 0-7 (we are adding a 0 as well so till 7 are 8 numbers)

# for numbers >= 2**x
# the number of 1's at MSB can be written as: n - (2**x) + 1 i.e. 4
# the remaining bits after MSB repeats the same pattern
# in our case it goes from 0-3
# so we recurse from (n-2**(x))

import math
  def countSetBits(n):
      if n <= 1:
          return n
      
      x = int(math.log2(n))
      y = 1 << (x-1)
      z = 1 << x
      
      return ((x*(y))+(n-z+1)+countSetBits(n-z))
