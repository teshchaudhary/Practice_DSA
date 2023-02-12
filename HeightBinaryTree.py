def height(root):
    if root == None:
        return 0

    return max(height(root.left), height(root.right))+1
