from dsa.doubly_linked_list import DoublyLinkedList

def swap_first_and_last(dll: DoublyLinkedList):
    if dll.head and dll.head is not dll.tail: 
        removed_head = dll.pop_first()
        dll.prepend(dll.pop().data)
        dll.append(removed_head.data)
        return True
    
    return False
        
def swap_first_and_last_simple(dll: DoublyLinkedList):
    if dll.head and dll.head is not dll.tail:
        old_head_data = dll.head.data
        dll.head.data = dll.tail.data
        dll.tail.data = old_head_data
        return True
    
    return False

def reverse(dll: DoublyLinkedList):
    current_node = dll.head
    while current_node:
        temp_next = current_node.next
        current_node.next = current_node.prev
        current_node.prev = temp_next
        current_node = temp_next

    temp_head = dll.head
    dll.head = dll.tail
    dll.tail = temp_head

def reverse_using_pointers_swap(dll: DoublyLinkedList):
    temp = dll.head
    while temp is not None:
        temp.prev, temp.next = temp.next, temp.prev
        temp = temp.prev
        
    dll.head, dll.tail = dll.tail, dll.head    

def is_palindrome(dll: DoublyLinkedList):
    if dll.head is None:
        return False
    
    if dll.head is dll.tail:
        return True

    fwd_pointer = dll.head
    rwd_pointer = dll.tail

    while fwd_pointer and rwd_pointer:
        if fwd_pointer.data != rwd_pointer.data:
            return False
        
        fwd_pointer = fwd_pointer.next
        rwd_pointer = rwd_pointer.prev
        if fwd_pointer is rwd_pointer:
            break
        
        if fwd_pointer.next is rwd_pointer:
            return fwd_pointer.data == rwd_pointer.data 
            
    return True






    



   