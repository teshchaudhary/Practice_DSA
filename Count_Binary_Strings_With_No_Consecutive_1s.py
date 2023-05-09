# We can go and check that upto n digit bit numbers how many are sparse numbers
# This will cost too much of time complexity
# This pattern is making a fibonacci sequence too so it will reduce the time complexity

def matMul(A, B, mod):
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % mod
    return C


def power(A, n, mod):
    if n == 1:
        return A
    H = power(A, n//2, mod)
    res = matMul(H, H, mod)
    if n % 2:
        res = matMul(res, A, mod)
    return res


def countStrings(self, N):
  mod = 10**9 + 7
  return self.power([[1, 1], [1, 0]], N+1, mod)[0][0]
