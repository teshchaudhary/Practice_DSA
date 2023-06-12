def Rearrange(self, n : int, arr : List[int]) -> None:
        res = []
        l = -1
        for i in arr:
            if i < 0:
                res.append(i)
                l += 1
        
        i = n-1
        j = -1
        while i >= 0:
            if arr[i] >= 0:
                arr[j] = arr[i]
                j -= 1
            
            i -= 1
    
        for i in range(len(res)):
            arr[i] = res[i]
        
        return arr
