def func(str):
    for i in range(len(str)):
        for j in range(i+1, len(str)):
            if str[i] == str[j]:
                return i
    
    return -1

print(func("abcd"))
