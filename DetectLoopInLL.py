# If there is a loop then the slow and fast pointers will collide

def detectLoop(head):
    slow = fast = head
        
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
            
        if slow == fast:
            return True
            
    return False
