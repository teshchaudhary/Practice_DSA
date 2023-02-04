def search(head,x):
    while head is not None:
        if head.data == x:
            return 1
        head = head.next
    
    return 0
