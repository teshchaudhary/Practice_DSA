import math

class myHead:
    def __init__(self):
        self.arr = []

    def parent(self, i):
        return (i-1)//2

    def leftChild(self, i):
        return 2*(i+1)

    def rightChild(self, i):
        return 2*(i+2)
    
    def minHeapify(self, i):
        arr = self.arr
        lt = self.leftChild(i)
        rt = self.rightChild(i)
        # Using it so that the recusion doesn't get to a place where the index is invalid
        n = len(arr)
        smallest = i  # Using the first node as the smallest initially

        # Making recursive calls to check which is the smallest among three (parent, leftchild, righchild)

        if lt < n and arr[lt] < arr[smallest]:
            smallest = lt

        if rt < n and arr[rt] < arr[smallest]:
            smallest = rt

        # if smallest is not i then we swap
        if smallest != i:
            arr[smallest], arr[i] = arr[i], arr[smallest]
            self.minHeapify(smallest)
    def extractMin(self):
        arr = self.arr
        n = len(arr)

        if n == 0:
            return math.inf

        res = arr[0]

        arr[0] = arr[-1]  # No need of swapping
        arr.pop()

        self.minHeapify(0)
        return res
