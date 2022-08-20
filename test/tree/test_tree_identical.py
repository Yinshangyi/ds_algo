from src.tree.tree_identical import are_trees_identical
from src.tree.tree_node import TreeNode
from test.tree.test_tree_traversal import make_tree_nodes


def test_are_trees_identical():
    root_node_1 = make_tree_nodes()
    root_node_2 = make_tree_nodes()
    are_identical = are_trees_identical(root_node_1, root_node_2)
    assert are_identical == True


def test_are_trees_not_identical():
    root_node_1 = make_tree_nodes()
    root_node_2 = make_tree_nodes()
    new_node = TreeNode(7)
    root_node_2.right_child.left_child = new_node
    are_identical = are_trees_identical(root_node_1, root_node_2)
    assert are_identical == False
