class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context:
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError("List must contain at least two nodes.")
    
    first = head
    second = head.next
    
    curr_first = first
    curr_second = second
    
    while curr_second and curr_second.next:
        curr_first.next = curr_second.next
        curr_first = curr_first.next
        curr_second.next = curr_first.next
        curr_second = curr_second.next
        
    curr_first.next = None
    if curr_second:
        curr_second.next = None
        
    return Context(first, second)
