def LargButMinFreq(arr, n):
    d = {}

    for i in arr: d[i] = d.get(i, 0) + 1

    minFreq = min(d.values())

    res = 0

    for key in d.keys():

        if d[key] == minFreq and res < key:
            res = key

    return res
