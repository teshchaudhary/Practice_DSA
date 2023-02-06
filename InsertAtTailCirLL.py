def insertInTail(head,data):
    newNode = Node(data)
    
    newNode.next = head.next
    head.next = newNode
    
    head.data, newNode.data = newNode.data, head.data
    return newNode
