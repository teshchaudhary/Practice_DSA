def insertAtPosition(head,pos,data):
    i = 1
    curr = head
    newNode = Node(data)
    if head == None:
        newNode.next = newNode
        return newNode
    
    while i < pos:
        curr = curr.next
        i += 1
        if curr == head:
            return head
        
    newNode.next = curr.next
    curr.next = newNode
    return head
  
  # If index > length of linked list then return the original linked list
