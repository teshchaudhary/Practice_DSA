def isIdentical(root1, root2):
        
        if root1 == None and root2 == None:
            return True
            
        elif (root1 == None and root2 != None) or (root1 != None and root2 == None):
            return False
            
        elif root1.data != root2.data:
            return False
        
        return isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)
