

from dsa.node import DllNode

class DoublyLinkedList:
    def __init__(self, data):
        self._reset_(data)
        

    def append(self, data):
        if self.head is None:
            self._reset_(new_node)
        else:
            new_node = DllNode(data)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def prepend(self, data):
        if self.head is None:
            self._reset_(data)
        else:        
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
        if index < 0:
            return None
        
        found_item = self.head
        for _ in range(index):
            if found_item is None:
                return None
            
            found_item = found_item.next

        return found_item

    def set(self, index, data):
        node = self.get(index)
        if node:
            node.data = data
            return True
        
        return False

    def insert(self, index, data):
        if index < 0:
            return False

        if index == 0:
            self.prepend(data)
        else:        
            node = self.get(index)
            if node:
                new_node = DllNode(data)
                new_node.next = node
                new_node.prev = node.prev
                node.prev.next = new_node
                node.prev = new_node
            else:
                node = self.get(index - 1)
                if node is None:
                    return False
            
                self.append(data)
        
        return True

    def remove(self, index):
        node = self.get(index)

        if self.head is self.tail:
            self._reset_(None)
            return node

        if node:
            if node is self.head:
                self.head = node.next
                self.head.prev = None
            elif node is self.tail:
                self.tail = node.prev
                self.tail.next = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            
            node.prev = None
            node.next = None
        
        return node

        
    def to_string(self):
        if self.head is None:
            return ""

        current = self.head
        result = f"{current.data}"
        current = current.next
        while current:
            result += f" <=> {current.data}"
            current = current.next

        return result
    
    def to_array(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result


    def _reset_(self, data = None):
        new_node = DllNode(data) if data is not None else None
        self.head = new_node
        self.tail = new_node