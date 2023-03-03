def OddOccurece(arr):
    for i in arr:
        c = arr.count(i)
        if c%2 != 0:
            return i
