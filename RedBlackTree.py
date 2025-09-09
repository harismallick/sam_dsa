from BinaryTreeNode import BinaryTreeNode
from enum import Enum

# Four rules of a RB Tree:
# 1. A node must be either red or black
# 2. Root node must be black
# 3. Red node can only have black children
# 4. All paths from root to leaves must contain the same number of black nodes

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


    def insert_iter(self, value: int) -> None:   
        self.total_nodes += 1
        if self.root is None:
            self.root = RedBlackTreeNode(value, None, None, None)
            return
        
        current_node = self.root
        previous_node = None
        while current_node is not None:
            previous_node = current_node
            if value <= current_node.value:
                current_node = current_node.left

            else:
                current_node = current_node.right

        if value <= previous_node.value:
            previous_node.left = RedBlackTreeNode(value, None, None, previous_node)
        else:
            previous_node.right = RedBlackTreeNode(value, None, None, previous_node)

    def _rotate_right(self, pivot_point: RedBlackTreeNode) -> None:
        if pivot_point is None:
            raise Exception("Passed in node is of None value.")
        
        if pivot_point.left is None:
            raise Exception("No left child node to rotate with.")
        
        parent = pivot_point.parent
        parents_new_child: RedBlackTreeNode = pivot_point.left

        if parent is None:
            self.root = parents_new_child

        elif parent.left is pivot_point:
            parent.left = parents_new_child

        else:
            parent.right = parents_new_child

        pivot_point.left = parents_new_child.right
        parents_new_child.right = pivot_point

        parents_new_child.parent = parent
        pivot_point.parent = parents_new_child
        pivot_point.left.parent = pivot_point

        return

    def _rotate_left(self, pivot_point: RedBlackTreeNode) -> None:
        if pivot_point is None:
            raise Exception("Passed in node is of None value.")
        
        if pivot_point.left is None:
            raise Exception("No left child node to rotate with.")
        
        parent = pivot_point.parent
        parents_new_child: RedBlackTreeNode = pivot_point.right

        if parent is None:
            self.root = parents_new_child

        elif parent.left is pivot_point:
            parent.left = parents_new_child

        else:
            parent.right = parents_new_child

        pivot_point.right = parents_new_child.left
        parents_new_child.left = pivot_point

        parents_new_child.parent = parent
        pivot_point.parent = parents_new_child
        pivot_point.right.parent = pivot_point

        return
    
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


