#POTD

def FirstNonRepeating(self, A):
	    check = [0]*26
	    stack = []
	    
	    res = ""
	    for i in A:
	        check[ord(i) - 97] += 1
        
            if check[ord(i) - 97] == 1:
                stack.append(i)
            
            if i in stack and check[ord(i)-97] != 1:
                stack.remove(i)
	   
	        if stack:
	            res += stack[0]
	        
	        else:
	            res += "#"
	    
	    return res
