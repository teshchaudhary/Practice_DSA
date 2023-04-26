# Convert the array into a palindrom e using the following operation: select an index i (1 ≤ i ≤ N) and add 1 to every element in the prefix of length i.

def func(arr):
    l = len(arr)
    si = 0
    ei = l-1

    diff = arr[ei] - arr[si]

    return diff if diff >= 0 else -1

n = int(input())
a = list(map(int, input().split()))
print(func(a))
