# Naive Solution
# O(n+k), array has elements less than equal to k
# Example
# arr = [1,4,4,1,0,1]
# count = [1,3,0,0,2]
# arr = [0,1,1,1,4,4]

def countSort_1(arr):
    n = len(arr)
    count = [0]*n

    for i in range(n):
        count[arr[i]] += 1
    
    index = 0
    for i in range(n):
        for j in range(count[i]):
            arr[index] = i
            index += 1
    
arr = [1,4,4,1,0,1]
countSort_1(arr)
print(arr)

# Efficient Solution
# O(n+k), array has elements less than equal to k
# Ensures Stability
# Example
# arr = [1,4,4,1,0,1]
# count = [1,3,0,0,2]
# count = [1,4,4,4,6]
# res = [0,1,1,1,4,4]

# count[i] tell how many values are lesser than equal to the value i present in the array
def countSort_2(arr):
    n = len(arr)
    count = [0]*n
    res = [0]*n

    for i in range(n):
        count[arr[i]] += 1
    
    for i in range(1,n):
        count[i] += count[i-1]
    
    for x in reversed(arr):
        res[count[x]-1] = x
        count[x] -= 1

    return res

arr = [1,4,4,1,0,1]
print(countSort_2(arr))
