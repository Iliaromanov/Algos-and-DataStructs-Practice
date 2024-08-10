class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
        let dp(i, j) be num possible ways to get to amount from coins[i] holding change j
        ans dp(0, 0)
        base dp(i, amount) = 1 
        recur dp(i, j) = j+coins[i] <= amount ? dp(i, j+coins[i]) : 0 + dp(i+1, j)
        """
        dp = [[0 for _ in range(amount+1)] for _ in range(len(coins))]
        
        for i in range(len(coins)-1, -1, -1):
            for j in range(amount, -1, -1):
                if j == amount:
                    dp[i][j] = 1
                    continue
                skip = dp[i+1][j] if i < len(coins)-1 else 0
                take = dp[i][j+coins[i]] if j+coins[i] <= amount else 0
                dp[i][j] = skip + take
        
        return dp[0][0]
