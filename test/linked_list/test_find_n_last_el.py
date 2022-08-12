from src.linked_list.find_n_last_el import find_last_n_element
from src.linked_list.linked_list import LinkedList
from test.linked_list.utils import populate_linked_list_n_values


def test_find_last_n_element():
    linked_list = LinkedList()
    linked_list = populate_linked_list_n_values(linked_list, 10)
    last_n_element = find_last_n_element(linked_list, 3)
    assert last_n_element.data == 8
