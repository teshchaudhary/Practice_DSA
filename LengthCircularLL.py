def length(head):
    count = 1
    
    curr = head.next
    while curr != head:
        count += 1
        curr = curr.next
    
    return count
