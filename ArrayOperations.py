def arrayOperations(n, arr):
    i = 0
    res = 0

    while i < n:

        if arr[i] == 0:
            while arr[i] == 0 and i < n-1:

                i += 1

        else:

            while arr[i] != 0 and i < n-1:
                i += 1

            res += 1

        i += 1

    return res
