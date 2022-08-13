class DataNode:
    def __init__(self, data: int):
        self.data: int = data
        self.next: DataNode = None


class Stack:
    def __init__(self):
        self.head: DataNode = None
        self.size = 0

    def __str__(self):
        current_node = self.head
        output = ""
        while current_node:
            output += str(current_node.data) + " --> "
            current_node = current_node.next
        return output[:-5]

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def peek(self):
        if self.is_empty():
            raise Exception("Peeking from an empty stack")
        return self.head.data

    def push(self, data: int):
        new_node = DataNode(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self) -> int:
        latest_node = self.head.data
        self.head = self.head.next
        self.size -= 1
        return latest_node
