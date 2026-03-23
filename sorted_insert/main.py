class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def sorted_insert(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    
    if head.data > data:
        new_node.next = head
        return new_node

    itr = head
    while itr:
        if itr.next is None or itr.data < data < itr.next.data:
            new_node.next = itr.next
            itr.next = new_node
            return head
        itr = itr.next
