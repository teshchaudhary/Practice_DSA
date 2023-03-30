def helper(s, si, ei):
    if si >= ei:
        return True

    if s[si] != s[ei]:
        return False

    return helper(s, si+1, ei-1)


def isPalindrome(s):
    l = len(s)
    si = 0
    ei = l-1
    if l == 0 or l == 1:
        return True

    return helper(s, si, ei)


print(isPalindrome("abaabaa"))
