from src.linked_list.linked_list import LinkedList


def populate_linked_list_n_values(linked_list: LinkedList, n: int) -> LinkedList:
    nodes_value = [n for n in range(1, n + 1)]
    nodes_value = sorted(nodes_value, reverse=True)
    for node in nodes_value:
        linked_list.push(node)
    return linked_list
