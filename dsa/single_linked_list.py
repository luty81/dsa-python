from dsa.node import Node

class SingleLinkedList:

    def __init__(self, data = None):
        self._reset_(data)


    def append(self, data):
        if self.head is None:
            self._reset_(data)
        else:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node

    def pop(self) -> Node:
        if self.head is None:
            return None
        
        if self.head is self.tail:
            return self._pop_one_and_reset_linked_list_()
        
        previous_node = None
        current_node = self.head
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next

        self.tail = previous_node
        self.tail.next = None

        return current_node
    
    def pop_first(self) -> Node:
        if self.head is None:
            return None
        
        if self.head is self.tail:
            return self._pop_one_and_reset_linked_list_()

        removed_node = self.head
        self.head = self.head.next
        removed_node.next = None
        return removed_node
    
    def prepend(self, data):
        if self.head is None:
            self._reset_(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def get(self, index):
        if index < 0 or self.head is None:
            return None
        
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
            if current_node is None:
                break
        
        return current_node

    def set(self, index, data):
        item = self.get(index)
        if item:
            item.data = data
            return True
        
        return False

    def insert_at(self, index, data):
        if index < 0:
            return False
        
        if index == 0:
            self.prepend(data)
        else:        
            item = self.get(index)
            if item:
                new_node = Node(data)
                new_node.next = item
                previous = self.get(index-1)
                previous.next = new_node
            else:
                self.append(data)        

        return True

    def remove_at(self, index):
        if index < 0:
            return False
        
        if index == 0:
            removed = self.pop_first()
            return removed is not None
        
        item_to_remove = self.get(index)        
        previous_item = self.get(index-1)
        if item_to_remove is self.tail:
            self.tail = previous_item
            self.tail.next = None
        else:
            previous_item.next = item_to_remove.next

        return True

    def reverse(self):
        if self.head is not None:
            current = self.head
            self.head = self.tail
            self.tail = current

            before = None
            after = current.next
            while current is not None and after is not None:
                after = current.next
                current.next = before
                before = current
                current = after


    def print_debug(self, before, current, after):
        msg = str(before.data) if before is not None else "None"
        msg = msg + " / " + str(current.data) if current is not None else "None"
        msg = msg + " / " + str(after.data) if after is not None else "None"
        print(msg)

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def to_string(self):
        result = ""
        arrow = ""        
        current = self.head
        processed_nodes = []        
        while current:
            result += f"{arrow}{current.data}"
            if current.next:
                result += f"->{current.next.data}"
            
            if current.data in processed_nodes:
                return f"{result[:-4]}->(...)"
            processed_nodes.append(current.data)

            current = current.next
            if current:
                current = current.next
        
            arrow = "->"

        return result

    def to_list(self):
        result = []
        current_node = self.head
        while current_node is not None:
            result.append(current_node.data)
            current_node = current_node.next
        
        return result


    def _reset_(self, data = None):
        new_node = Node(data) if data is not None else None
        self.head = new_node
        self.tail = new_node

    def _pop_one_and_reset_linked_list_(self):
        if self.head is self.tail:
            removed_item = self.head
            self._reset_()
            return removed_item
        
        return None
