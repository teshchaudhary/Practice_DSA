#LeetCode
# Missing Number

def missingNumber(nums):
    l = list(range(len(nums)+1))
    num = [x for x in l if x not in nums][0]
    return num
