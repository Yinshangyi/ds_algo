from src.tree.tree_node import TreeNode


def node_sum(root_node: TreeNode) -> int:
    if root_node is None:
        return 0
    return root_node.value + node_sum(root_node.left_child) + node_sum(root_node.right_child)


def is_sum_tree(root_node: TreeNode) -> bool:
    if (root_node is None) or (root_node.left_child is None) or (root_node.right_child is None):
        return 1

    sum_left_sub_tree = node_sum(root_node.left_child)
    sum_right_sub_tree = node_sum(root_node.right_child)

    if (root_node.value == sum_left_sub_tree + sum_right_sub_tree) \
            and is_sum_tree(root_node.left_child) \
            and is_sum_tree(root_node.right_child):
        return True
    return False
