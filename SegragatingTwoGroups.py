# In this type of problem we can segragate different groups in an array like
# Positive and Negative
# Even and Odd
# Ones and Zeros

# Naive Approach
# O(n) Time and Space Complexity
def sort_(arr) :
    n = len(arr)
    temp = [0] * n 
    i = 0 
    for j in range(0,n) :
        if arr[j] < 0 :
            temp[i] = arr[j]
            i += 1 
            
    for j in range(0,n) :
        if arr[j] >= 0 :
            temp[i] = arr[j]
            i += 1 
    arr[:] = temp
    
    print(arr)
