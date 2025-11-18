import unittest
from BinaryTree import BinarySearchTree 
from BinaryTreeNode import BinaryTreeNode

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def populate_tree(self, test_list=None):
        if len(test_list) is not None:
            values = test_list
        else:
            values: list[int] = [8, 4, 7, 3, 6, 5, 1, 2]
        for num in values:
            self.bst.insert_iter(num)
    
    def validate_tree(self) -> bool:
        if self.bst.total_nodes == 0 or self.bst.total_nodes == 1:
            return True
        
        def traverse_and_validate_tree(bst_node: BinaryTreeNode):
            if bst_node is None:
                return True
            
            if bst_node.left is not None and bst_node.left.value > bst_node.value:
                return False
            
            if bst_node.right is not None and bst_node.right.value <= bst_node.value:
                return False

            left_validation: bool = traverse_and_validate_tree(bst_node.left)
            right_validation: bool = traverse_and_validate_tree(bst_node.right)

            return left_validation and right_validation

        return traverse_and_validate_tree(self.bst.root)

    
    def test_insert_iter_empty_tree(self):
        self.bst.insert_iter(8)

        self.assertEqual(self.bst.root.value, 8)
        self.assertEqual(self.bst.total_nodes, 1)

    def test_insert_iter_nonempty_tree(self):
        self.populate_tree()
        
        self.bst.insert_iter(11)        
        self.assertEqual(self.bst.root.right.value, 11)
        self.assertEqual(self.bst.total_nodes, 9)
        self.assertTrue(self.validate_tree())

        self.bst.insert_iter(0)
        self.assertEqual(self.bst.root.left.left.left.left.value, 0)
        self.assertEqual(self.bst.total_nodes, 10)
        self.assertTrue(self.validate_tree())

    def test_lookup_iter_empty_tree(self):
        self.assertEqual(self.bst.lookup_iter(5), False)

    def test_lookup_iter_nonempty_tree_success(self):
        self.populate_tree()

        self.assertEqual(self.bst.lookup_iter(6), True)
    
    def test_lookup_iter_nonempty_tree_fail(self):
        self.populate_tree()

        self.assertEqual(self.bst.lookup_iter(12), False)

    def test_dfs_pre(self):
        self.populate_tree()

        self.assertEqual(self.bst.dfs_pre(), [8,4,3,1,2,7,6,5])
    
    def test_dfs_in(self):
        self.populate_tree()

        self.assertEqual(self.bst.dfs_in(), [1,2,3,4,5,6,7,8])
    
    def test_dfs_post(self):
        self.populate_tree()

        self.assertEqual(self.bst.dfs_post(), [2,1,3,5,6,7,4,8])

    def test_lookup_node_root(self):
        self.populate_tree()

        previous, current = self.bst.lookup_node(8)

        self.assertEqual(previous, None)
        self.assertEqual(current.value, 8)

    def test_lookup_node_nonroot(self):
        self.populate_tree()

        previous, current = self.bst.lookup_node(3)

        self.assertEqual(previous.value, 4)
        self.assertEqual(current.value, 3)

    def test_lookup_node_leaf(self):
        self.populate_tree()

        previous, current = self.bst.lookup_node(5)

        self.assertEqual(previous.value, 6)
        self.assertEqual(current.value, 5)

    def test_lookup_node_emptytree(self):

        previous, current = self.bst.lookup_node(8)

        self.assertEqual(previous, None)
        self.assertEqual(current, None)

    def test_lookup_node_nonempty_fail(self):
        self.populate_tree()

        previous, current = self.bst.lookup_node(11)

        self.assertEqual(previous, None)
        self.assertEqual(current, None)

    def test_delete_node_w_no_child_from_populated_tree(self):
        self.populate_tree()

        self.bst.delete(5)
        self.assertEqual(self.bst.root.left.right.left.left, None)
        self.assertTrue(self.validate_tree())

    def test_delete_node_w_one_left_child_from_populated_tree(self):
        self.populate_tree()

        self.bst.delete(6)
        self.assertEqual(self.bst.root.left.right.left.value, 5)
        self.assertTrue(self.validate_tree())

    def test_delete_node_w_one_right_child_from_populated_tree(self):
        self.populate_tree()

        self.bst.delete(1)
        self.assertEqual(self.bst.root.left.left.left.value, 2)
        self.assertTrue(self.validate_tree())
    
    def test_delete_node_w_two_children_from_populated_tree(self):
        self.populate_tree()

        self.bst.delete(4)
        self.assertEqual(self.bst.root.left.value, 7)
        self.assertEqual(self.bst.root.left.left.left.left.value, 3)
        self.assertTrue(self.validate_tree())

    def test_get_min_max_height(self):
        self.populate_tree()

        min_height, max_height = self.bst.get_min_max_height()
        self.assertEqual(min_height, 1)
        self.assertEqual(max_height, 5)

    def test_delete_optimised_root_delete_successor_no_right_child(self):
        self.populate_tree([10,5,12,-1,6,11,14,7,13])
        self.bst.delete_optimised(10)

        self.assertEqual(self.bst.root.value, 11)
        self.assertEqual(self.bst.total_nodes, 8)
        self.assertEqual(self.bst.root.right.left, None)
        self.assertEqual(self.bst.root.left.value, 5)
        self.assertEqual(self.bst.root.right.value, 12)

        return
    
    def test_delete_optimised_root_delete_successor_with_right_child(self):
        self.populate_tree([10,5,13,-1,6,11,14,7,12,15])
        self.bst.delete_optimised(10)

        self.assertEqual(self.bst.root.value, 11)
        self.assertEqual(self.bst.total_nodes, 9)
        self.assertEqual(self.bst.root.right.left.value, 12)
        self.assertEqual(self.bst.root.left, 5)
        self.assertEqual(self.bst.root.right, 13)

        return

    def test_delete_optimised_delete_node_with_right_child_as_successor(self):
        self.populate_tree([10,5,13,-1,6,11,14,7,12,15])
        self.bst.delete_optimised(5)

        self.assertEqual(self.bst.root.value, 10)
        self.assertEqual(self.bst.total_nodes, 9)
        self.assertEqual(self.bst.root.left, 6)
        self.assertEqual(self.bst.root.left.right, 7)
        self.assertEqual(self.bst.root.left.left, -1)

if __name__ == "__main__":
    unittest.main() 