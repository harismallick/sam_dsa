
class BinaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value: int = value
        self.left: BinaryTreeNode | None = left
        self.right: BinaryTreeNode | None = right