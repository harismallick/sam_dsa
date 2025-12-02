import random
from BinaryTreeNode import BinaryTreeNode

class BinarySearchTree:
    def __init__(self):
        self.root: BinaryTreeNode | None = None
        self.total_nodes: int = 0

    def insert_iter(self, value: int) -> None:   
        # This function is called 'iter' because we are using loop not recursion to insert the node.
        self.total_nodes += 1
        if self.root is None:
            self.root = BinaryTreeNode(value)
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
            previous_node.left = BinaryTreeNode(value)
        else:
            previous_node.right = BinaryTreeNode(value)

    def lookup_iter(self, value: int) -> bool:
        _, current = self.lookup_node(value)
        if current is not None:
            return True
        return False

    def lookup_node(self, value: int) -> tuple[BinaryTreeNode | None, BinaryTreeNode | None]:
        if self.root is None:
            return None, None

        current_node = self.root
        previous_node = None
        while current_node is not None:
            if value < current_node.value:
                previous_node = current_node
                current_node = current_node.left

            elif value > current_node.value:
                previous_node = current_node
                current_node = current_node.right
            
            elif value == current_node.value:
                return (previous_node, current_node)            

        return None, None
    
    # def count_child_nodes(self, node) -> tuple[]:

    #     count: int = 0
    #     if node.left is not None:
    #         count += 1
    #     if node.right is not None:
    #         count += 1

    #     return count
    
    def delete(self, value: int) -> None:
        parent, current = self.lookup_node(value)
        is_current_right_of_parent: bool = True if parent.right is current else False

        if current is None:
            raise Exception("The number does not exist. Nothing to delete.")
        
        if current.left is not None and current.right is not None:
            new_left_subtree = current.left
            new_right_subtree = current.right
            if is_current_right_of_parent:
                parent.right = new_right_subtree
            else:
                parent.left = new_right_subtree

            right_subtree_leaf = new_right_subtree

            while right_subtree_leaf.left is not None:
                right_subtree_leaf = right_subtree_leaf.left
            
            right_subtree_leaf.left = new_left_subtree

        elif current.left is not None or current.right is not None:
            child_node_of_current = current.left if current.left is not None else current.right
            if is_current_right_of_parent:
                parent.right = child_node_of_current
            else:
                parent.left = child_node_of_current
            
        else:
            if is_current_right_of_parent:
                parent.right = None
            else:
                parent.left = None

        self.total_nodes -= 1
        return

    def delete_optimised(self, value: int) -> None:

        parent, current = self.lookup_node(value) # Current is the node to delete
        
        if parent is None:
            root_delete: bool = True
        else:
            is_current_right_of_parent: bool = True if parent.right is current else False
            root_delete = False


        # Does the node to delete have any children?
        if current.left is None and current.right is None:
            if root_delete:
                self.root = None
            
            if is_current_right_of_parent:
                parent.right = None
            else:
                parent.left = None

            return
        
        # Node to delete has both left and right children?        
        if current.right is not None:
            # successor_helper_func
            successor_node, successor_node_parent = self.find_successor(current.right, current)

            # Move right sub-tree up to replace successor
            if successor_node is not current.right:
                successor_node_parent.left = successor_node.right
                successor_node.right = current.right
            
            successor_node.left = current.left

            if root_delete:
                self.root = successor_node

            elif is_current_right_of_parent:
                parent.right = successor_node
            
            else:
                parent.left = successor_node

        # Does the node to delete have left children only?
        else:
            if root_delete:
                self.root = current.left
            elif is_current_right_of_parent:
                parent.right = current.left
            else:
                parent.left = current.left

        self.total_nodes -= 1

        return
    
    def find_successor(self, node: BinaryTreeNode, parent: BinaryTreeNode) -> BinaryTreeNode:
        if node.left is None:
            return node, parent
        
        return self.find_successor(node.left, node)

    def get_min_max_height(self) -> tuple[int, int]:
        """
        Tuple returns the min_height as the left value and max_height as the right value
        """

        min_max_track: list[int | None, int | None] = [None, None]
        def find_tree_height(self, node:BinaryTreeNode, min_max_tuple, height: int = 1):
            if node is None:
                if min_max_tuple[0] is None:
                    min_max_tuple[0] = height - 1
                    min_max_tuple[1] = height - 1
                    return
                min_max_tuple[1] = height-1 if height-1 > min_max_tuple[1] else min_max_tuple[1]
                min_max_tuple[0] = height -1 if height-1 < min_max_tuple[0] else min_max_tuple[0]
                return
            
            new_height = height + 1
            find_tree_height(self, node.left, min_max_tuple, new_height)
            find_tree_height(self, node.right, min_max_tuple, new_height)
            
            return
        find_tree_height(self, self.root, min_max_track)
        return min_max_track


    def dfs_pre(self) -> list[int]:
        items: list[int] = []
        
        def dfs_pre_helper(self, node: BinaryTreeNode, items: list):
            items.append(node.value)

            if node.left is not None:
                dfs_pre_helper(self, node.left, items)

            if node.right is not None:
                dfs_pre_helper(self, node.right, items)

        dfs_pre_helper(self, self.root, items)
        return items
                
    def dfs_post(self) -> list[int]:
        items: list[int] = []
        
        def dfs_pre_helper(self, node: BinaryTreeNode, items: list):
            if node.left is not None:
                dfs_pre_helper(self, node.left, items)
            
            if node.right is not None:
                dfs_pre_helper(self, node.right, items)
            
            items.append(node.value)

        dfs_pre_helper(self, self.root, items)
        return items

    def dfs_in(self) -> list[int]:
        items: list[int] = []
        
        def dfs_pre_helper(self, node: BinaryTreeNode, items: list):
            if node.left is not None:
                dfs_pre_helper(self, node.left, items)

            items.append(node.value)

            if node.right is not None:
                dfs_pre_helper(self, node.right, items)

        dfs_pre_helper(self, self.root, items)
        return items

    def print_tree(self) -> None:
        print_queue: list[BinaryTreeNode | None] = [self.root]
        exponent: int = 0
        total_values_printed_on_line: int = 0 # Total values to be printed in this line
        current_values_printed: int = 0
        total_printed_nodes: int = 0
        while total_printed_nodes < self.total_nodes:
            total_values_printed_on_line = 2 ** exponent
            current_node = print_queue.pop(0)
            if current_node is not None:
                print(current_node.value, end=" ")
                current_values_printed += 1
                print_queue.append(current_node.left)
                print_queue.append(current_node.right)
                total_printed_nodes += 1
            else:
                print("-", end=" ")
                current_values_printed += 1
                print_queue.append(None)
                print_queue.append(None)

            if current_values_printed == total_values_printed_on_line:
                exponent += 1
                current_values_printed = 0
                print()

        print()

        return

def main():
    test_tree: BinarySearchTree = BinarySearchTree()
    # eg_list: list = [1,2,3,4,5,6,7,8]
    # random.shuffle(eg_list)
    eg_list = [8, 4, 7, 3, 6, 5, 1, 2]
    print(eg_list)
    for num in eg_list:
        test_tree.insert_iter(num)

    # test_tree.print_tree()    

    return

if __name__ == "__main__":
    main()