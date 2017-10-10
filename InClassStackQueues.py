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

class ArrayStack(object):
    def __init__(self):
        self.__stackarray = []

    @property
    def top(self):
        next_value = self.__stackarray.pop()
        self.push(next_value)
        return(next_value)

    def push(self, value):
        self.__stackarray.append(value)

    def pop(self):
        return self.__stackarray.pop()

    @property
    def size(self):
        return len(self.__stackarray)

    @property
    def is_empty(self):
        return self.size == 0

    @property
    def min(self):
        return min(self.__stackarray)

    @property
    def max(self):
        return min(self.__stackarray)

    def print(self):
        for item in self.__stackarray:
            print(item)


class LinkedListStack(object):
    def __init__(self):
        self.__stack_list = None

    def push(self, value):
        self.__stack_list.insert(value)

    def pop(self):
        pop_value = self.__stack_list.__head.value()
        stack_list.__head = stack.__next_node
        return(pop_value)

    @property
    def top(self):
        next_value = self.__stacklist.pop()
        self.__stackarray.push(next_value)
        return(next_value)

    @property
    def size(self):
        return (len(self.__stacklist))

    @property
    def is_empty(self):
        return(self.__stackarray == 0)

    @property
    def min(self):
        return(min(self.__stackarray))

    @property
    def max(self):
        return(min(self.__stackarray))



# Defines a node in the singly linked list
class Node(object):
    def __init__(self, value=None, next_node=None):
        self.__data = None  # protected
        self.__next_node = next_node

class TreeNode(object):
    def init(self, value=None, left=None, right=None):
        self.__value = value
        self.left = left
        self.right = right

        @property
        def value(self):
            return(value)

    def node(self):


class LinkedList(object):
    def __init__(self):
        self.__head = None # keep the head private. Not accessible outside this class

    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    def insert(self, data):
        new_node = Node(value = data)
        new_node.next_node = self.__head
        self.__head = new_node
        print ("inserting {}".format(data))

    def find_max(self):
        if self.__head == None:
            return "None"
        node = self.__head
        max = node.get_data()
        while node.next_node != None:
            if node.get_data() > max:
                max = node.get_data()
            node = node.next_node
        return(max)

    # # method to return the min value in the linked list
    # # returns the data value and not the node
    def find_min(self):
        if self.__head == None:
            return "None"

        node = self.__head
        min = node.get_data()
        while node.next_node != None:
            if node.get_data() < min:
                min = node.get_data()
            node = node.next_node
        return(min)

    # # method that returns the length of the singly linked list
    def length(self):
        node = self.__head
        counter = 0
        while node != None:
            counter += 1
            node = node.next_node
        return(counter)

class Queue(object):
    def init():
        self.__queuearray = []

    def top(self):
        next_value = self.__stackarray.pop()
        self.__stackarray.push(next_value)

    def push(self,value):
        self.__queuearray.append(self, value)

    def pop(self):
        return self.__queuearray.pop(0)

    def top(self):
        next_value = self.stackarray.pop()
        self.stackarray.push(next_value)

def test_stack(stacklist):
    if not(stacklist.is_empty): print ("empty doesn't work")
    if stacklist.size != 0: print ("size doesn't work")

    stacklist.push(4)
    if stacklist.size != 1: print("push doesn't work")
    if stacklist.top != 4: print("top doesn't work")

    if stacklist.pop() != 4: print ("pop doesn't work")
    if not(stacklist.is_empty): print ("pop doesn't work")

def make_tree(self):

test_stack(ArrayStack())
test_stack(LinkedListStack())
