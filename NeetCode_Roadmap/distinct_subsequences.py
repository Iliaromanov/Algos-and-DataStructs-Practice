class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        let dp(i, j) be number of subseqs of s[i:] which equal t[j:]
        ans dp(0, 0)
        base dp(i, len(t))=1, dp(len(s), j<len(t))=0
        recur dp(i, j) = dp(i+1,j+1) + dp(i+1, j) if s[i] == s[j] else dp(i+1, j)
        """
        dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]

        for i in range(len(s), -1, -1):
            for j in range(len(t), -1, -1):
                if j == len(t):
                    dp[i][j] = 1
                    continue
                elif i == len(s):
                    dp[i][j] = 0
                    continue

                dp[i][j] = dp[i+1][j]
                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1]
        
        return dp[0][0]
