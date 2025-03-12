import random

class BinaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value: int = value
        self.left: BinaryTreeNode | None = left
        self.right: BinaryTreeNode | None = right

class BinarySearchTree:
    def __init__(self):
        self.root: BinaryTreeNode | None = None
        self.total_nodes: int = 0

    def insert_iter(self, value: int) -> None:   
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

    test_tree.print_tree()    

    return

if __name__ == "__main__":
    main()