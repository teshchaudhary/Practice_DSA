#Naive Solution

def func0(arr, n) :

	if (n == 1) :
	    return arr[0]
	if (arr[0] >= arr[1]) :
		return arr[0]
	if (arr[n - 1] >= arr[n - 2]) :
		return arr[n - 1]

	for i in range(1, n - 1) :
		if (arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]) :
			return arr[i]

# Getting all peak elements by Naive Method
def func(arr):
    l = len(arr)
    li = []
    if arr[0] >= arr[1]:
        li.append (arr[0])
        
    elif arr[l-1] > arr[l-2]:
        li.append (arr[l-1])
    
    for i in range(1,l-1):
         if arr[i-1] < arr[i] and arr[i]> arr[i+1]:
             li.append(arr[i]) 

    return li
# Efficient Solution

def func1(arr, n):

	l = 0
	r = n-1
	
	while(l <= r):

		mid = (l + r) // 2

		if((mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == n - 1 or arr[mid + 1] <= arr[mid])):
			break

		if(mid > 0 and arr[mid - 1] > arr[mid]):
			r = mid - 1

		else:
			l = mid + 1

	return mid
