


from typing import Tuple
from dsa.doubly_linked_list import DoublyLinkedList
from dsa.node import DllNode


def test_init():
    dll = DoublyLinkedList(10)
    h, t = dll.head, dll.tail
    assert (type(h), h.data, h.next) == (DllNode, 10, None)
    assert (type(t), t.data, t.next) == (DllNode, 10, None)
    assert dll.to_string() == "10"

def test_append():
    dll = DoublyLinkedList(10)
    dll.append(20)
    dll.append(30)
    dll.append(40)
    dll.append(50)

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
    dll = DoublyLinkedList(10)
    dll.prepend(20)
    dll.prepend(30)
    dll.prepend(40)
    dll.prepend(50)

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
    dll = DoublyLinkedList(10)
    dll.append(20)
    dll.append(30)
    dll.append(40)

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
    dll = DoublyLinkedList(10)
    dll.append(20)
    dll.append(30)
    dll.append(40)
    dll.append(50)

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


    




