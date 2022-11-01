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
