# Given a list of N fractions, represented as two lists numerator and denominator, the task is to determine the count of pairs of fractions whose sum equals 1.

from collections import defaultdict
import math
def countFractions(n, numerator, denominator):
      fractionCount = defaultdict(int)
      res = 0

      for i in range(n):

          gcd_val = math.gcd(numerator[i], denominator[i])
          
          numerator[i] //= gcd_val
          denominator[i] //= gcd_val

          x_ = denominator[i] - numerator[i]
          y_ = denominator[i]

          if (x_, y_) in fractionCount:

              res += fractionCount[(x_, y_)]
          fractionCount[(numerator[i], denominator[i])] += 1

      return res
