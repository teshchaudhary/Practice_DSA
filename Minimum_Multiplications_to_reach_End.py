# Given start, end and an array arr of n numbers. At each step, start is multiplied with any number in the array and then mod operation with 100000 is done to get the new start.

# Your task is to find the minimum steps in which end can be achieved starting from start. If it is not possible to reach end, then return -1.

def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        dist=[float('inf')]*(100000+1)
        q=[[start,0]]
        mod=100000
        
        while(len(q)):
            ele,st=q.pop(0)
            if(ele==end):
                return st
            for j in arr:
                ele2=(j*ele)%mod
                if(dist[ele2]>st+1):
                    dist[ele2]=st+1
                    q.append([ele2,st+1])
        return -1
