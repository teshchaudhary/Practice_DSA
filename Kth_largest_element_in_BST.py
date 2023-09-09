# Given a Binary Search Tree. Your task is to complete the function which will return the Kth largest element without doing any modification in Binary Search Tree.

def inOrder(root, l):
    if root is None:
        return
    
    inOrder(root.right, l)
    l.append(root.data)
    inOrder(root.left, l)
    
class Solution:
    def kthLargest(self,root, k):
        l = []
        inOrder(root,l)
        
        return l[k-1]
