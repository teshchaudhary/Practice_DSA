# Every element will be present from 1-n if n is the maximum number in the array
# Only one element is repeated
# Find the repeating element

# O(n)

# The idea is to use the values of the array and make links
# Whenever the loop comes first then that element is repeated
# we can use the same approach for solving a problem where we have a loop in the linked list and we need to find the first element of that loop

def func(arr,n):
    slow = arr[0]
    fast = arr[0]

    slow = arr[slow]
    fast = arr[arr[fast]]

    while slow != fast:
        slow = arr[slow]
        fast = arr[arr[fast]]
    
    slow = arr[0]

    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    
    return fast # We can return slow as well

arr = [1, 2, 2, 3, 4, 5]
print(func(arr, 6))
