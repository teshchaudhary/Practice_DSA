def rearrange(arr, n):
    si, ei = 0, n-1

    maxi = arr[ei]+1

    for i in range(n):
        if i % 2 == 0:
            arr[i] += (arr[ei] % maxi)*maxi
            ei -= 1

        else:
            arr[i] += (arr[si] % maxi)*maxi
            si += 1

    for i in range(n):
        arr[i] = arr[i]//maxi
