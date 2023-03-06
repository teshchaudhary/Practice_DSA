class myHead:
    def __init__(self):
        self.arr = []

    def parent(self, i):
        return (i-1)//2

    def leftChild(self, i):
        return 2*(i+1)

    def rightChild(self, i):
        return 2*(i+2)
