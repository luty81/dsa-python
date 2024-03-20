from dsa.stack import Stack

def test_stack_init():
    stack = Stack(10)
    assert stack.height == 1
    assert stack.top.data == 10
    assert stack.top.next is None

def test_push():
    stack = Stack(10)
    new_item = stack.push(20)
    assert stack.top is new_item
    assert stack.top.data == 20
    assert stack.top.next.data == 10
    assert stack.top.next.next is None
    assert stack.height == 2

    stack.push(30)
    assert stack.top.data == 30
    assert stack.top.next.data == 20
    assert stack.top.next.next.data == 10
    assert stack.top.next.next.next is None
    assert stack.height == 3

def test_pop():
    stack = Stack(10)
    stack.push(20)
    stack.push(30)
    assert stack.top.data == 30
    assert stack.height == 3

    pop_item = stack.pop()
    assert pop_item.data == 30
    assert stack.top.data == 20
    assert stack.height == 2

    pop_item = stack.pop()
    assert pop_item.data == 20
    assert stack.top.data == 10
    assert stack.height == 1
    
    pop_item = stack.pop()
    assert pop_item.data == 10
    assert stack.top is None
    assert stack.height == 0

    pop_item = stack.pop()
    assert pop_item is None
    assert stack.top is None
    assert stack.height == 0