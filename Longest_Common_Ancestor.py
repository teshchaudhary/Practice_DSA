def LCA(root, n1, n2):
    while True:
        if root.data < n1 and root.data < n2:
            root = root.right
        
        elif root.data > n1 and root.data > n2:
            root = root.left
        
        else:
            return root
