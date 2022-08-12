from src.linked_list.linked_list import LinkedList, Node


def test_linked_list_creation():
    linked_list = LinkedList()
    assert linked_list.head is None


def test_node_creation():
    node1 = Node(1)
    node2 = Node(2)
    assert node1.data == 1
    assert node1.next is None
    assert node2.data == 2
    assert node2.next is None


def init_nodes(linked_list: LinkedList):
    linked_list.head = Node(1)
    linked_list.head.next = Node(2)
    linked_list.head.next.next = Node(3)


def test_init_node():
    linked_list = LinkedList()
    init_nodes(linked_list)
    assert linked_list.head.data == 1
    assert linked_list.head.next.data == 2
    assert linked_list.head.next.next.data == 3
    assert linked_list.head.next.next.next is None


def test_print_linked_list():
    linked_list = LinkedList()
    init_nodes(linked_list)
    status_linked_list = linked_list.get_representation()
    assert status_linked_list == "1 -> 2 -> 3"


def test_push_node_beginning():
    linked_list = LinkedList()
    linked_list.push(1)
    linked_list.push(2)
    assert linked_list.head.data == 2
    assert linked_list.head.next.data == 1


def test_add_node_at_index():
    linked_list = LinkedList()
    linked_list.push(3)
    linked_list.push(1)
    linked_list.insert_after(linked_list.head, 2)
    assert linked_list.head.data == 1
    assert linked_list.head.next.data == 2
    assert linked_list.head.next.next.data == 3


def test_append_node():
    linked_list = LinkedList()
    linked_list.push(3)
    linked_list.push(2)
    linked_list.push(1)
    linked_list.append(4)
    assert linked_list.head.data == 1
    assert linked_list.head.next.data == 2
    assert linked_list.head.next.next.data == 3
    assert linked_list.head.next.next.next.data == 4


def test_get_count_nodes_iter():
    linked_list = LinkedList()
    linked_list.push(3)
    linked_list.push(2)
    linked_list.push(1)
    number_nodes = linked_list.get_count_iter()
    assert number_nodes == 3


def test_get_count_nodes_rec():
    linked_list = LinkedList()
    linked_list.push(3)
    linked_list.push(2)
    linked_list.push(1)
    number_nodes = linked_list.get_count_rec()
    assert number_nodes == 3
