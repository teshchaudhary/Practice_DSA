# Toggle the middle bits of the number
# if even bits then two middle bits
# else the middle bit

def num(N):
    res = 0
    while N:
        res += 1
        N >>= 1
    
    return res
    
def toggle(N):
    if N == 0:
        return 1
    l = num(N)
    mid = l//2
    if l % 2 == 0:
        n = 3 << mid-1
        return N ^ n
    else:
        n = 1<<mid
        return N ^ n
    
for i in range(int(input())):
    n = int(input())
    n = toggle(n)
    print(n)
