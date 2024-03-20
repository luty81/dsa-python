

from dsa.node import Node


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1
        return new_node
    
    def dequeue(self):
        if self.length == 0:
            return None

        dequeued = self.first
        self.first = self.first.next
        self.length -= 1
        if self.length == 0:
            self.first = None
            self.last = None
            
        return dequeued



    def print_queue(self):
        current = self.first
        while current:
            print(current.data)
            current = current.next

    def to_array(self):
        result = []
        current = self.first
        while current:
            result.append(current.data)
            current = current.next
        return result