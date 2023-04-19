# Return the index if element is found
# O(index_of_element)

def func(arr, ele):
    i = 0
    while True:
        if arr[i] == ele:
            return i

        elif arr[i] > ele:
            return -1
        
        i += 1
        

arr = list(range(1, 10000001))
print(func(arr,999))
