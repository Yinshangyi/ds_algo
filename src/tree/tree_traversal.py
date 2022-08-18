from src.tree.tree_node import TreeNode


def in_order_traversal(root_node: TreeNode) -> list:
    def in_order_with_list(root_node: TreeNode, values: list) -> list:
        if root_node is None:
            return
        in_order_with_list(root_node.left_child, values)
        values.append(root_node.value)
        in_order_with_list(root_node.right_child, values)

    values = []
    in_order_with_list(root_node, values)
    return values


def pre_order_traversal(root_node: TreeNode) -> list:
    def pre_order_with_list(root_node: TreeNode, values: list) -> list:
        if root_node is None:
            return
        values.append(root_node.value)
        pre_order_with_list(root_node.left_child, values)
        pre_order_with_list(root_node.right_child, values)

    values = []
    pre_order_with_list(root_node, values)
    return values


def post_order_traversal(root_node: TreeNode) -> list:
    def post_order_with_list(root_node: TreeNode, values: list) -> list:
        if root_node is None:
            return
        post_order_with_list(root_node.left_child, values)
        post_order_with_list(root_node.right_child, values)
        values.append(root_node.value)

    values = []
    post_order_with_list(root_node, values)
    return values
