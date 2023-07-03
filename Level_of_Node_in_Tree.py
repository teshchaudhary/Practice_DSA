# DP Solution

def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        table = [[0, 0]] * (n + 1)
        table[0] = [1, 1]
        table[1] = [1, 1]
        for i in range(2, n+1):
            table[i] = [table[i-1][0] * i, (table[i-1][0] * i)+table[i-1][1]]
        return table


def FindLevel(N):
    table = fact(20)

    if N == 1:
        return 1

    i = 1

    while table[i][1] < N:
        i += 1

    if table[i][1] > N and table[i-1][1] > N:
        return i - 1

    else:
        return i


# Effective Solution

def FindLevel(self,N):
      level = 0
      curr = 1
      total = 0
      while total<N:
          level += 1
          curr *= level
          total += curr
      return level  
