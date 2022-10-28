class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.items = [None for i in range(self.size)]

    def hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.size

    def __setitem__(self, key, val):
        h = self.hash(key)
        self.items[h] = val

    def __getitem__(self, key):
        h = self.hash(key)
        return self.items[h]
