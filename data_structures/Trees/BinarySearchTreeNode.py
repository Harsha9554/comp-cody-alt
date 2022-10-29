class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, data):
        if self.data == data:
            return True

        if data < self.data:
            if self.left:
                return self.left.search(data)
            else:
                return False

        else:
            if self.right:
                return self.right.search(data)
            else:
                return False

    def in_order(self):
        items = []
        if self.left:
            items += self.left.in_order()

        items.append(self.data)

        if self.right:
            items += self.right.in_order()

        return items

    def get_level(self):
        pass

    def print_tree(self):
        pass

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    # def delete(self, data):
    #     if data < self.data:
    #         if self.left:
    #             self.left.delete(data)

    #     if data > self.data:
    #         if self.right:
    #             self.right.delete(data)

    #     else:
    #         if self.left is None and self.right is None:
    #             return None
    #         if self.left is None:
    #             return self.right
    #         if self.right is None:
    #             return self.left

    #         min_val = self.right.find_min()


def build_tree(items):
    root = BinarySearchTreeNode(items[0])

    for i in range(1, len(items)):
        root.add_child(items[i])

    return root
