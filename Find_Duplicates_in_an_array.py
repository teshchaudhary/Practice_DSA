def duplicates(arr, n): 
        for i, a in enumerate(arr):
            arr[a % n] += n
        return [i for i, a in enumerate(arr) if a >= 2 * n] or [-1]
