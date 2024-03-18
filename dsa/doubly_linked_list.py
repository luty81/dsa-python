

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
        
        node_to_remove = self.tail
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        node_to_remove.prev = None
        return node_to_remove


    def pop_first(self):
        if self.head is None:
            return None
        
        node_to_remove = self.head
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            
        node_to_remove.next = None
        return node_to_remove 
    
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

        