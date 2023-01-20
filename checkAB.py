def checkAB(s):
    l = len(s)
    if l == 0:
        return True

    if s[0] == "a":
        if len(s[1:]) > 1 and s[1:3] == "bb":
            return checkAB(s[3:])
        else:
            return checkAB(s[1:])
    else:
        return False


print(checkAB("abb"))
