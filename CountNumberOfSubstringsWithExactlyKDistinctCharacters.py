def func(S,k):
    l = 0
    r = 0

    distinct_count = 0
    arr = [0]*26
    res = 0
    while r < len(S):
        currentCharacter = ord(S[r]) - 97
        arr[currentCharacter] += 1

        # If count of the character is means there is a new character in the window
        if arr[currentCharacter] == 1:
            distinct_count += 1
        
        # Sliding Window
        # Keep removing the elements from left side of the window until distinct count is less than equal to k again
        while distinct_count > k:
            # Remove the element from left side of the window
            removedChar = ord(S[l]) - 97
            arr[removedChar] -= 1

            # Managing the distinct_count
            if arr[removedChar] == 0:
                distinct_count -= 1
        
            l += 1
        
        # Counts the number of substrings that can be made from a string of length(r-l)
        res += r-l+1
        r += 1
    
    return res

# Subtract atmost k-1 by atmost k to get exactly k
def substrCount (s, k):
        return atMostK(s,k)-atMostK(s,k-1)
