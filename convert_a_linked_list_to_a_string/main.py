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
