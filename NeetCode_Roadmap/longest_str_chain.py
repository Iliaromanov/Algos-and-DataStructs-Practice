class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        """
        let dp(i) = longest word chain starting at words i
        ans max(dp(i))
        base dp(len(words)) = 0
        recur dp(i) = 1+max(dp(j) for j>i if pred(words[i], words[j]))
        """
        words.sort(key=lambda x: len(x))
        dp = {}
        for w in words:
            dp[w] = 1+max(dp.get(w[:i] + w[i+1:], 0) for i in range(len(w)))

        return max(dp[w] for w in words)
