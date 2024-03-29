

"""

let n = len(s), m = len(wordDict), k = max(len(word) for word in wordDict)

"""



"""
O(n * m * k)
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        subprob: dp(i) = can parse s[i:]
        answer:  dp(0)
        recurrence: dp(i) = s[i] in wordDict and dp(j, j+1) 
                            or
                               dp(i, j+1)
        base cases: if j == len(s): dp(i, j) = s[i:j] in wordDict
                    dp(len(s), len(s)) = True
        """
        dp = [False for _ in range(len(s)+1)]

        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1): # O(len(s))
            for word in wordDict:
                if i+len(word) <= len(s) and s[i:i+len(word)] == word: # O(len(word))
                    dp[i] = dp[i+len(word)]
                    if dp[i] is True: break
        return dp[0]




"""
O(n^2)
"""
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