import pytest
from data_structures.stack import Stack
from data_structures.queue import Queue

# тесты для класса Stack
def test_stack_creation():
    stack = Stack()
    assert stack.is_empty() == True
    assert len(stack) == 0


def test_stack_push():
    stack = Stack()
    stack.push(10)
    assert stack.is_empty() == False
    assert len(stack) == 1

    stack.push(20)
    assert len(stack) == 2


def test_stack_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.pop() == 3
    assert len(stack) == 2

    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.is_empty() == True


def test_stack_pop_empty():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()


def test_stack_peek():
    stack = Stack()
    stack.push(100)
    stack.push(200)

    assert stack.peek() == 200
    assert len(stack) == 2
    assert stack.peek() == 200


def test_stack_peek_empty():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.peek()


def test_stack_is_empty():
    stack = Stack()
    assert stack.is_empty() == True

    stack.push(42)
    assert stack.is_empty() == False

    stack.pop()
    assert stack.is_empty() == True


def test_stack_len():
    stack = Stack()
    assert len(stack) == 0

    stack.push(1)
    assert len(stack) == 1

    stack.push(2)
    stack.push(3)
    assert len(stack) == 3

    stack.pop()
    assert len(stack) == 2


def test_stack_order():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1


def test_stack_multiple_types():
    stack = Stack()
    stack.push(123)
    stack.push("строка")
    stack.push([1, 2, 3])
    stack.push({"key": "value"})

    assert stack.pop() == {"key": "value"}
    assert stack.pop() == [1, 2, 3]
    assert stack.pop() == "строка"
    assert stack.pop() == 123

# тесты для класса Queue
def test_queue_creation():
    queue = Queue()
    assert queue.is_empty() == True
    assert len(queue) == 0

def test_queue_enqueue():
    queue = Queue()
    queue.enqueue(10)
    assert queue.is_empty() == False
    assert len(queue) == 1
    queue.enqueue(20)
    assert len(queue) == 2

def test_queue_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.dequeue() == 1
    assert len(queue) == 2
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.is_empty() == True

def test_queue_dequeue_empty():
    queue = Queue()
    with pytest.raises(IndexError):
        queue.dequeue()

def test_queue_front():
    queue = Queue()
    queue.enqueue(100)
    queue.enqueue(200)
    assert queue.front() == 100
    assert len(queue) == 2
    assert queue.front() == 100
    queue.dequeue()
    assert queue.front() == 200

def test_queue_front_empty():
    queue = Queue()
    with pytest.raises(IndexError):
        queue.front()

def test_queue_is_empty():
    queue = Queue()
    assert queue.is_empty() == True
    queue.enqueue(42)
    assert queue.is_empty() == False
    queue.dequeue()
    assert queue.is_empty() == True

def test_queue_len():
    queue = Queue()
    assert len(queue) == 0
    queue.enqueue(1)
    assert len(queue) == 1
    queue.enqueue(2)
    queue.enqueue(3)
    assert len(queue) == 3
    queue.dequeue()
    assert len(queue) == 2

def test_queue_fifo():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3

def test_queue_multiple_types():
    queue = Queue()
    queue.enqueue(123)
    queue.enqueue("строка")
    queue.enqueue([1, 2, 3])
    queue.enqueue({"key": "value"})
    assert queue.dequeue() == 123
    assert queue.dequeue() == "строка"
    assert queue.dequeue() == [1, 2, 3]
    assert queue.dequeue() == {"key": "value"}
