
class Node:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SingleLinkedList:

    def __init__(self, data):
        new_node = Node(data)
        self.head = new_node
        self.tail = new_node

    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def print_head(self):
        head_next = self.head.next.data if self.head.next is not None else "NULL"
        print(f"HEAD: {self.head.data} -> {head_next}")

    def print_tail(self):
        tail_next = self.tail.next.data if self.tail.next is not None else "NULL"
        print(f"TAIL: {self.tail.data} -> {tail_next}")


