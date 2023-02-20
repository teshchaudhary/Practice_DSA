#----------------------------
def preOrder(root):
    res = []
    
    if root == None:
        return res
    
    res.append(root.val)
    res.extend(preOrder(root.left))
    res.extend(preOrder(root.right))
    
    return res
  
 
#------------------------------
def gen(root,res):
    if root == None:
        return
    
    gen(root.left, res)
    res.append(root.val)
    gen(root.right, res)
    
    return res
  
def InOrder(root):
    res = []
    
    return gen(root,res)

#-----------------------------
from collections import deque
def levelOrder(root):
    curr = root
    l = []
    q = deque()
    q.append(root)
    
    if root == None:
        return l
        
    while q:
        node = q.popleft()
        l.append(node.val)
        
        if node.left != None:
            q.append(node.left)
        if node.right != None:
            q.append(node.right)
            
    return l
