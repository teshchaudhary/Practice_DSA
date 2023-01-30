def LinearProbing(hashSize, arr, N):
    table = [-1] * hashSize

    for data in arr:
        iniKey = data % hashSize

        for i in range(hashSize):
            key = (iniKey+i) % hashSize

            if table[key] == -1:
                table[key] = data
                break

            elif table[key] == data:
                break

    return table


hashSize = 10
N = 4
arr = [4, 14, 24, 44]

print(LinearProbing(hashSize, arr, N))
