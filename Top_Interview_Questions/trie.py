class Trie:

    def __init__(self):
        self.arr = [None for _ in range(26)]
        self.is_end = False
        

    def insert(self, word: str) -> None:
        cur = self
        for char in word:
            i = ord(char) - ord('a')
            if cur.arr[i] is None:
                cur.arr[i] = Trie()
            cur = cur.arr[i]
        cur.is_end = True
        

    def search(self, word: str) -> bool:
        cur = self
        for char in word:
            i = ord(char) - ord('a')
            if cur.arr[i] is None:
                return False
            cur = cur.arr[i]
        
        return cur.is_end

    def startsWith(self, prefix: str) -> bool:
        cur = self
        for char in prefix:
            i = ord(char) - ord('a')
            if cur.arr[i] is None:
                return False
            cur = cur.arr[i]
        return True