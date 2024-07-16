class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        /*
        subproblem: dp[m] = min number of coins needed to get to amount m
        answer: dp[amount]
        base case: dp[0] = 0
        recurrence: dp[m] = min(1 + dp[m-coin] for coin in coins)
        */
        vector<int> dp(amount+1, -1);
        // base case
        dp[0] = 0;

        // recurrence
        for (int m = 1; m <= amount; ++m)
        {
            for (int i = 0; i < coins.size(); ++i)
            {
                int next_amount = m - coins[i];
                if (next_amount >= 0 && dp[next_amount] != -1)
                    dp[m] = min(dp[m] == -1 ? INT_MAX : dp[m], 1 + dp[next_amount]);
            }
        }
        return dp[amount];
    }
};