class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)


def print_pretty(root, marker_str="+- ", level_markers=[]):
    emptry_str = " " * len(marker_str)

    connection_str = "|" + emptry_str[:-1]

    level = len(level_markers)

    mapper = lambda draw: connection_str if draw else emptry_str
    markers = "".join(map(mapper, level_markers[:-1]))
    markers += marker_str if level > 0 else ""
    print(f"{markers}{root.data}")

    for i, child in enumerate(root.children):
        is_last = i == len(root.children) - 1
        print_pretty(child, marker_str, [*level_markers, not is_last])
