# Method 1

def reverseDLL(head):
    curr = head
    p = None
    
    while curr != None:
        n = curr.next
        curr.next = p
        curr.prev = n
        
        p = curr
        curr = curr.prev
    
    return p

# ------------------------------------------------------

# Method 2

def reverseDLL(head):
    curr = head
    
    while curr != None:
        curr.next, curr.prev = curr.prev, curr.next
        
        if curr.prev == None:
            return curr
        curr = curr.prev
