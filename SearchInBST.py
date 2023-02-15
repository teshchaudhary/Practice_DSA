# Recursive
def search(node, x):
    if node == None:
            return False

    if node.data == x:
        return True
        
    elif node.data < x:
        return search(node.right, x)
        
    else:
        return search(node.left, x)

# Iterative
def search(root,x):
    while root is not None:
        if root.data == x:
            return True
        elif root.data < x:
            root = root.right
        else:
            root = root.left
    
    return False
