# An optimization over selection sort
# O(nlog(n))
# Not Stable
# Used in hybrid sort like intro sort

# Works in two steps
# 1.) Build a max heap
# 2.) Repeatedly swap root element with last node and reduce size of the heap by 1 and heapify

def heapify(self,arr, n, i):
    lt, rt = 2*i+1, 2*i+2
    largest = i
        
    if lt < n and arr[largest] < arr[lt]:
        largest = lt
        
    if rt < n and arr[largest] < arr[rt]:
        largest = rt
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        self.heapify(arr, n, largest)

def buildHeap(self,arr,n):
    p = (n-2)//2
    for i in range(p,-1,-1):
        self.heapify(arr,n,i)
    
def HeapSort(self, arr, n):
    self.buildHeap(arr,n)
    for i in range(n-1,0,-1):
        arr[i], arr[0] = arr[0], arr[i]
        self.heapify(arr,i,0)
