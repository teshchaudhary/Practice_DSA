def findMoves(self,n,chairs,passengers):
        count = 0
        chairs.sort()
        passengers.sort()
        
        for i in range(n):
            count += abs(chairs[i]-passengers[i])
        
        return count
