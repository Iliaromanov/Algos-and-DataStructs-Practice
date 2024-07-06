class Solution {
public:
    int maxNonDecreasingLength(vector<int>& nums1, vector<int>& nums2) {
        /*
        subproblem: dp[i][0] = longest n-d subarr *starting* at i using
        answer: max(dp[i][j] for i in len(nums1) for j in [0,1])
        base: dp[-1][0] = 1, dp[-1][1] = 1
        recurrence: dp[i][0] = 1 if min(nums1[i+1], nums2[i+1]) < nums1[i] else 1 + max(dp[i+1][0], dp[i+1][1])
                    dp[i][1] = 1 if min(nums1[i+1], nums2[i+1]) < nums1[i] else 1 + max(dp[i+1][0], dp[i+1][1])
        */
        vector<pair<int, int>> dp(nums1.size(), make_pair(1, 1));
        for (int i = nums1.size()-2; i >= 0; --i)
        {
            dp[i].first = 1 + max(
                nums1[i] > nums1[i+1] ? 0 : dp[i+1].first,
                nums1[i] > nums2[i+1] ? 0 : dp[i+1].second 
            );
            dp[i].second = 1 + max(
                nums2[i] > nums1[i+1] ? 0 : dp[i+1].first,
                nums2[i] > nums2[i+1] ? 0 : dp[i+1].second 
            );
        }

        int result = 0;
        for (const auto& [nums1_start_subarr, nums2_start_subarr] : dp)
            result = max(result, max(nums1_start_subarr, nums2_start_subarr));

        return result;
    }
};