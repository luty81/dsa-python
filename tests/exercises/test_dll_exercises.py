

from typing import List
from dsa.doubly_linked_list import DoublyLinkedList
from dsa.node import DllNode
from exercises.dll_exercises import *
from tests.helpers import create_doubly_linked_list_from


def test_swap_first_and_last_on_even_list():
    dll = create_doubly_linked_list_from([10, 20, 30, 40])
    assert swap_first_and_last(dll)
    assert dll.to_array() == [40, 20, 30, 10]
    assert swap_first_and_last(dll)
    assert dll.to_array() == [10, 20, 30, 40]
    
def test_swap_first_and_last_on_odd_list():
    dll = create_doubly_linked_list_from([10, 20, 30])
    assert swap_first_and_last(dll)
    assert dll.to_array() == [30, 20, 10]
    assert swap_first_and_last(dll)
    assert dll.to_array() == [10, 20, 30]

    dll.append(40)
    dll.append(50)
    assert swap_first_and_last(dll)
    assert dll.to_array() == [50, 20, 30, 40, 10]
    assert swap_first_and_last(dll)
    assert dll.to_array() == [10, 20, 30, 40, 50]

def test_swap_first_and_last_on_a_list_with_two_elements():
    dll = create_doubly_linked_list_from([10, 20])
    
    assert swap_first_and_last(dll)
    assert dll.to_array() == [20, 10]
    assert dll.head.data == 20
    assert dll.head.prev is None
    assert dll.head.next.data == 10
    assert dll.tail.data == 10
    assert dll.tail.prev.data == 20
    assert dll.tail.next is None

def test_swap_first_and_last_on_a_list_with_one_element():
    dll = DoublyLinkedList(10)
    
    assert swap_first_and_last(dll) is False
    assert dll.to_array() == [10]
    assert dll.head.data == 10
    assert dll.head.prev is None
    assert dll.head.next is None
    assert dll.tail is dll.head


def test_swap_first_and_last_on_empty_list():
    dll = DoublyLinkedList()
    
    assert swap_first_and_last(dll) is False
    assert dll.to_array() == []
    assert dll.head is None
    assert dll.tail is None

def test_swap_first_and_last_simple():
    dll = create_doubly_linked_list_from([10, 20, 30, 40])
    assert swap_first_and_last_simple(dll)
    assert dll.to_array() == [40, 20, 30, 10]

    dll.pop()
    assert dll.to_array() == [40, 20, 30]
    assert swap_first_and_last_simple(dll)
    assert dll.to_array() == [30, 20, 40]

    dll.pop()
    dll.pop_first()
    assert dll.to_array() == [20]
    assert swap_first_and_last_simple(dll) is False
    assert dll.to_array() == [20]

    empty_dll = DoublyLinkedList()
    assert swap_first_and_last_simple(empty_dll) is False
    assert empty_dll.head is None
    assert empty_dll.tail is None

def test_reverse():
    def assert_dll(head: DllNode):
        current_node = head
        assert current_node.prev is None
        assert current_node.next.data == 30
        
        current_node = current_node.next 
        assert current_node.prev.data == 40
        assert current_node.next.data == 20

        current_node = current_node.next 
        assert current_node.prev.data == 30
        assert current_node.next.data == 10

        current_node = current_node.next 
        assert current_node.prev.data == 20
        assert current_node.next is None

    dll = create_doubly_linked_list_from([10, 20, 30, 40])
    reverse(dll)
    assert dll.to_array() == [40, 30, 20, 10]
    assert_dll(dll.head)

    dll = create_doubly_linked_list_from([10, 20, 30, 40])
    reverse_using_pointers_swap(dll)
    assert dll.to_array() == [40, 30, 20, 10]
    assert_dll(dll.head)


def test_is_palindrome_odd_list():
    assert is_palindrome(_dll_([10, 20, 30, 20, 10])) is True
    assert is_palindrome(_dll_([10, 20, 10])) is True
    assert is_palindrome(_dll_([20])) is True

    assert is_palindrome(_dll_([10, 20, 30, 20, 11])) is False
    assert is_palindrome(_dll_([10, 20, 30, 21, 10])) is False
    assert is_palindrome(_dll_([10, 20, 11])) is False

def test_is_palindrome_even_list():
    assert is_palindrome(_dll_([10, 20, 30, 30, 20, 10])) is True
    assert is_palindrome(_dll_([10, 20, 20, 10])) is True
    assert is_palindrome(_dll_([20, 20])) is True

    assert is_palindrome(_dll_([10, 20, 30, 30, 20, 11])) is False
    assert is_palindrome(_dll_([10, 20, 30, 30, 21, 10])) is False
    assert is_palindrome(_dll_([10, 20, 30, 31, 20, 10])) is False
    assert is_palindrome(_dll_([10, 20, 31, 30, 20, 10])) is False
    assert is_palindrome(_dll_([10, 20, 20, 11])) is False
    assert is_palindrome(_dll_([10, 20, 21, 10])) is False
    assert is_palindrome(_dll_([10, 20])) is False

def test_is_palindrome_empty_list():
    assert is_palindrome(DoublyLinkedList()) is False

def _dll_(array: List):
    return create_doubly_linked_list_from(array)