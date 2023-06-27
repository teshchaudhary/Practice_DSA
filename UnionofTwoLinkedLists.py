def union(head1,head2):
        tail = head1
        while tail.next != None:
            tail=tail.next
        
        tail.next = head2
        
        s = set()
        
        tail = head1
        while tail:
            s.add(tail.data)
            tail = tail.next
        
        s = sorted(s)
        
        head = linkedList()
        
        for i in s:
            head.insert(i)
        
        return head.head
