def prntLLCir(head):
    l = []
    curr = head.next
    
    if head == None:
        return
    
    l.append(head.data)
    while curr != head:
        l.append(curr.data)
        curr = curr.next
    
    return l
