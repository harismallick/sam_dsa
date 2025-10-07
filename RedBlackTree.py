from BinaryTreeNode import BinaryTreeNode
from enum import Enum

# Four rules of a RB Tree:
# 1. A node must be either red or black
# 2. Root node must be black
# 3. Red node can only have black children
# 4. All paths from root to leaves must contain the same number of black nodes
# 5. All NULL nodes are considered black

class Color(Enum):
    RED = "RED"
    BLACK = "BLACK"

class Direction(Enum):
    LEFT = "LEFT"
    RIGHT = "RIGHT"

class RedBlackTreeNode(BinaryTreeNode):

    def __init__(self, value: int, left, right, parent: BinaryTreeNode | None, color=Color.RED):

        super().__init__(value, left, right)
        self.color: str = color
        self.parent: RedBlackTreeNode = parent


class RedBlackTree():

    def __init__(self):
        self.root: RedBlackTreeNode = None
        self.total_nodes: int = 0

    def get_grandparent(self, node: RedBlackTreeNode) -> tuple[RedBlackTreeNode, Direction]:
        if node is None:
            return None
        
        if node.parent is None:
            return None
        
        if node.parent.parent is None:
            return None
        
        grandparent: RedBlackTreeNode = node.parent.parent
        if grandparent.left is node.parent:
            direction: Direction = Direction.LEFT
        else:
            direction = Direction.RIGHT

        return (grandparent, direction)
    
    def get_uncle(self, node: RedBlackTreeNode) -> tuple[RedBlackTreeNode, Direction]:
        grandparent, parent_direction = self.get_grandparent(node)
        uncle_direction: Direction = Direction.LEFT if parent_direction == Direction.RIGHT else Direction.RIGHT
        uncle: RedBlackTreeNode = None
        if uncle_direction == Direction.LEFT:
            uncle = grandparent.left
        else:
            uncle = grandparent.right
        return (uncle, uncle_direction)
    
    def get_node_direction_to_parent(self, node: RedBlackTreeNode) -> Direction:
        node_parent = node.parent
        if node_parent.left is node:
            return Direction.LEFT
        
        return Direction.RIGHT


    def insert_iter(self, value: int) -> None:
        print(f"Trying to insert {value}")
        new_node: RedBlackTreeNode = self.__insert_iter(value)
        self.fix_violations(new_node)
        return
    
    def __insert_iter(self, value: int) -> RedBlackTreeNode:   
        # This function is called 'iter' because we are using loop not recursion to insert the node.
        self.total_nodes += 1
        if self.root is None:
            self.root = RedBlackTreeNode(value, None, None, None)
            return self.root
        
        current_node = self.root
        previous_node = None
        while current_node is not None:
            previous_node = current_node
            if value <= current_node.value:
                current_node = current_node.left

            else:
                current_node = current_node.right

        new_node: RedBlackTreeNode = RedBlackTreeNode(value, None, None, previous_node)
        if value <= previous_node.value:
            previous_node.left = new_node
        else:
            previous_node.right = new_node
        
        return new_node

    def fix_violations(self, new_node: RedBlackTreeNode) -> None:
        if self.root is new_node:
            print("Violation Fix Case 1")
            self.root.color = Color.BLACK
            return

        violating_node = new_node
        while violating_node.parent and violating_node.parent.color == Color.RED:
            uncle, uncle_direction = self.get_uncle(violating_node)
            grandparent, grandparent_direction = self.get_grandparent(violating_node)
            if uncle and uncle.color == Color.RED:
                print("Violation Fix Case 2")
                uncle.color = Color.BLACK
                violating_node.parent.color = Color.BLACK
                grandparent.color = Color.RED
                violating_node = grandparent
                continue
            
            violating_node_direction = self.get_node_direction_to_parent(violating_node)
            if violating_node_direction != grandparent_direction:
                # case 3
                print("Violation Fix Case 3")
                violating_node = violating_node.parent
                if violating_node_direction == Direction.RIGHT:
                    self._rotate_left(violating_node)

                else:
                    self._rotate_right(violating_node)
                
            #case 4
            print("Violation Fix Case 4")
            violating_node_parent = violating_node.parent
            if grandparent_direction == Direction.RIGHT:
                self._rotate_left(grandparent)
            else:
                self._rotate_right(grandparent)

            # Change color of OG grandparent and parent
            grandparent.color = Color.RED
            violating_node_parent.color = Color.BLACK

        return

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

        if pivot_point.left is not None:
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

        if pivot_point.right is not None:
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


