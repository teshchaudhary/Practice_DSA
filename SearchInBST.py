def search(node, x):
    if node == None:
            return False

    if node.data == x:
        return True
        
    elif node.data < x:
        return search(node.right, x)
        
    else:
        return search(node.left, x)
