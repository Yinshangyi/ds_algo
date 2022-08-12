from src.linked_list.linked_list import LinkedList, Node


def find_last_n_element_rec():
    return None


def find_last_n_element(linked_list: LinkedList, position: int) -> Node:
    if linked_list.head is None:
        return None
    forward_node = linked_list.head
    backward_node = linked_list.head

    for step in range(0, position):
        if forward_node is None:
            return None
        forward_node = forward_node.next

    while forward_node is not None:
        forward_node = forward_node.next
        backward_node = backward_node.next

    return backward_node
