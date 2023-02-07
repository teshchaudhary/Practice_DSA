def deleteTail(head):
    curr = head
    while curr.next.next != head:
        curr = curr.next
    
    curr.next.next = None
    curr.next = head
    
    return head
