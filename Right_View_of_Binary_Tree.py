def rightView(root):
        res = []
        res_ = []
        if root is None:
            return
        
        q = deque()
     
        q.append(root)
     
        while q:
            
            count = len(q)
    
            while count > 0:
                node = q.popleft()
                
                res_.append(node.data)
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    
                    q.append(node.right)
     
                count -= 1
                
            res.append(res_[-1])
            res_.clear()
        
        return res
