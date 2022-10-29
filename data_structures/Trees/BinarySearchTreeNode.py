from queue import Queue


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

    # [x]: Implement get level of a node from the root of BST.
    def get_level(self, data, level=1):
        if self.data == data:
            return level

        if data < self.data:
            return self.left.get_level(data, level + 1)
        else:
            return self.right.get_level(data, level + 1)

    # [ ]: Implement pretty print for a BST.
    def print_tree(self):
        pass

    # [ ]: Implement max depth for a BST.
    def max_depth(self):
        pass

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    # [ ]: Implement Node deletion in BST
    def delete(self, data):
        pass


def build_tree(items):
    root = BinarySearchTreeNode(items[0])

    for i in range(1, len(items)):
        root.add_child(items[i])

    return root
