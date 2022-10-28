class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def push_item(self, item):
        self.items.append(item)

    def pop_item(self):
        print("removing {}.".format(self.peek_item()))
        return self.items.pop()

    def peek_item(self):
        return self.items[-1]

    def __str__(self):
        return "[" + ", ".join(self.items) + "]"
