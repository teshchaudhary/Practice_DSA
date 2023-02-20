def floor(root,x):
    res = -1
    while root != None:
        if root.data == x:
            return root.data
        
        elif x < root.data:
            root =  root.left
        
        else:
            res = root.data
            root = root.right
    
    
    return res
