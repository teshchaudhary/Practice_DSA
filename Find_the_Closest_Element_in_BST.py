def find(root, K, l):
    if root == None:
        return
    
    elif root.data == K:
        l.append(0)
    
    elif root.data > K:
        l.append(abs(root.data-K))
        find(root.left, K, l)
    
    else:
        l.append(abs(root.data-K))
        find(root.right, K, l)

def minDiff(root, K):
        l = []
        find(root, K, l)
        
        return min(l)
