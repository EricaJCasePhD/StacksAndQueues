class LinkedList(object):
    def __init__(self):
        self.__head = None  # keep the head private. Not accessible outside this class

    # method to add a new node with the specific data value in the linked list
    # insert the new node at the beginning of the linked list
    def insert(self, data):
        new_node = Node(value=data)
        new_node.next_node = self.__head
        self.__head = new_node
        print("inserting {}".format(data))

    def find_max(self):
        if self.__head == None:
            return "None"
        node = self.__head
        max = node.get_data()
        while node.next_node != None:
            if node.get_data() > max:
                max = node.get_data()
            node = node.next_node
        return (max)

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
        return (min)

    # # method that returns the length of the singly linked list
    def length(self):
        node = self.__head
        counter = 0
        while node != None:
            counter += 1
            node = node.next_node
        return (counter)

    # Defines a node in the singly linked list
    class Node(object):
        def __init__(self, value=None, next_node=None):
            self.__data = None  # protected
            self.__next_node = next_node
