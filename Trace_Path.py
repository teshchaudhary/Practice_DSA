def isPossible(self, n, m, s):
        
        l=r=u=d=0
        lr=0
        ud=0

        for i in s:
            if i=='L':
                lr-=1
                if lr<l:
                    l=lr

            elif i=='R':
                lr+=1
                if lr>r:
                    r=lr

            elif i=='U':
                ud+=1
                if ud>u:
                    u=ud

            else:
                ud-=1
                if ud<d:
                    d=ud
        
        return 0 if r-l+1>m or u-d+1>n else 1
