class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append((value, timestamp))
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map or self.map[key][0][1] > timestamp:
            return ""
        if timestamp >= self.map[key][-1][1]:
            return self.map[key][-1][0]
        
        records = self.map[key]
        l, r = 0, len(records) - 1
        while l <= r:
            m = l + (r - l) // 2

            val, time = records[m]
            if time == timestamp:
                return val
            elif time > timestamp:
                r = m - 1
            else:
                l = m + 1
        
        return records[l-1][0]

        
# set foo (bar, 1), (car, 3), (cat, 5), (war, 7)
# get foo 2 -> bar
# get foo 4 -> car

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

