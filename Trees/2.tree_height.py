# A class to create a tree node
class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Function to find height of the tree
def max_depth(root):

    # If there is no node, height is 0
    if root is None:
        return 0

    # Find height of left subtree
    left_height = max_depth(root.left)

    # Find height of right subtree
    right_height = max_depth(root.right)

    # Take the larger height and add 1
    return max(left_height, right_height) + 1


# Creating nodes
root = TreeNode(1)

root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


# Find height
print("Height of tree =", max_depth(root))