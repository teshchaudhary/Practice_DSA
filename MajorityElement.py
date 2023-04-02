# An element is considered a majority element if the element comes more than the half of the length of the array (freq(n) > length(arr)/2)
# Return the index of such element

# Naive Solution
# O(n^2)

def func1(arr):
    l = len(arr)
    threshold = l//2

    for i in range(len(arr)):
        count = 1

        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                count += 1

        if count > threshold:
            return i

    return -1

# Efficient Solution
# Boyer-Moore Majority Voting Algorithm
# We increase the count if the canditate element is equal to current element
# Otherwise decrease the count
# This works as if we the count decreases it means there are votes for other as well that reduces the chances to win

# We can also infer that if we divide the array into two
# One containing all the elements that cancels the votes
# Other containing that didn't cancel the votes
# We can see that in the first array will have pairs which can cancel each other if the pair is same as well even then it can come for maximum (n/2) times not more than that

# O(n)


def func2(arr, n):
    candidate = 0
    votes = 1

    # Finding a candidate
    for i in range(n):
        if (votes == 0):
            candidate = i
            votes = 1
        else:
            if (arr[i] == candidate):
                votes += 1
            else:
                votes -= 1

    # Checking if majority candidate occurs more than n/2 times
    count = 0

    for i in range(n):
        if (arr[candidate] == arr[i]):
            count += 1

    if (count < n // 2):
        candidate = -1
    return candidate
