def DtB(n):
    while n>0:
        if n%2!=0:
            print(1, end = "")
        else:
            print(0, end = "")
        n//=2

DtB(21)