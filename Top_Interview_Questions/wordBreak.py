class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        subprob: dp(i, j) = can parse s given that the last break was at i
                and we are currently at j
        answer:  dp(0, 0)
        recurrence: dp(i, j) = s[i:j] in wordDict and dp(j, j+1) 
                            or
                               dp(i, j+1)
        base cases: if j == len(s): dp(i, j) = s[i:j] in wordDict
                    dp(len(s), len(s)) = True
        """
        wordDict = set(wordDict)  # O(n)
        dp = [[False for _ in range(len(s)+1)] for _ in range(len(s)+1)]

        # Base cases
        dp[len(s)][len(s)] = True
        for i in range(len(s)): # O(n) since 'in' for hashset is O(1)
            if s[i:] in wordDict:
                dp[i][len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for j in range(len(s)-1, i-1, -1):
                dp[i][j] = (s[i:j] in wordDict and dp[j][j+1]) or dp[i][j+1]

        return dp[0][0]