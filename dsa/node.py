class Node:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

    def to_string(self):
        node_next = self.next.data if self.next is not None else "NULL"
        return f"{self.data} -> {node_next}"
        

class DllNode(Node):
    def __init__(self, data):
        super(DllNode, self).__init__(data)
        self.prev = None

    def to_string(self):
        node_prev = self.prev.data if self.prev is not None else "NULL"
        node_next = self.next.data if self.next is not None else "NULL"
        return f"{node_prev} -> {self.data} -> {node_next}"

