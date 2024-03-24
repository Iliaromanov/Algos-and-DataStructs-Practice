class MyHashSet:

    def __init__(self):
        self.k = 601
        self.buckets = [Node(-1) for _ in range(self.k)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            key_hash = key % self.k
            node = Node(key, self.buckets[key_hash].next)
            self.buckets[key_hash].next = node

    def remove(self, key: int) -> None:
        key_hash = key % self.k
        cur = self.buckets[key_hash]
        while cur.next:
            if cur.next.val == key:
                cur.next = cur.next.next
                break
            cur = cur.next
        
    def contains(self, key: int) -> bool:
        key_hash = key % self.k
        cur = self.buckets[key_hash]
        while cur.next:
            if cur.next.val == key:
                return True
            cur = cur.next
        return False

class Node:
    def __init__(self, val: int, _next = None) -> None:
        self.val = val
        self.next = _next

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)