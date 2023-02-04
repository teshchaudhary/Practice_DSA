def insertAtBegining(head,x):
        newHead = Node(x)
        newHead.next = head
        
        return newHead
            
def insertAtEnd(head,x):
        
    curr = head
    if head is None:
        return Node(x)
        
    while curr.next is not None:
        curr = curr.next
        
    curr.next = Node(x)
    return head
 
def len(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    
    return count
    
def insertAtPosition(head,pos,data):
    if pos > len(head):
        return head
        
    i = 1
    curr = head
    while i < pos:
        curr = curr.next
        i += 1
    
    newNode = Node(data)
    newNode.next = curr.next
    curr.next = newNode
    return head
