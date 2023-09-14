# O(n+k), array has elements less than equal to k
# Example
# arr = [1,4,4,1,0,1]
# count = [1,3,0,0,2]
# arr = [0,1,1,1,4,4]

def countSort(arr):
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
countSort(arr)
print(arr)
