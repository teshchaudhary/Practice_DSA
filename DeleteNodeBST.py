# InOrder Successor of the node to be deleted.
# i.e. the nearest greater node of the node to be deleted.
# We can also pick the nearest smaller node of the node to be deleted.

def inOrderSuccessor(root):
    while root.left != None:
        root = root.left
    
    return root.data

def deleteNode(root, X):
    if root is None:
        return None
    
    
    elif root.data > X:
        root.left = deleteNode(root.left, X)
    
    elif root.data < X:
        root.right = deleteNode(root.right, X)
    
    else:
        if root.right == None:
            return root.left
            
        elif root.left == None:
            return root.right
        
        else:
            ele = inOrderSuccessor(root.right)
            root.data = ele
            root.right = deleteNode(root.right, ele)
    
    return root
