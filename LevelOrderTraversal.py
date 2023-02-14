

def height(root):
    if root == None:
        return 0
    return max((height(root.left), height(root.right)))+1

def printkth(root, k, l):
    if root == None:
        return
    
    if k == 0:
        l.append(root.data)
    
    printkth(root.left, k-1,l)
    printkth(root.right, k-1, l)

def traversal(head):
  h = height(root)
  for i in range(h):
    printkth(root,i,[])
