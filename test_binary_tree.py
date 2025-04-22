import unittest
from binary_tree import BinarySearchTree

class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()

    def populate_tree(self):
        values: list[int] = [8, 4, 7, 3, 6, 5, 1, 2]
        for num in values:
            self.bst.insert_iter(num)

    
    def test_insert_iter_empty_tree(self):
        self.bst.insert_iter(8)

        self.assertEqual(self.bst.root.value, 8)
        self.assertEqual(self.bst.total_nodes, 1)

    def test_insert_iter_nonempty_tree(self):
        self.populate_tree()
        
        self.bst.insert_iter(11)        
        self.assertEqual(self.bst.root.right.value, 11)
        self.assertEqual(self.bst.total_nodes, 9)

        self.bst.insert_iter(0)
        self.assertEqual(self.bst.root.left.left.left.left.value, 0)
        self.assertEqual(self.bst.total_nodes, 10)

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

if __name__ == "__main__":
    unittest.main() 