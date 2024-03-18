from typing import List
from single_linked_list import Node, SingleLinkedList


def find_middle_node(sll: SingleLinkedList) -> Node:
    if sll.head is sll.tail:
        return sll.head

    slow_ptr = sll.head
    fast_ptr = sll.head
    while fast_ptr and fast_ptr.next: 
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    
    return slow_ptr

def has_loop(sll: SingleLinkedList) -> bool:
    if sll.head is None or sll.head.next is None:
        return False

    slow_ptr = sll.head
    fast_ptr = slow_ptr.next
    while slow_ptr and fast_ptr:
        if slow_ptr.next == fast_ptr.next:
            return True
        
        fast_ptr = fast_ptr.next
        if fast_ptr is None:
            slow_ptr = slow_ptr.next
            fast_ptr = slow_ptr.next

    return False
