def totalCuts(N, K, A):

    res = 0
    lMax = [0]*N
    rMin = [0]*N

    lMax[0] = A[0]
    for i in range(1, N):
        lMax[i] = max(A[i], lMax[i-1])

    rMin[N-1] = A[N-1]
    for i in range(N-2, -1, -1):
        rMin[i] = min(A[i], rMin[i+1])

    for i in range(1, N):
        if lMax[i-1]+rMin[i] >= K:
            res += 1

    return res
