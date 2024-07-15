class Solution {
public:
    int maxProduct(vector<int>& nums) {
        // dp[i].first = max product including nums[i]
        // dp[i].second = min product including nums[i]
        // answer: max(dp[i].first) for i in range(len(nums))
        // base case: dp[i] = {nums[i], 1}
        // dp[i].first = max(nums[i], nums[i] * dp[i+1].first, nums[i] * dp[i+1].second)
        // dp[i].second = min(nums[i], nums[i] * dp[i+1].second)
        vector<pair<double, double>> dp(nums.size(), make_pair(nums[nums.size()-1], 1));
        
        for (int i = nums.size()-2; i >= 0; --i)
        {
            dp[i].first = max(static_cast<double>(nums[i]), max(nums[i] * dp[i+1].first, nums[i] * dp[i+1].second));
            dp[i].second = min(static_cast<double>(nums[i]), min(nums[i] * dp[i+1].first, nums[i] * dp[i+1].second));
        }
        double result = nums[0];
        for (const auto [max_at_i, _] : dp) result = max(static_cast<double>(result), max_at_i);
        return static_cast<int>(result);
    }
};