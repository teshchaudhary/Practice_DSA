#Naive Solution
# O(n^2)
def leftmost1(str):
    for i in range(len(str)):
        for j in range(i+1, len(str)):
            if str[i] == str[j]:
                return i
    
    return -1

# O(n)
def leftmost2(st) :
    count = [0] * 96
    for i in range(len(st)) :
        count[ord(st[i] - 97)] += 1 

    for i in range(len(st)) :
        if count[ord(st[i] - 97)] > 1:
            return i 
        
    return -1 
