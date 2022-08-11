class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: Node = None


class LinkedList:
    def __init__(self):
        self.head: Node = None

    def push(self, data: int):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node: Node, new_data: int):
        if prev_node is None:
            print("The previous Node should be in the LinkedList")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data: int):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = new_node

    def get_representation(self):
        if self.head is Node:
            return "The LinkedList is empty"
        linked_list_status = ""
        current_node = self.head
        while current_node is not None:
            linked_list_status = linked_list_status + str(current_node.data) + " -> "
            current_node = current_node.next
        return linked_list_status[:-4]
