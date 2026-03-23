class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    itr = head

    if itr is None or itr.next is None:
        return head
    
    while itr.next:
        if itr.data == itr.next.data:
            itr.next = itr.next.next
        else:
            itr = itr.next

    return head

