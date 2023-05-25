# Given a sorted array of positive integers rearrange the array elements in a way that first element should be max value,
# second should be min value, third should be second max, fourth should be second min and so on.
# Modify the original array itself. Do it without using any extra space. You do not have to return anything

# Two values can be stored in a single value as

# Dividend = Divisor * Quotient + Remainder
# Divisor = Maximum number in element + 1
# Quotient = New Value Stored
# Remainder = Original Value

def rearrange(self, arr, n):
    si, ei = 0, n-1

    maxi = arr[ei]+1

    # To store two values in a single value
    for i in range(n):
        if i % 2 == 0:  # For even position the element will be the maximum one
            arr[i] += (arr[ei] % maxi)*maxi
            ei -= 1

        else:  # For odd position the element will be the minimum one
            arr[i] += (arr[si] % maxi)*maxi
            si += 1

    # This is to arrange the original value
    for i in range(n):
        arr[i] = arr[i]//maxi
