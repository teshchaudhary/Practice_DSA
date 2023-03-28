# We are given a array of bars and we need to determine maximum amount of water we can hold between the bars

# O(n^2)
def func(arr):
    res = 0
    l = len(arr)
    for i in range(1, l-1):
        leftMax = arr[i]
        for j in range(0, i):
            leftMax = max(leftMax, arr[j])

        rightMax = arr[j]

        for j in range(i+1, l):
            rightMax = max(rightMax, arr[j])

        # This will reduce the extra space above ground that is taken by the bar in a region where the water it trapped
        res = res + (min(leftMax, rightMax) - arr[i])

    return res

# Theta(n)


def func1(arr):
    l = len(arr)
    res = 0
    lMax = [0]*l
    rMax = [0]*l

    # An array to get the left one for an element i in arr[i]
    # lMax = [5,5,6,6,6]
    lMax[0] = arr[0]
    for i in range(1, l):
        lMax[i] = max(arr[i], lMax[i-1])

    # An array to get the left one for an element i in arr[i]
    # rMax = [6,6,6,3,3]
    rMax[l-1] = arr[l-1]
    for i in range(l-2, -1, -1):
        rMax[i] = max(arr[i], rMax[i+1])

    # We start from the second of the start and last and keep comparing
    # res = (5-0)+(6-6)+(3-2)
    for i in range(1, l-1):
        res = res + (min(lMax[i], rMax[i]) - arr[i])

    return res


arr = [5, 0, 6, 2, 3]
print(func1(arr))