# Find the two repeated elements in the given array
# There are numbers from 1 to N and N+2 elments in the array
# O(N)
# Make the element negative at the founded valued index

def twoRepeated(arr):
    res = []

    for i in range(len(arr)):
        idx = abs(arr[i]) - 1

        arr[idx] *= -1

        if arr[idx] > 0:
            res.append(idx+1)

    return res


arr = [1, 2, 1, 3, 4, 3]
print(twoRepeated(arr))
