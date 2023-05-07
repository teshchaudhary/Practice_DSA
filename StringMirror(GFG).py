def stringMirror(str: str) -> str:

    l = len(str)
    k = 1
    smallest_index = 0

    while k < l:
        if k == 1 and ord(str[k-1]) == ord(str[k]):
            break

        elif ord(str[k]) <= ord(str[smallest_index]):
            smallest_index = k

        else:
            break

        k += 1

    res = str[:smallest_index+1]

    return res + res[::-1]
