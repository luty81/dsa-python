

from dsa.node import DllNode

class DoublyLinkedList:
    def __init__(self, data):
        new_node = DllNode(data)
        self.head = new_node
        self.tail = new_node

    def append(self, data):
        new_node = DllNode(data)
        if self.head is None:
            self._set_head_and_tail_(new_node)
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
    
    def prepend(self, data):
        new_node = DllNode(data)
        if self.head is None:
            self._set_head_and_tail_(new_node)
            return
        
        new_node = DllNode(data)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        
        removed_node = self.tail
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        removed_node.prev = None
        return removed_node


    def pop_first(self):
        pass

    def get(self, index):
        pass

    def set(self, index, data):
        pass

    def insert(self, index, data):
        pass

    def remove(self, index):
        pass
        
        
    def to_string(self):
        current = self.head
        result = f"{current.data}"
        current = current.next
        while current:
            result += f" <=> {current.data}"
            current = current.next

        return result

    def _set_head_and_tail_(self, new_node: DllNode):
        self.head = new_node
        self.tail = new_node

        