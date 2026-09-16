class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def count_internal_nodes(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 0

    return 1 + count_internal_nodes(root.left) + count_internal_nodes(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Internal nodes:", count_internal_nodes(root))