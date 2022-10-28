from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def push_item(self, item):
        self.container.append(item)

    def pop_item(self):
        # print("removing {}.".format(self.peek_item()))
        return self.container.pop()

    def peek_item(self):
        return self.container[-1]

    def __str__(self):
        return "[" + ", ".join(self.container) + "]"
