
from exercises.sll_exercises import *
from tests.helpers import create_linked_list_from, assert_node

def test_find_middle_node():
    middle = find_middle_node(_in_([10, 20, 30, 40]))
    assert (middle.data, middle.next.data) == (30, 40)

    middle = find_middle_node(_in_([10, 20, 30]))
    assert (middle.data, middle.next.data) == (20, 30)

    middle = find_middle_node(_in_([10, 20]))
    assert (middle.data, middle.next) == (20, None)

    middle = find_middle_node(_in_([10]))
    assert (middle.data, middle.next) == (10, None)

    middle = find_middle_node(_in_([]))
    assert middle is None

def test_has_loop():
    sll = _in_([10, 20, 30, 40, 50])
    assert has_loop(sll) is False
    sll.pop()
    assert has_loop(sll) is False

    second_node = sll.head.next
    third_node = second_node.next
    third_node.next = second_node
    assert has_loop(sll) is True
    assert sll.to_string() == "10->20->30->20->30->(...)"


    sll = _in_([10, 20])
    assert has_loop(sll) is False

    sll.tail.next = sll.head
    assert has_loop(sll) is True
    assert sll.to_string() == "10->20->10->(...)"

    sll = SingleLinkedList(10)
    assert has_loop(sll) is False
    sll.tail.next = sll.head
    assert has_loop(sll) is True
    assert sll.to_string() == "10->10->10->(...)"

    assert has_loop(_in_([])) is False


def _in_(array):
   return create_linked_list_from(array)
 
