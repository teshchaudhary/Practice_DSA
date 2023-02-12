# Inorder

def generator(root, res):
    if root == None:
        return
    
    generator(root.left, res)
    res.append(root.data)
    generator(root.right, res)
    
    
def inOrder(root):
    l = []
    generator(root,l)
    return l

  
# PreOrder

def generator(root, res):
    if root == None:
        return
    
    res.append(root.data)
    generator(root.left, res)
    generator(root.right, res)
    
    
def preOrder(root):
    l = []
    generator(root,l)
    return l



# Post Order

def generator(root, res):
    if root == None:
        return
    
    generator(root.left, res)
    generator(root.right, res)
    res.append(root.data)
    

def postOrder(root):
    l = []
    generator(root,l)
    return l
