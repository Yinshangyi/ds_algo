from src.stack.stack import Stack


def test_stack_creation():
    stack = Stack()
    assert stack.is_empty() == True


def test_push_data():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert str(stack) == "3 --> 2 --> 1"


def test_peek():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    latest_value = stack.peek()
    assert latest_value == 3


def test_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    latest_value = stack.pop()
    assert latest_value == 3
    assert stack.get_size() == 2
    assert str(stack) == "2 --> 1"