# Rotate Counter-Clockwise

def reverse(arr, si, ei):
    while si < ei:
        (arr[si], arr[ei]) = (arr[ei], arr[si])
        si += 1
        ei -= 1
    return arr

def rotateArr(self,A,D,N):
  D = D % N
  reverse(A, 0, D-1)
  reverse(A, D, N-1)
  reverse(A, 0, N-1)
