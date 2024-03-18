from typing import Tuple
from dsa.node import Node
from dsa.single_linked_list import SingleLinkedList

def create_linked_list_from(array):
    sll = SingleLinkedList()
    for value in array:
        sll.append(value)
    return sll

def assert_node(node: Node, expected: Tuple):
    assert node is not None 
    assert node.data == expected[0]
    if next is None:
        assert node.next is None
    else:
        assert node.next is not None
        assert node.next.data == expected[1]

def assert_node_data(node: Node, expected_data):
    assert node is not None
    assert node.data == expected_data
