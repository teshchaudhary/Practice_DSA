def romanToDecimal(self, S): 
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        
        l = len(S)
        vals = [0]*l
        for i in range(l):
            vals[i] = d[S[i]]
        
        res = 0
        for i in range(1, l):
            num = 0
            if vals[i-1] >= vals[i]:
                num += vals[i-1]
            
            else:
                num -= vals[i-1]
            
            res += num
        
        res += vals[-1]
        return res
