# Naive Solution

def height(root):
    if root == None:
        return 0
    return max((height(root.left), height(root.right)))+1

def printkth(root, k, l):
    if root == None:
        return
    
    if k == 0:
        l.append(root.data)
    
    printkth(root.left, k-1,l)
    printkth(root.right, k-1, l)

def traversal(root):
  h = height(root)
  for i in range(h):
    printkth(root,i,[])

    
# Efficient Solution

from collections import deque

def levelOrderTraversal(root):
    if root is None:
        return
    q = deque()
    q.append(root)
    
    while len(q) > 0:
        node = q.popleft()
        print(node.key)
        
        if node.left != None:
            q.append(root.left)
            
        if node.right != None:
            q.append(root.right)
