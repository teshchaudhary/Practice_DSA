class myHead:
    def __init__(self):
        self.arr = []

    def parent(self, i):
        return (i-1)//2

    def leftChild(self, i):
        return 2*(i+1)

    def rightChild(self, i):
        return 2*(i+2)

# O(log(N)), N is the number of element in the heap.
# First insert the element at the last of heap list.
# Now we have to maintain heap property.
# Compare the element with its parent and the swap if needed.
# We keep swapping until we find a node smaller the the element in case of a min heap.
# We also stop when we reach the root node.

    def insert(self, x):
        arr = self.arr
        arr.append(x)

        i = len(arr)-1

        while i > 0 and arr[self.parent] > arr[i]:  # i > 0 means reaching root node
            # other condition checks until we get an element lesser than the key

            p = self.parent(i)  # returns the index of parent at the moment
            arr[i], arr[p] = arr[p], arr[i]  # swapping
            i = p  # moving i to the new position to be compared with grandparent and so on
