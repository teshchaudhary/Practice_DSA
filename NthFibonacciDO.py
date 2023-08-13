table = [0]*((10**5)+1)
def nthFibonacci(n):
      table[0] = 0
      table[1] = 1
      
      if n == 1:
          return 1
      
      for i in range(2,n+1):
          if table[i]:
              if i == n:
                  return table[i]%1000000007

          else:
              table[i] = table[i-1] + table[i-2]
              if i == n:
                  return table[n]%1000000007
