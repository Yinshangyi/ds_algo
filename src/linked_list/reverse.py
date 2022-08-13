from src.linked_list.linked_list import Node


def reverse_linked_list(head_node: Node) -> Node:
    prev_node = None
    current_node = head_node
    while current_node is not None:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node
    return prev_node


def reverse_linked_list_rec(head_node: Node) -> Node:
    # If head is empty or has reached the list end
    if head_node is None or head_node.next is None:
        return head_node
    # Reverse the rest list
    rest = reverse_linked_list_rec(head_node.next)

    # Put first element at the end
    head_node.next.next = head_node
    head_node.next = None

    # Fix the header pointer
    return rest
