class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    new_list = Node(data)
    new_list.next = head
    return new_list

def build_one_two_three():
    built_list = None
    for i in range(3, 0, -1):
        built_list = push(built_list, i)
    return built_list

