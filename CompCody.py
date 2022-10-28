import sys


# from data_structures.Queue import Queue
# from data_structures.HashMap import HashMap
from data_structures.Trees.TreeNode import TreeNode, print_pretty

# IO
sys.stdin = open("io/in.txt", "r")
sys.stdout = open("io/out.txt", "w")


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


def main():
    root = TreeNode("agents")

    sentinels = TreeNode("sentinels")

    chamber = TreeNode("chamber")
    chamber.add_child(TreeNode("male"))
    chamber.add_child(TreeNode("france"))

    sentinels.add_child(chamber)
    sentinels.add_child(TreeNode("sage"))
    sentinels.add_child(TreeNode("cypher"))

    duelists = TreeNode("duelists")
    duelists.add_child(TreeNode("reyna"))
    duelists.add_child(TreeNode("phoenix"))
    duelists.add_child(TreeNode("yoru"))

    initiators = TreeNode("initiators")
    initiators.add_child(TreeNode("fade"))
    initiators.add_child(TreeNode("sova"))
    initiators.add_child(TreeNode("breach"))

    root.add_child(sentinels)
    root.add_child(duelists)
    root.add_child(initiators)

    print_pretty(root)


main()
