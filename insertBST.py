# Recursive Approach

def insert(root, Key):
    
    if root.left is None and Key < root.data :
        root.left = Node(Key)
        return root
    elif root.right is None and Key > root.data:
        root.right = Node(Key)
        return root
    
    if Key > root.data:
        insert(root.right, Key)
    
    elif Key < root.data:
        insert(root.left, Key)
    
    else:
        return root

    
# Iterative Approach

def insert(root, Key):
    parent = None
    curr = root
    
    while curr != None:
        parent = curr
        
        if curr.data == Key:
            return root
            
        elif Key > curr.data:
            curr = curr.right
            
        else:
            curr = curr.left
    
    if parent == None:
        return parent
    
    elif parent.data > Key:
        parent.left = Node(Key)
    
    else:
        parent.right = Node(Key)
    
    return root
