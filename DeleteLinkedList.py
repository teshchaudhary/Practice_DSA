def deleteHead(head):
    newHead = head.next
    head.next = None
    
    return newHead
  
  def deleteTail(head):
    curr = head
    
    if head == None:
        return
    
    while curr.next.next is not None:
        curr = curr.next
    
    curr.next = None
    return head
  
  def deleteAtPosition(head, pos):
    
    if pos == 1:
        newHead = head.next
        head.next = None
        return newHead
    i = 1
    curr = head
    while i < pos-1:
        curr = curr.next
        i += 1
    
    curr.next = curr.next.next
    
    return head
