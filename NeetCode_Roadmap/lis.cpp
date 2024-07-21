class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        /*
        dp[i] = LIS starting at i
        ans: max(dp[i] for i in range(len(nums)))
        base: dp = {1...}
        recur: dp[i] = max(1, 1+dp[j] for j>i and nums[j]>nums[i])
        */
        vector<int> dp(nums.size(), 1);
        int overall_max = 1;
        for (int i = nums.size() - 2; i >= 0; --i)
        {
            for (int j = i+1; j < nums.size(); ++j)
            {
                if (nums[j] > nums[i])
                    dp[i] = max(dp[i], 1 + dp[j]);
            }
            overall_max = max(overall_max, dp[i]);
        }
        return overall_max;
    }
};