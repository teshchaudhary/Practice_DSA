# Given a Binary Search Tree, modify the given BST such that it is balanced and has minimum possible height. Return the balanced BST.

class Node:
     def __init__(self, data):
          self.data = data
          self.left = None
          self.right = None

def BSTMaker(l):
        if not l:
            return None
        
        mid = len(l)//2
        root = Node(l[mid])
        root.left, root.right = BSTMaker(l[:mid]), BSTMaker(l[mid+1:])

        return root
    
def InOrder(root, l):
    if root is None:
        return
    
    InOrder(root.left, l)
    l.append(root.data)
    InOrder(root.right, l)
    return l
    
def buildBalancedTree(root):
    l = InOrder(root, [])
    
    return BSTMaker(l)
