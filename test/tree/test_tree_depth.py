from src.tree.tree_node import TreeNode
from test.tree.test_tree_traversal import make_tree_nodes
from src.tree.tree_depth import get_depth_tree


def test_get_tree_depth():
    root_node: TreeNode = make_tree_nodes()
    tree_height = get_depth_tree(root_node)
    assert tree_height == 3
