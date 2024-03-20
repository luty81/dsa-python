from dsa.queue import Queue

def test_queue_init():
    queue = Queue(10)
    assert queue.first.data == 10
    assert queue.first.next is None
    assert queue.last is queue.first
    assert queue.length == 1

def test_enqueue():
    queue = Queue(1)
    enqueued = queue.enqueue(2)
    assert enqueued.data == 2
    assert queue.first.data == 1
    assert queue.first.next is enqueued
    assert queue.last.data == 2 
    assert queue.last.next is None
    assert queue.last is enqueued
    assert queue.length == 2

    queue.enqueue(3)
    queue.enqueue(4)
    assert queue.first.data == 1
    assert queue.first.next.data == 2
    assert queue.last.data == 4
    assert queue.last.next is None
    assert queue.length == 4
    assert queue.to_array() == [1, 2, 3, 4]


def test_dequeue():
    queue = Queue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    dequeued = queue.dequeue()
    assert dequeued.data == 1
    assert queue.first.data == 2
    assert queue.last.data == 4
    assert queue.length == 3

    dequeued = queue.dequeue()
    assert dequeued.data == 2
    assert queue.first.data == 3
    assert queue.last.data == 4
    assert queue.length == 2
    
    dequeued = queue.dequeue()
    assert dequeued.data == 3
    assert queue.first.data == 4
    assert queue.last is queue.first
    assert queue.length == 1
    
    dequeued = queue.dequeue()
    assert dequeued.data == 4
    assert queue.first is None
    assert queue.last is None
    assert queue.length == 0

    assert queue.dequeue() is None


