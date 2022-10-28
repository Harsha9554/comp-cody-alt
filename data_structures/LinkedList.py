class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if not self.head:
            return "empty."
        else:
            itr = self.head
            temp = "["
            while itr:
                temp += str(itr.data) + " -> "
                itr = itr.next
            temp += "None]"
            return temp

    def insert_first(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_end(self, data):

        node = Node(data, None)
        if self.is_empty():
            self.head = node
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = node

    def insert_at(self, index, data):
        if index < 0 or index >= self.size():
            raise Exception("invalid_index.")

        if index == 0:
            self.insert_first(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def delete_at(self, index):
        if index < 0 or index >= self.size():
            raise Exception("invalid_index.")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def is_empty(self):
        return self.head == None

    def size(self):
        size = 0
        itr = self.head
        while itr:
            size += 1
            itr = itr.next
        return size
