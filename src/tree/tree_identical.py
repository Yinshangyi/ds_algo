from src.tree.tree_node import TreeNode


def are_trees_identical(first_tree_node: TreeNode, second_tree_node: TreeNode) -> bool:
    if (first_tree_node is None) and (second_tree_node is None):
        return True

    both_nodes_not_null = ((first_tree_node is not None) and (second_tree_node is not None))

    return both_nodes_not_null \
           and are_trees_identical(first_tree_node.left_child, second_tree_node.left_child) \
           and are_trees_identical(first_tree_node.right_child, second_tree_node.right_child)
