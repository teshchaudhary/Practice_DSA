def inorderSuccessor(root, x):
        if root is None:
            return None
            
        res = None
        while root:
            if root.data > x.data:
                res = root
                root = root.left
            else:
                root = root.right
                
        return res
