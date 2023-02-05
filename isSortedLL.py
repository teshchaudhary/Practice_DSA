def isSorted(head):
    
    if head.next is None:
        return 1
    
    elif head.data == head.next.data and head.next is not None:
        head = head.next
        
    elif head.data < head.next.data:
        while head.next is not None:
            if head.data > head.next.data:
                return 0
            head = head.next
    
    else:
        while head.next is not None:
            if head.data < head.next.data:
                return 0
            head = head.next
    
    return 1
