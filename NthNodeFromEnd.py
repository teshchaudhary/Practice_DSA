def length (head):
    count = 0
    while head is not None:
        head = head.next
        count += 1
    
    return count
    
def getNthFromLast(head,n):
    l = length(head)
    index = l - n
    i = 0
    
    while i<index:
        head = head.next
        i += 1
    
    if n <= 0 or n > l:
        return -1

    return head.data
