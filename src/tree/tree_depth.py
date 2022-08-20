from src.tree.tree_node import TreeNode


def get_depth_tree(root_node: TreeNode) -> int:
    if root_node is None:
        return 0

    depth_left = get_depth_tree(root_node.left_child)
    depth_right = get_depth_tree(root_node.right_child)

    if depth_left > depth_right:
        return depth_left + 1
    return depth_right + 1