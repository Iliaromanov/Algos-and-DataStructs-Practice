class Solution:
    """
    Subproblem: let dp[i][j] = the number of unique paths from i, j to m-1. n-1
    Answer: dp[0][0]
    Recurrence: dp[i][j] = dp[i+1][j] + dp[i][j+1]
    Base Case: dp[m-1][n-1] = 0
    """
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for i in range(m)]
        dp[m-1][n-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                elif i == m - 1:
                    dp[i][j] = dp[i][j+1]
                elif j == n - 1:
                    dp[i][j] = dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]