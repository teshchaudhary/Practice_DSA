def reverse(head):
    curr = head
    prev = None

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


def lenl(head):
    res = 0
    curr = head
    while curr:
        res += 1
        curr = curr.next

    return res


def modify_the_list(head):
    mid = lenl(head) // 2
    head1 = head
    head2 = head
    prev = None

    i = 0
    while i < mid:
        prev = head2
        head2 = head2.next
        i += 1

    prev.next = reverse(head2)
    head2 = prev.next

    curr1 = head1
    curr2 = head2

    i = 0

    while i < mid:
        diff = curr2.data - curr1.data
        swap = curr1.data

        curr1.data = diff
        curr2.data = swap

        i += 1
        curr1 = curr1.next
        curr2 = curr2.next

    head2 = head

    prev = None
    i = 0
    while i < mid:
        prev = head2
        head2 = head2.next
        i += 1

    prev.next = reverse(head2)
    head2 = prev.next

    return head
