

from dsa.node import Node, DllNode


def test_node_init():
    node = Node(10)
    assert node.data == 10
    assert node.next is None
    assert node.to_string() == "10 -> NULL"

    node.next = Node(20)
    assert node.data == 10
    assert node.next is not None
    assert node.next.data == 20
    assert node.next.next is None
    assert node.to_string() == "10 -> 20"

def test_dll_node_init():
    node = DllNode(10)
    assert node.data == 10
    assert node.prev is None
    assert node.next is None
    assert node.to_string() == "NULL -> 10 -> NULL"