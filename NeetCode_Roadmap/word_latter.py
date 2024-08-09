class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        vis = set()
        q = deque([[beginWord, 1]])
        while len(q):
            top, l = q.popleft()
            if top == endWord:
                return l
            vis.add(top)
            for i in range(len(top)):
                for char in range(ord('a'), ord('z') + 1):
                    adj_s = top[:i] + chr(char) + top[i+1:]
                    if adj_s in wordSet and adj_s not in vis:
                        q.append([adj_s, l+1])

        return 0