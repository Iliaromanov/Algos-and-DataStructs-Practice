class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        subprob: dp[i] = min cost to reach the top starting at i
        answer: min(dp[0], dp[1])
        recurrence: dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        base cases: dp[n] = 0, dp[n-1] = cost[n-1]
        """
        n = len(cost)
        if len(cost) <= 2:
            return min(cost)
        dp = [0 for _ in range(n+1)]
        dp[n] = 0
        dp[n-1] = cost[n-1]
        for i in range(n-2, -1, -1):
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])

        return min(dp[0], dp[1])