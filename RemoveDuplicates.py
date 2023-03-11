def remDup(l):
    res = 1
    for i in range(1, 5):
        if l[res-1] != l[res]:
            l[res] = l[i]
            res += 1

    return l


print(remDup([1, 2, 2, 3, 4]))