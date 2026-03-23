class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next

def linked_list_from_string(list_repr: str) -> Node | None:
    val_list = map(int, list_repr.split(' -> ')[:-1])
    head = Node(0)
    itr = head

    for val in val_list:
        itr.next = Node(val)
        itr = itr.next

    return head.next

