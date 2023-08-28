# We need to sort an array that contains three types of elements
# The different forms of the same question or approach can be

# Sort 0s, 1s and 2s
# Sort by a pivot (one chunk is lesser one is equal and one is greater)
# Sorted by a range like (5,10)
# (One chunk lessser than the range one between the range one greater than the range)

temp = []
def sortarr_(arr) :
    temp = []
    for x in arr :
        if x == 0 :
            temp.append(x)
    for x in arr :
        if x == 1 :
            temp.append(x)
    for x in arr :
        if x == 2 :
            temp.append(x)
    for i in range(len(arr)) :
        arr[i] = temp[i]
        
    return temp
    
arr = [0,1,1,2,0,1]
A = sortarr_(arr)
print(A)
