import unittest
from RedBlackTree import RedBlackTreeNode, RedBlackTree, Color

class TestRBTree(unittest.TestCase):
    def setUp(self):
        self.rbtree = RedBlackTree()

    def populate_tree(self):
        values: list[int] = [10,4,2,7,1,3,6,8,9]
        for num in values:
            self.rbtree.insert_iter(num)

    def test_right_rotation_on_root(self):
        self.populate_tree()
        
        self.rbtree._rotate_right(self.rbtree.root)
        
        root = self.rbtree.root
        left_child = root.left
        right_child = root.right

        self.assertEqual(root.value, 4)
        self.assertEqual(right_child.value, 10)
        self.assertEqual(left_child.value, 2)
        self.assertEqual(right_child.left.value, 7)
        
        return
    
    def test_right_rotation_on_child(self):
        self.populate_tree()

        pivot: RedBlackTreeNode = self.rbtree.root.left
        pivot_parent = pivot.parent

        self.rbtree._rotate_right(pivot)

        # Check new child of pivot_parent:
        self.assertEqual(pivot_parent.left.value, 2)
        # Check that pivot is not right child of its former left child:
        self.assertEqual(pivot_parent.left.right.value, 4)
        # Check that pivot's former left's right subtree is now pivot's left subtree:
        self.assertEqual(pivot.left.value, 3)

        # Check that pivot's left child's parent is now pivit_parent:
        self.assertIs(pivot_parent.left.parent, pivot_parent)
        # Check that the old pivot's new parent is the new pivot:
        self.assertIs(pivot.parent, pivot_parent.left)
        # Check that new pivot's former right child's parent is now the old pivot:
        self.assertIs(pivot.left.parent, pivot)

        return

    def test_left_rotation_on_child(self):
        self.populate_tree()

        pivot = self.rbtree.root.left
        pivot_parent = pivot.parent

        self.rbtree._rotate_left(pivot)

        # Check new child of pivot_parent:
        self.assertEqual(pivot_parent.left.value, 7)
        # Check that pivot is now the left child of its former right child:
        self.assertEqual(pivot_parent.left.left.value, 4)
        # Check that pivot's former right's left subtree is now pivot's right subtree:
        self.assertEqual(pivot.right.value, 6)

        # Check that pivot's right child's parent is now pivot_parent:
        self.assertIs(pivot_parent.left.parent, pivot_parent)
        # Check that the old pivot's new parent is the new pivot:
        self.assertIs(pivot.parent, pivot_parent.left)
        # Check that new pivot's former left child's parent is now the old pivot:
        self.assertIs(pivot.right.parent, pivot)

        return
    
    # Define helper functions to validate RB Tree:
    def traverse_tree(self, node: RedBlackTreeNode, black_node_count: set[int], count: int):
        if node is None:
            return black_node_count.add(count)

        # Check that red node only has black children:
        if node.color == Color.RED:
            if node.left is not None:
                self.assertEqual(node.left.color, Color.BLACK)
            if node.right is not None:
                self.assertEqual(node.right.color, Color.BLACK)

        count = count + 1 if node.color == Color.BLACK else count

        self.traverse_tree(node.left, black_node_count, count)
        self.traverse_tree(node.right, black_node_count, count)

    def validate_rb_tree(self):
        starting_node = self.rbtree.root
        
        # Validate rule 2:
        self.assertEqual(starting_node.color, Color.BLACK)

        black_node_count: set[int] = set()


        self.traverse_tree(self, self.rbtree.root, black_node_count, 0)

        # Check that only one element is in the set for a balanced RB Tree:
        self.assertEqual(len(black_node_count), 1)

        # Create our own test case to run the above tests:

        return

if __name__ == "__main__":
    unittest.main()