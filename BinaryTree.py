class BinaryTree(object):
    def __init__(self, root=None):
        self.root = root

    def print_pre_order(self, node):
        if node == None:
            return
        print(node.value)
        self.print_pre_order(node.left)
        self.print_pre_order(node.right)

    def print_post_order(self, node):
        if node == None:
            return
        self.print_post_order(node.left)
        self.print_post_order(node.right)
        print(node.value)

    def print_in_order(self, node):
        if node is None:
            return
        self.print_in_order(node.left)
        print(node.value)
        self.print_in_order(node.right)

    # def insert(self, value):
    #     if self._root == null:
    #         self._root = Node(value)


class TreeNode(object):
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    #
    # @property
    # def value(self):
    #     return (self.__value)

def make_tree():
    root = TreeNode(value=1)
    root.left = TreeNode(value=2)
    root.right = TreeNode(value=3)
    root.left.left = TreeNode(value=4)
    root.left.right = TreeNode(value=5)
    return BinaryTree(root)


tree = make_tree()
# tree.print_pre_order(tree.root)
# tree.print_post_order(tree.root)
tree.print_in_order(tree.root)
