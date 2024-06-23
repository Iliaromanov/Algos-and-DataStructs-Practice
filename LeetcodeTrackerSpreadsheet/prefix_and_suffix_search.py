class Trie:
    def __init__(self):
        self.children = {}
        self.idx = -1 # only used after $
    
    def insert(self, word: str, dict_idx: int):
        def insert_with_suffix(prefix: str, word: str):
            cur = self
            to_insert = f"{prefix}${word}"
            past_dollar = False
            for c in to_insert:
                if c not in cur.children:
                    cur.children[c] = Trie()
                cur = cur.children[c]
                if c == '$':
                    past_dollar = True
                    continue
                if past_dollar:
                    cur.idx = dict_idx

        for i in range(len(word)):
            insert_with_suffix(word[i:], word)

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for i, word in enumerate(words):
            self.trie.insert(word, i)

    def f(self, pref: str, suff: str) -> int:
        to_search = f"{suff}${pref}"
        cur = self.trie
        for char in to_search:
            if char not in cur.children:
                return -1
            cur = cur.children[char]
        return cur.idx
