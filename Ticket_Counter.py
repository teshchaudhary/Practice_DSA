from collections import deque

def distributeTicket(N, K):
    q = deque()
    for i in range(1, N+1):
        q.append(i)

    while q:
        for i in range(K):
            if q:
                ele = q.popleft()

        for i in range(K):
            if q:
                ele = q.pop()

    return ele
