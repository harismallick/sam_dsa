
class BinaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value: int = value
        self.left: BinaryTreeNode | None = left
        self.right: BinaryTreeNode | None = right


    def __eq__(self, value: int):

        if isinstance(value, int):
           return value == self.value 
        
        if isinstance(value, BinaryTreeNode):
            return value.value == self.value

        raise Exception("The passed in value must be of type BinaryTreeNode or an integer.")