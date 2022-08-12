from src.linked_list.linked_list import LinkedList
from src.linked_list.reverse import reverse_linked_list
from test.linked_list.utils import populate_linked_list_n_values


def test_reverse_linked_list():
    linked_list = LinkedList()
    linked_list = populate_linked_list_n_values(linked_list, 5)
    reversed_linked_list = reverse_linked_list(linked_list)
    expected_linked_status = "5 -> 4 -> 3 -> 2 -> 1"
    assert expected_linked_status == reversed_linked_list.get_representation()
