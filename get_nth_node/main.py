class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def get_nth(node, index):
    if node is None:
        raise ValueError('None linked list should throw error.')
    i = 0
    while node:
        if i == index:
            return node
        node = node.next
        i += 1
    raise ValueError('Invalid index value should throw error.')
