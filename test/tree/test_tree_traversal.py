from src.tree.tree_node import TreeNode
from src.tree.tree_traversal import in_order_traversal, pre_order_traversal, post_order_traversal


def make_tree_nodes() -> TreeNode:
    """
    Function building and returning the following tree
                1
              /  \
            2     3
          /  \
        4     5
    """
    node1, node2, node3, node4, node5, node6 = TreeNode(1), TreeNode(2), TreeNode(3), \
                                               TreeNode(4), TreeNode(5), TreeNode(6)
    node1.left_child = node2
    node1.right_child = node3
    node2.left_child = node4
    node2.right_child = node5
    return node1


def test_in_order_traversal():
    root_node: TreeNode = make_tree_nodes()
    nodes_traversal: list[TreeNode] = in_order_traversal(root_node)
    assert len(nodes_traversal) == 5
    assert nodes_traversal == [4, 2, 5, 1, 3]


def test_pre_order_traversal():
    root_node: TreeNode = make_tree_nodes()
    nodes_traversal: list[TreeNode] = pre_order_traversal(root_node)
    assert len(nodes_traversal) == 5
    assert nodes_traversal == [1, 2, 4, 5, 3]


def test_post_order_traversal():
    root_node: TreeNode = make_tree_nodes()
    nodes_traversal: list[TreeNode] = post_order_traversal(root_node)
    assert len(nodes_traversal) == 5
    assert nodes_traversal == [4, 5, 2, 3, 1]
