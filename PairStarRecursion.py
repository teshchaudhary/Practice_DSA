def pairStar(str,si):
    l = len(str)
    if si == l-1:
        return str
    if str[si]==str[si+1]:
        return str[si]+"*"+pairStar(str[1:], si+1)
    return str[si]+pairStar(str[1:], si+1)

print(pairStar("hello",0))
