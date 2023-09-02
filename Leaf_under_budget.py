# Given a binary tree and a budget. Assume you are at the root of the tree(level 1), you need to maximise the count of leaf nodes you can visit in your budget if the cost of visiting a leaf node is equal to the level of that leaf node.

def getCount(root,budget):

        q=deque([root])
        lvl=0
        count=0
        ans=0
        while q:
            n=len(q)
            lvl+=1
            for i in range(n):
                temp=q.popleft()
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                if temp.left==None and temp.right==None:
                    count+=lvl
                    if count<=budget:
                        ans+=1
                    else:
                        break
        return ans
