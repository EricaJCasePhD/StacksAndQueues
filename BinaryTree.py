class BinaryTree(object):
    def __init__(self, value=None):
        self._root = TreeNode(value)

    def print_pre_order(self, node = self._root):
        if node == None:
            return
        print node.value
        print_pre_order(node.left)
        print_pre_order(node.right)

    def print_post_order(self):
        if node == None:
            return
        print_post_order(node.left)
        print_post_order(node.right)
        print(node.value)

    def print_in_order(self):
        if node == None:
            return
        print_post_order(node.left)
        print(node.value)
        print_post_order(node.right)

    def insert(self, value):
        if self._root == null:
            self._root = Node(value)

class TreeNode(object):
    def init(self, value=None, left=None, right=None):
        self.__value = value
        self.left = left
        self.right = right

        @property
        def value(self):
            return(value)

def make_tree(self):
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    return BinaryTree(root)


