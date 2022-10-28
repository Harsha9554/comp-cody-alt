import sys
from data_structures.Stack import Stack

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
    t = int(input())
    for _ in range(t):
        n = int(input())
        stack = Stack()
        for _ in range(n):
            stack.push_item(input())
        print(stack)
        stack.pop_item()
        print(stack)
        stack.push_item("harbor")
        print(stack)
        print(stack.size())


main()
