def tribonacci(self, n: int) -> int:
    arr = [0, 1, 1]

    if n == 0:
        return arr[0]
    elif n == 1 or n == 2:
        return arr[1]

    elif n == 3:
        return arr[0]+arr[1]+arr[2]

    else:
        i = 3
        while i <= n:
            arr.append(arr[i-1]+arr[i-2]+arr[i-3])
            i += 1

        return arr[-1]
