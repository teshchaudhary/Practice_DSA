def func(num):
    s = ""
    i = 0
    while i < len(num):
        number = num[i]
        freq = 0
        while(i< len(num) and num[i] == number):
            i+=1
            freq +=1
        s+= str(freq) + number
    return s

def countAndSay(n):
    s = "1"
    for i in range(n-1):
        s = func(s)
        return s
