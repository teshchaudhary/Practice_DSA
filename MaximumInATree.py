def maxt(root):
    if root == None:
        return -15411543513535646544334
    

    m = max(root.data, maxt(root.left), maxt(root.right))
    return m
