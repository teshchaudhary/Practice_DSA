def compareCLL(head1,head2):
        n1 = head1
        n2 = head2
        while (n1.next != head1) and (n2.next != head2):
            if n1.data != n2.data:
                return 0
            
            n1 = n1.next
            n2 = n2.next
        
        if n1.data != n2.data:
            return 0
        return 1
