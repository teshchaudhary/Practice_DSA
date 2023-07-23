def removeDuplicates(head):
        d={}
        curr=head
        prev=None

        while(curr):
            
            d[curr.data]=1+d.get(curr.data,0)

            if d[curr.data] == 1:
                prev=curr
                curr=curr.next
                
            else:
                curr=curr.next
                prev.next=curr
                
        return head
