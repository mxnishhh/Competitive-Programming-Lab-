# A class to create a tree node
class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def max_depth(root):

    if root is None:
        return 0

    left_height = max_depth(root.left)

    right_height = max_depth(root.right)

    return max(left_height, right_height) + 1


root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


print("Height of tree =", max_depth(root))