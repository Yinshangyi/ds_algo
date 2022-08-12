from src.linked_list.linked_list import LinkedList, Node


def has_linked_list_loop(linked_list: LinkedList) -> bool:
    if not linked_list.head:
        return False
    nodes_list = set()
    current_node = linked_list.head
    while current_node:
        if current_node in nodes_list:
            return True
        nodes_list.add(current_node)
        current_node = current_node.next
    return False

