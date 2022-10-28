from collections import deque


class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue_item(self, data):
        self.container.appendleft(data)

    def dequeue_item(self):
        return self.container.pop()

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

    def __str__(self):
        return "[" + ", ".join(self.container) + "]"
