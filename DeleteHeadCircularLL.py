def deleteHead(head):
    head.data =  head.next.data
    
    head.next = head.next.next
    return head
