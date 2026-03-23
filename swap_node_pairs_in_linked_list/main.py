class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    if head is None or head.next is None:
        return head

    placeholder = Node(head)

    itr = placeholder

    while itr.next and itr.next.next:
        first = itr.next
        second = itr.next.next

        itr.next = second
        first.next = second.next
        second.next = first

        itr = first

    return placeholder.next
