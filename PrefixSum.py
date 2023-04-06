# Get the sum of the given queries like
# getSum(0,3) => Get sum from index 0 to index 3 (both inclusive)
# getSum(3,9) => Get sum from index 3 to index 9 (both inclusive)

# O(n)
def func1(arr, si, ei):
    res = 0
    while si != ei+1:
        res += arr[si]
        si += 1
    
    return res

# arr = [2,8,3,9,6,5,4]
# print(func1(arr,0,6))
