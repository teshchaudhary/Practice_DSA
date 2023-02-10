def deleteTail(head):
    curr = head
    while curr.next.next != None:
        curr = curr.next
    
    next = curr.next
    curr.next = None
    next.pev = None
    
    return head
