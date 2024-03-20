
from dsa.node import Node

class Stack:
    def __init__(self, value = None):
        new_node = Node(value)        
        self.top = new_node
        self.height = 1

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.height += 1
        return new_node
    
    def pop(self):
        if self.top is None:
            return None
        
        pop_item = self.top
        self.top = self.top.next
        self.height -= 1
        return pop_item

    def print_stack(self):
        current = self.top
        while current:
            print(current.data)
            current = current.next
        

