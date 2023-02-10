def findMiddle(head):
  slow = head
  fast = head
  while fast.next != head:
    slow = slow.next
    fast = fast.next.next

  return slow.data
