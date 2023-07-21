def reverse(self,head, k):
      curr = head
      prev = None
      
      i = k
      
      while curr and i > 0:
          nxt = curr.next
          curr.next = prev
          prev = curr
          curr = nxt
          i -= 1
          
      if curr:
          head.next = self.reverse(curr, k)
          
      return prev
