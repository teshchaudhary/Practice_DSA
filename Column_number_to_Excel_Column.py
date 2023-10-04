# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
# Excel columns has a pattern like A, B, C, … ,Z, AA, AB, AC,…. ,AZ, BA, BB, … ZZ, AAA, AAB ….. etc. In other words, column 1 is named as “A”, column 2 as “B”, column 27 as “AA” and so on.

def colName(n):
      if n <= 26:
          return chr(64 + n)
      
      base_26 = 0
      res = ""
      while n:
          ud = (n - 1) % 26
          base_26 = base_26 * 26 + ud
          res = chr(65 + ud) + res
          n = (n - 1) // 26
      return res
