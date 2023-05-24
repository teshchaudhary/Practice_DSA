# Remove duplicates from sorted array
# This will take space complexity as slicing makes a new copy of the array
# in worst case the space complexity will go O(n) when all elements are unique

def rem(arr):
    res = 1
    for i in range(1,len(arr)):
        # Everytime we get a distinct element from the POV of res and i we update the values according to index (res)
        if arr[res-1] != arr[i]:
            arr[res] = arr[i]
            res += 1 # res is only updates when we find a new value so that we can make the array distinct
    return arr[:res]
