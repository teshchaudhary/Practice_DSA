# Maximum Identical Bowls POTD

def getMaximum(N, arr):

    total_cookies = sum(arr)

    for i in range(N, 0, -1):
        if total_cookies % i == 0:
            return i

    return 0
