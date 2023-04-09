# Given two arrays left and right
# We need to tell the maximum appearing element within the ranges
# ranges will be if first element of left array is 2 and first element of right array is 5 then range will be from 2 to 5 both inclusive

# O(N^Max)
# N is the number of ranges
# Max is the last element that can appear (in our case it is 100)

def func1(left, right):
    freq = [0]*100
    for i in range(len(left)):
        for j in range(left[i], right[i]+1):
            freq[j] += 1

    return freq.index(max(freq))
