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
