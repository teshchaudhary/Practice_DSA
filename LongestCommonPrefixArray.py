def checkforTwo(s1,s2):
    res = ""
    l1 = len(s1)
    l2 = len(s2)
    i = j = 0
    
    while i != l1 and j != l2:
        if s1[i] == s2[j]:
            res = res + s1[i]
            i += 1
            j += 1
        
        else:
            break
    
    return res
    
def longestCommonPrefix(arr, n):
    if n == 1:
        return arr[0]

    res = checkforTwo(arr[0], arr[1])

    for i in range(2, n):
        res = checkforTwo(res, arr[i])

    if res:
        return res

    return -1
