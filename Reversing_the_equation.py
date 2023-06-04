def reverseEqn(s):
        sym = "+-*/"
        res = ""
        i = len(s)-1
        
        while i >= 0:
            num = ""
            if s[i] not in sym:
                j = i
                while s[j] not in sym and j >= 0:
                    num = s[j] + num
                    j -= 1
                
                i = j
                res = res + num
            
            else:
                res = res + s[i]
                i -= 1
        
        return res   

print(reverseEqn("20-3+5*2"))
