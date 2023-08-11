# Extra Space

def missingNumber(arr,n):
      visited = [False]*(n+1)
      
      for i in range(n):
          if arr[i] > 0 and arr[i] <= n:
              visited[arr[i]] = True
      
      for i in range(1,n+1):
          if visited[i] == False:
              return i
      
      return n + 1

# Extra Space
def solution(A):

    # To know how long should be the check array
    m = max(A)

    if m < 1:
        return 1
    
    if len(A) == 1:
        # If it contains only one element
        return 2 if A[0] == 1 else 1
    
    l = [0] * m
    for i in range(len(A)):
        if A[i] > 0:
            if l[A[i] - 1] != 1:
                # Changing the value status at the index of our list
                l[A[i] - 1] = 1
    
    for i in range(len(l)):
        # Encountering first 0, i.e, the element with least value
        if l[i] == 0:
            return i + 1
            # In case all values are filled between 1 and m
    return i + 2


arr = [1,2,3,4,5]
print(solution(arr))
