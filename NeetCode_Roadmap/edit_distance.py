class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        let dp(i, j) = min edit dist between word1[i:] and word2[j:]
        ans dp(0,0)
        base dp(len(word1), len(word2)) = 0
        recur dp(i, j) = dp(i+1,j+1) if word1[i] == word2[j] else 1+min(
            dp(i, j+1), # insert
            dp(i+1, j+1), # replace
            dp(i+1, j) # delete
        )
        """
        dp = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        for i in range(len(word1)):
            dp[i][len(word2)] = len(word1) - i

        for j in range(len(word2)):
            dp[len(word1)][j] = len(word2) - j
        
        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                    continue
                dp[i][j] = 1 + min(
                    # insert
                    dp[i][j+1],
                    # replace
                    dp[i+1][j+1] if i+1 < len(word1) or j+1 == len(word2) else float('inf'),
                    # delete
                    dp[i+1][j] if i+1 < len(word1) else float('inf'),
                )

        return dp[0][0]
