import sys

# from data_structures.Queue import Queue
# from data_structures.HashMap import HashMap
from data_structures.Trees.BinarySearchTree import BinarySearchTree


# IO
sys.stdin = open("io/in.txt", "r")
sys.stdout = open("io/out.txt", "w")


def main():
    tree = BinarySearchTree()
    tree.insert(10)
    tree.insert(12)
    tree.insert(5)
    tree.insert(4)
    tree.insert(20)
    tree.insert(8)
    tree.insert(7)
    tree.insert(15)
    tree.insert(13)
    print(tree.search(1))
    print(tree.search(12))

    """ Following tree is getting created:
                    10
                 /      \
               5         12
              / \           \
            4     8          20
                 /          /
                7         15
                         /
                       13
    """

    # tree.in_order()
    # print("\n\nAfter deleting 20")
    # tree.delete(20)
    tree.in_order()
    # print("\n\nAfter deleting 10")
    # tree.delete(10)
    tree.in_order()
    print()
    print()
    print("max-depth: ", tree.max_depth())


main()
