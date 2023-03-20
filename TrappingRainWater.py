# We are given a array of bars and we need to determine maximum amount of water we can hold between the bars

# O(n^2)
def func(arr):
    res = 0
    l = len(arr)
    for i in range(1, l-1):
        leftMax = arr[i]
        for j in range(0,i):
            leftMax = max(leftMax, arr[j])

        rightMax = arr[j]

        for j in range(i+1, l):
            rightMax = max(rightMax, arr[j])
        
        res = res + (min(leftMax, rightMax) - arr[i]) # This will reduce the extra space above ground that is taken by the bar in a region where the water it trapped
    
    return res
