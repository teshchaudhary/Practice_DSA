def intersetPoint(head1,head2):
    l1 = l2 = 0
    
    curr = head1
    
    while curr:
        l1 += 1
        curr = curr.next
    
    curr = head2
    while curr:
        l2 += 1
        curr = curr.next
    
    if l1 > l2:
        diff = l1 - l2
        i = 0
        
        curr1 = head1
        curr2 = head2
        
        while diff:
            curr1 = curr1.next
            diff -= 1
            
        while curr1 != curr2:
            curr1 = curr1.next
            curr2 = curr2.next
    
    else:
        diff = l2 - l1
        i = 0
        
        curr1 = head1
        curr2 = head2
        
        while diff:
            curr2 = curr2.next
            diff -= 1
            
        while curr1 != curr2:
            curr1 = curr1.next
            curr2 = curr2.next
            
    
    if not curr1:
        return -1
    
    return curr1.data
