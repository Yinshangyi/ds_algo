from src.tree.tree_is_sum import node_sum, is_sum_tree
from src.tree.tree_node import TreeNode
from test.tree.test_tree_traversal import make_tree_nodes


def test_node_sum():
    root_node = make_tree_nodes()
    nodes_sum = node_sum(root_node)
    assert nodes_sum == 15


def make_sum_tree_nodes() -> TreeNode:
    """
    Function building and returning the following tree
                  26
                /   \
              10     3
            /    \     \
          4      6      3
    """
    node26, node10, node4, node6, node3, node3child = TreeNode(26), TreeNode(10), TreeNode(4), \
                                                      TreeNode(6), TreeNode(3), TreeNode(3)
    node26.left_child = node10
    node10.left_child = node4
    node10.right_child = node6
    node26.right_child = node3
    node3.right_child = node3child
    return node26


def test_is_sum_tree():
    root_node = make_sum_tree_nodes()
    assert is_sum_tree(root_node) == True


def test_is_not_sum_tree():
    root_node = make_sum_tree_nodes()
    root_node.value = 30
    assert is_sum_tree(root_node) == False
