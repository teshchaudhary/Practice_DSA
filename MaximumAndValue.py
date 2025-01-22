# Function to count how many elements in the array match the current bit pattern
# `bitPattern`: the current combination of set bits being tested
# `arr`: the array of numbers to check
# `N`: the size of the array
# The function iterates through the array and checks if the bit pattern is present in each element.
# It returns the count of elements that have all bits in the bit pattern set.
def countNumbersWithPattern(bitPattern, arr, N):
    count = 0
    for i in range(N):
        # Perform bitwise AND operation between bitPattern and arr[i].
        # If the result is equal to bitPattern, it means all bits in bitPattern are set in arr[i].
        if bitPattern == bitPattern & arr[i]:
            count += 1
    return count

# Function to find the maximum possible AND value for any pair of numbers in the array
# `arr`: the array of numbers
# `N`: the size of the array
# The goal is to find the largest AND value that can be formed by any two numbers in the array.
# The function checks each bit from the most significant bit (MSB) to the least significant bit (LSB),
# trying to maximize the AND value at every step.
def maxAND(self, arr, N):
    res = 0  # This will hold the result for the maximum AND value
    
    # Loop through bit positions from the 18th (MSB) to the 0th (LSB)
    for bitPosition in range(18, -1, -1):
        # Temporarily set the current bit in the result
        potentialAndValue = res | (1 << bitPosition)
        
        # Check how many elements in the array match the current bit pattern
        count = countNumbersWithPattern(potentialAndValue, arr, N)
        
        # If at least two elements have this bit pattern, it means we can use it to form the maximum AND value
        if count >= 2:
            # Update the result to include the current bit
            res = potentialAndValue
    
    # Return the maximum AND value
    return res
