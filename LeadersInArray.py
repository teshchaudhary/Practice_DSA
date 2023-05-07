def leaders(A, N):
    arr = [A[-1]]

    m = arr[-1]

    for i in range(N-2, -1, -1):

        if A[i] >= m:
            m = A[i]
            arr.append(m)

    return arr[::-1]
