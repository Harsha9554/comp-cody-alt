class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data == data:
            return False

        elif data < self.data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = BinarySearchTreeNode(data)
                return True

        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = BinarySearchTreeNode(data)
                return True

    def max_node(self, node):
        cur_node = node
        while cur_node.right is not None:
            cur_node = cur_node.right

        return cur_node

    def min_node(self, node):
        cur_node = node
        while cur_node.left is not None:
            cur_node = cur_node.left

        return cur_node

    def delete(self, data, root):
        if self is None:
            return None

        if data < self.data:
            self.left = self.left.delete(data, root)
        if data > self.data:
            self.right = self.right.delete(data, root)

        else:
            if self.left is None:
                if self == root:
                    temp = self.min_node(self.right)
                    self.data == temp.data
                    self.right = self.right.delete(temp.data, root)

                temp = self.right
                self = None
                return temp
            elif self.right is None:
                if self == root:
                    temp = self.max_node(self.left)
                    self.data = temp.data
                    self.left = self.left.detele(temp.data, root)

                temp = self.left
                self = None
                return temp
            temp = self.min_node(self.right)
            self.data = temp.data
            self.right = self.right.delete(temp.data, root)
        return self

    def search(self, data):
        if data == self.data:
            return True
        elif data < self.data:
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
        if self:
            if self.left:
                self.left.in_order()
            print(str(self.data), end=" ")
            if self.right:
                self.right.in_order()

    def max_depth(self, root):
        if not root:
            return 0
        if root:
            return 1 + max(root.max_depth(root.left), root.max_depth(root.right))


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = BinarySearchTreeNode(data)
            return True

    def delete(self, data):
        if self.root is not None:
            return self.root.delete(data, self.root)

    def search(self, data):
        if self.root:
            return self.root.search(data)
        else:
            return False

    def in_order(self):
        if self.root is not None:
            print()
            print("In-Order: ")
            self.root.in_order()

    def max_depth(self):
        if self.root is not None:
            return self.root.max_depth(self.root)
