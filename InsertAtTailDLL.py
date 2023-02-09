def insertInTail(head, data):
  newNode = Node(data)
  if head == None:
    return newNode
  
  else:
    curr = head
    while curr.next != None:
      curr = curr.next
      curr.next = newNode
      newNode.prev = curr

      return head
