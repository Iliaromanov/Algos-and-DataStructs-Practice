class Node:
    def __init__(self, key: int, val: int, _next = None, _prev = None):
        self.val = val
        self.key = key
        self.next = _next
        self.prev = _prev

class LRUCache:

    def __init__(self, capacity: int):
         self.capacity = capacity
         self.map = dict()
         self.head = Node(0, 0)  # dummy node for head
         self.tail = Node(0, 0)  # dummy node for tail
         self.head.next = self.tail
         self.tail.prev = self.head

    def _remove(self, node: Node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node: Node):
        p = self.tail.prev
        node.prev = p
        node.next = self.tail
        p.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            # add node to front of LList
            self._remove(node)
            self._add(node)
            return node.val

        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            # add node to front of LList
            self._remove(node)
            self._add(node)
            return

        if len(self.map) == self.capacity:
            lru_node = self.head.next
            self._remove(lru_node)
            del self.map[lru_node.key]
        
        new_node = Node(key, value)
        self.map[key] = new_node
        self._add(new_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)