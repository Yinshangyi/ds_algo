from src.linked_list.linked_list import LinkedList
from src.linked_list.reverse import reverse_linked_list, reverse_linked_list_rec
from test.linked_list.utils import populate_linked_list_n_values


def test_reverse_linked_list():
    linked_list = LinkedList()
    linked_list = populate_linked_list_n_values(linked_list, 5)
    head_node = linked_list.head
    reversed_head_node = reverse_linked_list(head_node)
    reversed_list = LinkedList()
    reversed_list.head = reversed_head_node
    expected_linked_status = "5 -> 4 -> 3 -> 2 -> 1"
    assert expected_linked_status == reversed_list.get_representation()

def test_reverse_linked_list_rec():
    linked_list = LinkedList()
    linked_list = populate_linked_list_n_values(linked_list, 3)
    head_node = linked_list.head
    reversed_head_node = reverse_linked_list_rec(head_node)
    reversed_list = LinkedList()
    reversed_list.head = reversed_head_node
    expected_linked_status = "3 -> 2 -> 1"
    assert expected_linked_status == reversed_list.get_representation()
