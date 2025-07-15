from BinaryTreeNode import BinaryTreeNode
from enum import Enum

class Color(Enum):
    RED = "RED"
    BLACK = "BLACK"

class RedBlackTreeNode(BinaryTreeNode):

    def __init__(self, value: int, left, right, parent: BinaryTreeNode | None, color=Color.RED):

        super().__init__(value, left, right)
        self.color: str = color
        self.parent: RedBlackTreeNode = parent


class RedBlackTree():

    def __init__(self):
        self.root: RedBlackTreeNode = None
        self.total_nodes: int = 0

    def _rotate_right(self, pivot_point: RedBlackTreeNode) -> None:
        if pivot_point is None:
            raise Exception("Passed in node is of None value.")
        
        if pivot_point.left is None:
            raise Exception("No left child node to rotate with.")
        
        parent = pivot_point.parent
        parents_new_child = pivot_point.left
        parent.left = parents_new_child
        # Continue here


        pass

if __name__ == "__main__":
    node3 = RedBlackTreeNode(3, None, None, None)
    node4 = RedBlackTreeNode(4, None, None, None)
    node8: RedBlackTreeNode = RedBlackTreeNode(8, None, None, None)
    node7 = RedBlackTreeNode(7, None, None, None)
    node8.left = node4
    node4.parent = node8
    node4.left = node3
    node3.parent = node4
    node4.right = node7
    node7.parent = node4
    test_tree = RedBlackTree()
    test_tree.root = node8
    test_tree.total_nodes = 4
    x: int = 3
    pass


