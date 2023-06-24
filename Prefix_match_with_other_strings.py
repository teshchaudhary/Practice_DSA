Given an array of strings arr[] of size n, a string str and an integer k. The task is to find the count of strings in arr[] whose prefix of length k matches with the k-length prefix of str.

def func(si, s, k):
    if (len(si) < len(s) and len(si) < k):
        return False
        
    for i in range(k):
        if s[i]!=si[i]:
            return False
            
    return True

class Solution:
    def klengthpref(self,arr,n,k,s):
        res = 0
        match = []
        
        if len(s) < k:
            return 0
            
        for i in arr:
            match.append(func(i, s, k))
        
        for i in match:
            if i == True:
                res += 1
        
        return res
