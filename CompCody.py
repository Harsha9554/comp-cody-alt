import sys

# from data_structures.Queue import Queue
# from data_structures.HashMap import HashMap
from data_structures.Trees.BinarySearchTreeNode import max_depth, build_tree

# IO
sys.stdin = open("io/in.txt", "r")


#   5
#  4 8
# 3 6 10
# 2


def generate_bin(n, i, s, bin_nums):
    if i == n:
        bin_nums.append(s)
    else:
        generate_bin(n, i + 1, s + "0", bin_nums)
        generate_bin(n, i + 1, s + "1", bin_nums)


def subsets(n, items):
    bin_nums = []
    res = []

    generate_bin(n, 0, "", bin_nums)
    for x in bin_nums:
        temp = []
        for i in range(n):
            if x[i] == "1":
                temp.append(items[i])
        res.append(temp)
    return res


def partially_old(n, a):
    flag = 0
    for i in range(1, n - 1):
        if a[i - 1] < a[i] > a[i + 1]:
            flag = 1
            return i + 1
    if not flag:
        return -1


def main():
    a = list(map(int, input().split()))
    bst = build_tree(a)
    print(max_depth(bst))


main()
