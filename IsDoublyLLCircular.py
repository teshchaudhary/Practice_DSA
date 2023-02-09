def isCircularDLL(head):
  curr = head
  while True:
    if curr.next == head:
      return 1
    elif curr.next == None:
      return 0
  
    curr = curr.next

def isCicularDLL(head):
  if head.prev == None:
    return 0
  else:
    return 1
