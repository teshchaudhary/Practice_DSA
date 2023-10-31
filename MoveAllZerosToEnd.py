# Given an array arr[] of n positive integers. Push all the zeros of the given array to the right end of the array while maintaining the order of non-zero elements. Do the mentioned change in the array in-place.


# Lomuto Partitioning
def pushZerosToEnd(arr, n):
  low = 0
  high = n-1
  pivot = 0

  i = (low - 1) 
  for j in range(low, high): 
      if (arr[j] != pivot): 
          i += 1 
          arr[i], arr[j] = arr[j], arr[i] 

  arr[i + 1], arr[high] = arr[high], arr[i + 1] 
  
  return arr
