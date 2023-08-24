# Given two numbers as strings s1 and s2. Calculate their Product.

# Note: The numbers can be negative and You are not allowed to use any built-in function or convert the strings to integers. There can be zeros in the begining of the numbers.

def multiply_strings(str1: str, str2: str):
    carry = 0
    res = 0
    digit_of_str2 = ord(str2) - ord('0')
    
    position_multiplier = 1
    length_of_str1 = len(str1)
    
    for i in reversed(range(length_of_str1)):
        digit_of_str1 = ord(str1[i]) - ord('0')
        
        product = digit_of_str2 * digit_of_str1 + carry
        carry = product // 10
        res += product % 10 * position_multiplier
        position_multiplier *= 10
    
    res += carry * position_multiplier
    
    return res
        
class Solution:
    def multiplyStrings(self,s1,s2):
        sign = 1
        
        if s1[0] == "-":
            sign *= -1
            s1 = s1[1:]
            
        if s2[0] == "-":
            sign *= -1
            s2 = s2[1:]
        
        res = 0
        position_multiplier = 1
        
        for i in reversed(range(len(s2))):
            res += multiply_strings(s1, s2[i])*position_multiplier
            position_multiplier *= 10
            
        return res*sign
