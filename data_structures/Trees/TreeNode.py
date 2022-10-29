class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def print_pretty(self, marker_str="+- ", level_markers=[]):
        emptry_str = " " * len(marker_str)

        connection_str = "|" + emptry_str[:-1]

        level = len(level_markers)

        mapper = lambda draw: connection_str if draw else emptry_str
        markers = "".join(map(mapper, level_markers[:-1]))
        markers += marker_str if level > 0 else ""
        print(f"{markers}{self.data}")

        for i, child in enumerate(self.children):
            is_last = i == len(self.children) - 1
            child.print_pretty(marker_str, [*level_markers, not is_last])
