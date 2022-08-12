from src.linked_list.linked_list import LinkedList, Node
from src.linked_list.loops import has_linked_list_loop


def test_has_linked_list_loop():
    linked_list = LinkedList()
    linked_list.head = Node(1)
    linked_list.head.next = Node(2)
    linked_list.head.next.next = Node(3)
    linked_list.head.next.next.next = Node(4)
    linked_list.head.next.next.next.next = linked_list.head.next.next
    has_loop = has_linked_list_loop(linked_list)
    assert has_loop == True


def test_has_no_linked_list_loop():
    linked_list = LinkedList()
    linked_list.head = Node(1)
    linked_list.head.next = Node(2)
    linked_list.head.next.next = Node(3)
    has_loop = has_linked_list_loop(linked_list)
    assert has_loop == False

