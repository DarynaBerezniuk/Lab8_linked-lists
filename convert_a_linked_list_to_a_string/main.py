class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
    output = ''
    while node:
        output += f'{node.data}'
        output += ' -> '
        node = node.next
    output += 'None'
    return output

stringify(Node(0, Node(1, Node(4, Node(9, Node(16))))))
