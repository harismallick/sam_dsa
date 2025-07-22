import unittest
from RedBlackTree import RedBlackTreeNode, RedBlackTree

class TestRBTree(unittest.TestCase):
    def setUp(self):
        self.rbtree = RedBlackTree()

    def populate_tree(self):
        values: list[int] = [8, 4, 2, 7, 1, 3]
        for num in values:
            self.rbtree.insert_iter(num)

    def test_right_rotation_on_root(self):
        self.populate_tree()
        
        self.rbtree._rotate_right(self.rbtree.root)
        
        root = self.rbtree.root
        left_child = root.left
        right_child = root.right

        self.assertEqual(root.value, 4)
        self.assertEqual(right_child.value, 8)
        self.assertEqual(left_child.value, 2)
        self.assertEqual(right_child.left.value, 7)
        pass


if __name__ == "__main__":
    unittest.main()