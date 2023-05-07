def sort012(self,arr,n):
        zCount = 0
        oCount = 0
        tCount = 0
        
        for i in arr:
            if i == 0:
                zCount += 1
            
            elif i == 1:
                oCount += 1
            
            else:
                tCount += 1
                
        oCount += zCount
        tCount += oCount
        
        for i in range(zCount):
            arr[i] = 0
        
        for i in range(zCount,oCount):
            arr[i] = 1
            
        for i in range(oCount, tCount):
            arr[i] = 2
        
        return zCount, oCount, tCount
