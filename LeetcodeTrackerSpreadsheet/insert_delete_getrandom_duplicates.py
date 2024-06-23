class RandomizedCollection:
    def __init__(self):
        self.map = {}
        self.vals = [] # List[val, i_in_map]
        
    def insert(self, val: int) -> bool:
        result = False
        if val not in self.map or len(self.map[val]) == 0:
            result = True
            self.map[val] = []
        self.vals.append([val, len(self.map[val])])
        self.map[val].append(len(self.vals) - 1)
        return result

    def remove(self, val: int) -> bool:
        if val not in self.map or len(self.map[val]) == 0:
            return False
        rm_val_idx = self.map[val].pop()
        if rm_val_idx != len(self.vals) - 1:
            self.vals[rm_val_idx], self.vals[-1] = self.vals[-1], self.vals[rm_val_idx]
            swapped_val, swapped_val_map_idx = self.vals[rm_val_idx]
            self.map[swapped_val][swapped_val_map_idx] = rm_val_idx
        self.vals.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)[0]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()