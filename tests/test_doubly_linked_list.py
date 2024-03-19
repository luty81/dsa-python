


from typing import List, Tuple
from dsa.doubly_linked_list import DoublyLinkedList
from dsa.node import DllNode


def test_init():
    dll = DoublyLinkedList(10)
    h, t = dll.head, dll.tail
    assert (type(h), h.data, h.next) == (DllNode, 10, None)
    assert (type(t), t.data, t.next) == (DllNode, 10, None)
    assert dll.to_string() == "10"

def test_append():
    dll = _doubly_linked_list_with_(5)

    assert dll.to_string() == "10 <=> 20 <=> 30 <=> 40 <=> 50"
    node = dll.head
    assert (node.prev, node.data, node.next.data) == (None, 10, 20)
    node = node.next
    assert (node.prev.data, node.data, node.next.data) == (10, 20, 30)
    node = node.next
    assert (node.prev.data, node.data, node.next.data) == (20, 30, 40)
    node = node.next
    assert (node.prev.data, node.data, node.next.data) == (30, 40, 50)
    node = node.next
    assert (node.prev.data, node.data, node.next) == (40, 50, None)

def test_prepend():
    dll = _reversed_doubly_linked_list_with_(5)

    assert dll.to_string() == "50 <=> 40 <=> 30 <=> 20 <=> 10"
    node = dll.head
    assert (node.prev, node.data, node.next.data) == (None, 50, 40)
    node = node.next
    assert (node.prev.data, node.data, node.next.data) == (50, 40, 30)
    node = node.next
    assert (node.prev.data, node.data, node.next.data) == (40, 30, 20)
    node = node.next
    assert (node.prev.data, node.data, node.next.data) == (30, 20, 10)
    node = node.next
    assert (node.prev.data, node.data, node.next) == (20, 10, None) 


def test_pop():
    dll = _doubly_linked_list_with_(4)

    removed_node = dll.pop()
    assert removed_node.data == 40
    assert (removed_node.prev, removed_node.next) == (None, None)
    assert dll.tail.data == 30
    assert dll.tail.prev.data == 20
    assert dll.tail.next is None

    removed_node = dll.pop()
    assert removed_node.data == 30
    assert (removed_node.prev, removed_node.next) == (None, None)
    assert dll.tail.data == 20
    assert dll.tail.prev.data == 10
    assert dll.tail.next is None

    removed_node = dll.pop()
    assert removed_node.data == 20
    assert (removed_node.prev, removed_node.next) == (None, None)
    assert dll.tail.data == 10
    assert dll.tail.prev is None
    assert dll.tail.next is None
    assert dll.head is dll.tail
    
    removed_node = dll.pop()
    assert removed_node.data == 10
    assert (removed_node.prev, removed_node.next) == (None, None)
    assert dll.tail is None
    assert dll.head is None

    assert dll.pop() is None


def test_pop_first():
    dll = _doubly_linked_list_with_(5)

    removed_node = dll.pop_first()
    assert removed_node.data == 10
    assert (removed_node.prev, removed_node.next) == (None, None)
    assert dll.head.data == 20
    assert dll.head.next.data == 30
    assert dll.head.prev is None

    removed_node = dll.pop_first()
    assert removed_node.data == 20
    assert (removed_node.prev, removed_node.next) == (None, None)
    assert dll.head.data == 30
    assert dll.head.next.data == 40
    assert dll.head.prev is None

    removed_node = dll.pop_first()
    assert removed_node.data == 30
    assert (removed_node.prev, removed_node.next) == (None, None)
    assert dll.head.data == 40
    assert dll.head.next.data == 50
    assert dll.head.prev is None

    removed_node = dll.pop_first()
    assert removed_node.data == 40
    assert (removed_node.prev, removed_node.next) == (None, None)
    assert dll.head.data == 50
    assert dll.head.next is None
    assert dll.head.prev is None
    assert dll.head is dll.tail

    removed_node = dll.pop_first()
    assert removed_node.data == 50
    assert (removed_node.prev, removed_node.next) == (None, None)
    assert dll.head is None
    assert dll.tail is None

    assert dll.pop_first() is None


def test_get():
    dll = _doubly_linked_list_with_(4)

    found_item = dll.get(0)
    assert found_item is not None
    assert found_item.data == 10
    assert found_item.prev is None
    assert found_item.next.data == 20
    assert found_item is dll.head

    found_item = dll.get(1)
    assert found_item is not None
    assert found_item.data == 20
    assert found_item.prev.data == 10
    assert found_item.next.data == 30

    found_item = dll.get(2)
    assert found_item is not None
    assert found_item.data == 30
    assert found_item.prev.data == 20
    assert found_item.next.data == 40

    found_item = dll.get(3)
    assert found_item is not None
    assert found_item.data == 40
    assert found_item.prev.data == 30
    assert found_item.next is None
    assert found_item is dll.tail

def test_get_index_out_of_bounds():
    dll = _doubly_linked_list_with_(4)
    assert dll.get(-1) is None
    assert dll.get(4) is None

def test_get_from_dll_with_one_element():
    dll = DoublyLinkedList(10)
    found_item = dll.get(0)
    assert found_item.data == 10
    assert found_item.prev is None
    assert found_item.next is None
    assert found_item is dll.head
    assert found_item is dll.tail

def test_set_by_index():
    dll = _doubly_linked_list_with_(3)
    assert dll.set(-1, 100) is False
    assert dll.to_string() == "10 <=> 20 <=> 30"
    
    assert dll.set(0, 15)
    assert dll.to_string() == "15 <=> 20 <=> 30"
    assert dll.head.data == 15

    assert dll.set(1, 25)
    assert dll.to_string() == "15 <=> 25 <=> 30"
    
    assert dll.set(2, 35)
    assert dll.to_string() == "15 <=> 25 <=> 35"
 
    assert dll.set(3, 40) is False
    assert dll.to_string() == "15 <=> 25 <=> 35"

def test_set_by_index_empty_dll():
    empty_dll = DoublyLinkedList(None)
    assert empty_dll.set(0, 10) is False
    assert empty_dll.to_string() == ""
    assert empty_dll.head is None
    assert empty_dll.tail is None

def test_insert_in_the_middle():
    dll = _doubly_linked_list_with_(4)
    
    assert dll.insert(1, 15)  
    assert _dll_is_expected_(dll, [10, 15, 20, 30, 40])
    
    assert dll.insert(3, 25) 
    assert _dll_is_expected_(dll, [10, 15, 20, 25, 30, 40])

    assert dll.insert(5, 35)
    assert _dll_is_expected_(dll, [10, 15, 20, 25, 30, 35, 40])

def test_insert_in_the_edges():
    dll = _doubly_linked_list_with_(3)

    assert dll.insert(0, 5)
    assert _dll_is_expected_(dll, [5, 10, 20, 30])
    assert dll.insert(4, 35)
    assert _dll_is_expected_(dll, [5, 10, 20, 30, 35])

def test_insert_in_single_dll():
    dll = DoublyLinkedList(10)
    assert dll.insert(0, 5)
    assert _dll_is_expected_(dll, [5, 10])

    dll = DoublyLinkedList(1)
    assert dll.insert(1, 2)
    assert _dll_is_expected_(dll, [1, 2])
    
def test_insert_in_an_empty_list():
    dll = DoublyLinkedList(None)
    assert dll.head is None
    assert dll.tail is None

    assert dll.insert(0, 10)
    assert _dll_is_expected_(dll, [10])
    


def _dll_is_expected_(actual_dll: DoublyLinkedList, expected: List):
    if any(expected):
        assert actual_dll.head.prev is None
        assert actual_dll.tail.next is None

        if len(expected) == 1:
            assert actual_dll.head.data == expected[0]
            assert actual_dll.tail is actual_dll.head
        else:
            assert actual_dll.head.data == expected[0]
            assert actual_dll.head.next.data == expected[1]
            assert actual_dll.tail.data == expected[-1]
            assert actual_dll.tail.prev.data == expected[-2]
        
        assert actual_dll.to_array() == expected
        return True
    
    return False


def _doubly_linked_list_with_(n_items: int):
    dll = DoublyLinkedList(10)
    for i in range(1, n_items, 1):
        dll.append((i+1)*10)
    return dll


def _reversed_doubly_linked_list_with_(n_items: int):
    dll = DoublyLinkedList(n_items*10)
    for i in range(n_items-1, 0, -1):
        dll.append(i*10)
    return dll


    




