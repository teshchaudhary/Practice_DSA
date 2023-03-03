# def OddOccurence(arr):
#     for i in arr:
#         c = arr.count(i)
#         if c%2 != 0:
#             return i


# XOR Properties
# x^0 = x
# x^x = 0
# x^y^z = y^x^z = x^z^y = all other permutations

def OddOccurence(arr):
    res = 0
    for i in arr:
        res = res^i
    
    return res
print(OddOccurence([1,2,2,3,1])) 
