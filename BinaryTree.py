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

    def search(self, value, node):
        # Base case: returns true if the node value matches value
        # returns false if the node is empty.
        if node is None or node.value == value:
            return (node is not None)

        # go to the left if  search value is greater than current_node_value
        if value < node.value:
            return self.search(value, node.left)

        # go to the left if current node value is less than or equal to
        # value_to_find
        return self.search(value, node.right)


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
    root = TreeNode(value=3)
    root.left = TreeNode(value=2)
    root.right = TreeNode(value=4)
    root.left.left = TreeNode(value=1)
    root.right.left = TreeNode(value=3.5)
    root.right.right = TreeNode(value=5)
    return BinaryTree(root)


tree = make_tree()
tree.search(3.5, tree.root)
# tree.print_pre_order(tree.root)
# tree.print_post_order(tree.root)
tree.print_in_order(tree.root)

print(tree.search(5, tree.root))
print(tree.search(1, tree.root))
print(tree.search(3.5, tree.root))
print(tree.search(1.5, tree.root))
