from dsa.single_linked_list import SingleLinkedList
from tests import helpers as helper

def test_init():
    sll = SingleLinkedList(10)
    assert sll.head.data == 10
    assert sll.tail.data == 10
    assert sll.head is sll.tail
    

def test_append_in_empty_list():
    sll = SingleLinkedList()
    assert sll.head is None
    assert sll.tail is None

    sll.append(10)
    assert sll.head is sll.tail
    assert sll.head.next is None
    
def test_append():
    sll = SingleLinkedList(10)
    sll.append(20)
    sll.append(30)

    assert sll.head is not None
    assert sll.head.data == 10
    assert sll.head.next.data == 20
    assert sll.head.next.next is sll.tail
    assert sll.tail.data == 30
    assert sll.tail.next is None


def test_to_list():
    sll = helper.create_linked_list_from([10, 20, 30])
    _assert_linked_list_(sll, [10, 20, 30])


def test_pop():
    sll = helper.create_linked_list_from([10, 20, 30])
    _assert_linked_list_(sll, [10, 20, 30])

    assert sll.pop().data == 30
    _assert_linked_list_(sll, [10, 20])

    assert sll.pop().data == 20
    _assert_linked_list_(sll, [10])

    assert sll.pop().data == 10
    _assert_linked_list_(sll, [])

    assert sll.pop() is None
    _assert_linked_list_(sll, [])

def test_pop_first():
    sll = SingleLinkedList()
    assert sll.pop_first() is None

    sll = helper.create_linked_list_from([10, 20, 30])

    assert sll.pop_first().data == 10
    _assert_linked_list_(sll, [20, 30])
    assert sll.pop_first().data == 20
    _assert_linked_list_(sll, [30])
    assert sll.pop_first().data == 30
    _assert_linked_list_(sll, [])

    assert sll.pop_first() is None
    assert sll.head is None
    assert sll.tail is None


def test_get_by_index():
    assert SingleLinkedList().get(0) is None

    sll = helper.create_linked_list_from([10, 20, 30])
    helper.assert_node_data(sll.get(0), 10)
    helper.assert_node_data(sll.get(1), 20)
    helper.assert_node_data(sll.get(2), 30)
    assert sll.get(3) is None
    assert sll.get(-1) is None
    
def test_set_by_index():
    sll = helper.create_linked_list_from([10, 20, 30])
    assert sll.set(-1, 100) is False
    _assert_linked_list_(sll, [10, 20 , 30])

    assert sll.set(0, 15) is True
    _assert_linked_list_(sll, [15, 20, 30])

    assert sll.set(1, 25) is True
    _assert_linked_list_(sll, [15, 25, 30])
    
    assert sll.set(2, 35) is True
    _assert_linked_list_(sll, [15, 25, 35])

    assert sll.set(3, 40) is False
    _assert_linked_list_(sll, [15, 25, 35])

    empty_sll = SingleLinkedList()
    assert empty_sll.set(0, 10) is False
    _assert_linked_list_(empty_sll, [])


def test_insert_at():
    sll = helper.create_linked_list_from([10, 30])
    assert sll.insert_at(1, 25) is True
    _assert_linked_list_(sll, [10, 25, 30])
    assert sll.insert_at(0, 5) is True
    _assert_linked_list_(sll, [5, 10, 25, 30])
    assert sll.insert_at(4, 35) is True
    _assert_linked_list_(sll, [5, 10, 25, 30, 35])

def test_insert_at_empty_list():
    sll = SingleLinkedList()
    assert sll.insert_at(0, 10) is True
    _assert_linked_list_(sll, [10])
    assert sll.insert_at(0, 5)
    _assert_linked_list_(sll, [5, 10])


def test_remove_at_middle():
    sll = helper.create_linked_list_from([10, 20, 30, 40])
    assert sll.remove_at(2) is True
    _assert_linked_list_(sll, [10, 20, 40])
    assert sll.remove_at(1) is True
    _assert_linked_list_(sll, [10, 40])

def test_remove_at_end():
    sll = helper.create_linked_list_from([10, 20, 30])
    assert sll.remove_at(2) is True
    _assert_linked_list_(sll, [10, 20])
    assert sll.remove_at(1) is True
    _assert_linked_list_(sll, [10])

def test_remove_at_start():
    sll = helper.create_linked_list_from([10, 20, 30])
    assert sll.remove_at(0) is True
    _assert_linked_list_(sll, [20, 30])
    assert sll.remove_at(0) is True
    _assert_linked_list_(sll, [30])

def test_remove_at_until_empty():
    sll = helper.create_linked_list_from([10, 20])
    assert sll.remove_at(1) is True
    assert sll.remove_at(0) is True
    _assert_linked_list_(sll, [])

    sll = SingleLinkedList()
    assert sll.remove_at(0) is False


def test_reverse():
    sll = helper.create_linked_list_from([1, 2, 3])
    sll.reverse()
    _assert_linked_list_(sll, [3, 2, 1])

    sll = helper.create_linked_list_from([1, 2, 3, 4])
    sll.reverse()
    _assert_linked_list_(sll, [4, 3, 2, 1])

    sll = helper.create_linked_list_from([1, 2])
    sll.reverse()
    _assert_linked_list_(sll, [2, 1])

    sll = helper.create_linked_list_from([1])
    sll.reverse()
    _assert_linked_list_(sll, [1])

    sll = SingleLinkedList()
    sll.reverse()
    _assert_linked_list_(sll, [])

def test_prepend():
    sll = SingleLinkedList()
    sll.prepend(10)
    _assert_linked_list_(sll, [10])

    sll = helper.create_linked_list_from([20, 30, 40])
    sll.prepend(10)
    _assert_linked_list_(sll, [10, 20, 30, 40])


def test_to_string():
    sll = helper.create_linked_list_from([1, 2, 3, 4, 5])
    assert sll.to_string() == "1->2->3->4->5"

    sll = helper.create_linked_list_from([1, 2, 3, 4])
    assert sll.to_string() == "1->2->3->4"

    sll = helper.create_linked_list_from([1, 2])


def _assert_linked_list_(sll: SingleLinkedList, expected):
    assert expected == sll.to_list()
    if any(expected):
        assert sll.head.data == expected[0]
        assert sll.tail.data == expected[-1]
        assert sll.tail.next is None
    else:
        assert sll.head is None
        assert sll.tail is None


