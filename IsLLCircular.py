def isCircular(head):
    curr = head
    while curr.next != head:
        if curr.next == None:
            return 0
        
        curr = curr.next
    
    return 1
