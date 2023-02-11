def reverseDLL(head):
    curr = head
    p = None
    
    while curr != None:
        n = curr.next
        curr.next = p
        curr.prev = n
        
        p = curr
        curr = curr.prev
    
    return p
