def isSorted(li):
    l = len(li)
    for i in range(1,l):
        if li[i-1]>li[i]:
            return False
    
    return True

print(isSorted([1,8,2,3]))