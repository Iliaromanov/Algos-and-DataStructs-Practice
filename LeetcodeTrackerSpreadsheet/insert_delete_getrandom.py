class RandomizedSet:

    def __init__(self):
        self.map = dict()
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        idx = self.map[val]
        del self.map[val]
        if idx != len(self.values) - 1:
            self.values[idx], self.values[-1] = self.values[-1], self.values[idx]
            self.map[self.values[idx]] = idx
        self.values.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()