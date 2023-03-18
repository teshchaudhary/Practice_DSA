class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printLL(head):
    while head is not None:
        print(str(head.data) + " -> ",end = "")
        head = head.next
    print("None")
    return

def takeInput():
    
    inputList = [int(ele) for ele in input().split()]
    head = None
    tail = None
    
    for currData in inputList:
        if currData == -1:
            break
        
        newNode=Node(currData) 
        
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode # This will point the reference of previous node to the data of new node
            tail = newNode # Once the reference it done then the new tail will be the new Node
        
    return head

def length(head):
    slow = head
    fast = head.next
    length = 0
    while slow.next!= None and fast.next != None:
        if fast.next != None:
            length += 2
            
        elif slow.next != None:
            length += 1
            
        else:
            break
        slow = slow.next
        fast = fast.next
    
    print(length)
