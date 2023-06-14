# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

def findAnagrams(s, p):
        k = len(p)
        res = []
        if k > len(s):
            return res

        count_p = [0] * 26
        count_s = [0] * 26

        for i in range(k):
            count_p[ord(p[i]) - 97] += 1

        for i in range(k):
            count_s[ord(s[i]) - 97] += 1

        if count_s == count_p:
            res.append(0)

        for i in range(k, len(s)):
            count_s[ord(s[i - k]) - 97] -= 1 
            count_s[ord(s[i]) - 97] += 1

            if count_s == count_p:
                res.append(i - k + 1)

        return res
      
# Eg: 
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
