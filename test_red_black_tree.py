import unittest
from RedBlackTree import RedBlackTreeNode, RedBlackTree, Color

class TestRBTree(unittest.TestCase):
    def setUp(self):
        self.rbtree = RedBlackTree()
        self.comparison_tree = RedBlackTree()

    def manual_rb_tree(self):
        # # case 1
    #     node_6 = RedBlackTreeNode(6, None, None, None, Color.BLACK)
    #     node_5 = RedBlackTreeNode(5, None, None, None, Color.BLACK)
    #     node_15 = RedBlackTreeNode(15, None, None, None, Color.RED)
    #     node_14 = RedBlackTreeNode(14, None, None, None, Color.BLACK)
    #     node_16 = RedBlackTreeNode(16, None, None, None, Color.BLACK)

    #     node_6.left = node_5
    #     node_5.parent = node_6

    #     node_6.right = node_15
    #     node_15.parent = node_6

    #     node_15.left = node_14
    #     node_14.parent = node_15

    #     node_15.right = node_16
    #     node_16.parent = node_15
        
    #     self.rbtree.root = node_6
    #     self.rbtree.total_nodes = 5

        # case 2
        node_23 = RedBlackTreeNode(23, None, None, None, Color.RED)
        node_19 = RedBlackTreeNode(19, None, None, None, Color.BLACK)
        node_13 = RedBlackTreeNode(13, None, None, None, Color.RED)
        node_9 = RedBlackTreeNode(9, None, None, None, Color.RED)
        node_12 = RedBlackTreeNode(12, None, None, None, Color.BLACK)
        node_15 = RedBlackTreeNode(15, None, None, None, Color.RED)
        node_5 = RedBlackTreeNode(5, None, None, None, Color.BLACK)
        node_8 = RedBlackTreeNode(8, None, None, None, Color.BLACK)

        node_23.parent = node_19
        node_19.right = node_23
        node_19.parent = node_15
        node_15.right = node_19
        
        node_13.parent = node_12
        node_12.right = node_13
        node_9.parent = node_12
        node_12.left = node_9
        node_12.parent = node_15
        node_15.left = node_12

        node_15.parent = node_8
        node_8.right = node_15

        node_5.parent = node_8
        node_8.left = node_5

        self.rbtree.root = node_8
        self.validate_rb_tree()
        pass

    def populate_tree(self, test_list=None):
        if test_list is not None:
            values = test_list
        else:
            values: list[int] = [10,4,2,7,1,3,6,8,9]
        for num in values:
            self.rbtree.insert_iter(num)
            self.rbtree.print_tree()

    def populate_comparison_tree(self, test_list=None):
        if test_list is not None:
            values = test_list
        else:
            values: list[int] = [10,4,2,7,1,3,6,8,9]
        for num in values:
            self.comparison_tree.insert_iter(num)
            self.comparison_tree.print_tree()

    def test_right_rotation_on_root(self):
        self.manual_rb_tree()
        
        self.rbtree._rotate_right(self.rbtree.root)
        
        root = self.rbtree.root
        left_child = root.left
        right_child = root.right

        self.assertEqual(root.value, 5)
        self.assertEqual(right_child.value, 8)
        self.assertEqual(left_child, None)
        self.assertEqual(right_child.left, None)
        
        return
    
    def test_right_rotation_on_child(self):
        self.manual_rb_tree()

        pivot: RedBlackTreeNode = self.rbtree.root.right
        pivot_parent = pivot.parent

        self.rbtree._rotate_right(pivot)

        # Check new child of pivot_parent:
        self.assertEqual(pivot_parent.right.value, 12)
        # Check that pivot is not right child of its former left child:
        self.assertEqual(pivot_parent.right.left.value, 9)
        # Check that pivot's former left's right subtree is now pivot's left subtree:
        self.assertEqual(pivot.right.value, 19)

        # Check that pivot's left child's parent is now pivot_parent:
        self.assertIs(pivot_parent.right.parent, pivot_parent)
        # Check that the old pivot's new parent is the new pivot:
        self.assertIs(pivot.parent, pivot_parent.right)
        # Check that new pivot's former right child's parent is now the old pivot:
        self.assertIs(pivot.right.parent, pivot)

        return

    def test_left_rotation_on_child(self):
        self.manual_rb_tree()

        pivot = self.rbtree.root.right
        pivot_parent = pivot.parent

        self.rbtree._rotate_left(pivot)

        # Check new child of pivot_parent:
        self.assertEqual(pivot_parent.right.value, 19)
        # Check that pivot is now the left child of its former right child:
        self.assertEqual(pivot_parent.right.left.value, 15)
        # Check that pivot's former right's left subtree is now pivot's right subtree:
        self.assertEqual(pivot.right, None)

        # Check that pivot's right child's parent is now pivot_parent:
        self.assertIs(pivot_parent.right.parent, pivot_parent)
        # Check that the old pivot's new parent is the new pivot:
        self.assertIs(pivot.parent, pivot_parent.right)
        # Check that new pivot's former left child's parent is now the old pivot:
        self.assertIs(pivot.right, None)

        return
    
    # Define helper functions to validate RB Tree:
    def traverse_tree(self, node: RedBlackTreeNode, black_node_count: set[int], count: int):
        if node is None:
            return black_node_count.add(count)

        # Check that red node only has black children:
        if node.color == Color.RED:
            if node.left is not None:
                self.assertEqual(node.left.color, Color.BLACK, "RULE BROKEN: Red node must have a black child.")
            if node.right is not None:
                self.assertEqual(node.right.color, Color.BLACK, "RULE BROKEN: Red node must have a black child.")

        count = count + 1 if node.color == Color.BLACK else count

        self.traverse_tree(node.left, black_node_count, count)
        self.traverse_tree(node.right, black_node_count, count)

    def validate_rb_tree(self):
        starting_node = self.rbtree.root
        
        # Validate rule 2:
        self.assertEqual(starting_node.color, Color.BLACK, "RULE BROKEN: Root node must be black.")

        black_node_count: set[int] = set()


        self.traverse_tree(self.rbtree.root, black_node_count, 0)

        # Check that only one element is in the set for a balanced RB Tree:
        self.assertEqual(len(black_node_count), 1, "RULE BROKEN: All paths from root to leaves must contain the same number of black nodes.")

        # Create our own test case to run the above tests:

        return

    # def test_validate_rb_tree_new_node_is_root(self):
    #     self.rbtree.insert_iter(8)
    #     self.assertEqual(self.rbtree.root.color, Color.BLACK)
    #     self.validate_rb_tree()
    #     return

    # def test_manual_rb_tree(self):
    #     self.manual_rb_tree()
    #     self.validate_rb_tree()

    # def test_populated_rb_tree(self):
    #     self.populate_tree()
    #     self.validate_rb_tree()

    def test_insert_on_empty_rbtree(self):
        self.rbtree.insert_iter(15)
        self.validate_rb_tree()
        self.rbtree.insert_iter(5)
        self.validate_rb_tree()
        self.rbtree.insert_iter(1)
        self.validate_rb_tree()

        self.assertEqual(self.rbtree.root.value, 5)
        self.assertEqual(self.rbtree.root.color, Color.BLACK)

        self.assertEqual(self.rbtree.root.left.value, 1)
        self.assertEqual(self.rbtree.root.left.color, Color.RED)
        
        self.assertEqual(self.rbtree.root.right.value, 15)
        self.assertEqual(self.rbtree.root.right.color, Color.RED)
        return
    
    def test_rbtree_insert_case_2_3_4(self):
        self.manual_rb_tree()
        self.rbtree.insert_iter(10)
        self.validate_rb_tree()
        self.assertEqual(self.rbtree.root.value, 12)
        self.assertEqual(self.rbtree.root.left.right.right.value, 10)

        return

    def test_lookup_on_custom_rbtree(self):
        self.populate_tree([10,5,30,1,7,25,40,20,28])

        return
    
    def test_delete_node_with_no_children(self):
        self.populate_tree([10,5,30,1,7,25,40,20,28])
        # self.rbtree.delete_node(1)
        
        self.validate_rb_tree()
        test = RedBlackTreeNode(10, None, None, None, Color.BLACK)
        self.assertEqual(self.rbtree.root, test)

        return

    def test_dunder_eq_of_rbtree_class_correct(self):
        self.populate_tree([10,5,30,1,7,25,40,20,28])
        self.populate_comparison_tree([10,5,30,1,7,25,40,20,28])

        self.assertEqual(self.rbtree, self.comparison_tree)
        return
    
    def test_dunder_eq_of_rbtree_class_incorrect(self):
        self.populate_tree([10,5,30,1,7,25,40,20,28])
        self.populate_comparison_tree([5,10,30,1,7,25,40,20,28])

        self.assertNotEqual(self.rbtree, self.comparison_tree)
        return

if __name__ == "__main__":
    unittest.main()