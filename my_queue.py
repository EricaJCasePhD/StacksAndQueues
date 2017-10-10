class Queue(object):
    def init():
        self.__queuearray = []

    def top(self):
        next_value = self.__stackarray.pop()
        self.__stackarray.push(next_value)

    def push(self, value):
        self.__queuearray.append(self, value)

    def pop(self):
        return self.__queuearray.pop(0)

    def top(self):
        next_value = self.stackarray.pop()
        self.stackarray.push(next_value)