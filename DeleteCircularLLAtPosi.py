def deleteAtPosition(head,pos):
    curr = head
    i = 0
    
    if pos == 1:
        head.data = head.next.data
        head.next = head.next.next
        
        return head
        
    
    while i < pos-2:
        curr = curr.next
        i += 1
    
    curr.next = curr.next.next
    return head
