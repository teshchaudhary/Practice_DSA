def insertInHead(head,data):
    newNode = Node(data)
    newNode.next = head.next
    head.next = newNode
    
    head.data, newNode.data = newNode.data, head.data
    
    return head
