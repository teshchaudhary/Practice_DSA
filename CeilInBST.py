def findCeil(root, inp):
    res = -1

    while root != None:
        if root.key == inp:
            return root.key

        elif inp < root.key:
            res = root.key
            root = root.left

        else:
            root = root.right

    return res
