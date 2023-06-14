# There are N bags with diamonds in them. The i'th of these bags contains A[i] diamonds. If you drop a bag with A[i] diamonds,
# it changes to A[i]/2 diamondsand you gain A[i] diamonds. Dropping a bag takes 1 minute. Find the maximum number of diamonds 
# that you can take if you are given K minutes.

import heapq as hq

def maxDiamonds(A, N, K):
    ans = 0
    maxHeap = [-i for i in A]
    hq.heapify(maxHeap)

    for _ in range(K):
        ele = -hq.heappop(maxHeap)
        ans += ele

        newVal = ele // 2
        hq.heappush(maxHeap, -newVal)

    return ans
