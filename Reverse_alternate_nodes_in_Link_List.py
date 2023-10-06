def rearrange(self, head):
        r1 = []
        r2 = []
        
        i = 0
        curr = head
        while curr:
            if i%2 == 0:
                r1.append(curr.data)
            
            else:
                r2.append(curr.data)
            i += 1
            curr = curr.next
        
        curr = head
        
        for i in r1:
            curr.data = i
            curr = curr.next
        
        while r2:
            d = r2.pop()
            curr.data = d
            curr = curr.next
        
        return head
