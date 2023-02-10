def deleteHead(head):
    newHead = head.next
    newHead.prev = None
    return newHead
