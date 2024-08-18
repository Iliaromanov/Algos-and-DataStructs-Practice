#include <vector>
#include <cmath>
#include <numeric>

using namespace std;

class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        /*
        amount of times to get to +ve target == amount of times to get to -1 * +ve target
        so assume its +ve

        sum(P) - sum(N) = target
        sum(P) = target + sum(N)
        sum(P) = target + sum(nums) - sum(P)
        2sum(P) = target + sum(nums)
        sum(P) = (target + sum(nums)) / 2

        How to count subsets that sum to sum_p:
        let dp[i][k] = num ways to get to sum k using subset of nums[i:]
        ans dp(0, sum_p)
        base: dp(i, j) = 0,  dp(i, 0) = 1
        recurrence: dp(i, k) = dp(i+1, k) + dp(i+1, k-nums[i])
        */
        int sum_p = std::abs(target) + std::accumulate(nums.begin(), nums.end(), 0);
        if (sum_p % 2) return 0;
        sum_p = sum_p / 2;

        int dp[21][1001] = {0};
        for (int i = 0; i <= nums.size(); ++i) dp[i][0] = 1;

        for (int i = nums.size()-1; i >= 0; --i) {
            for (int j = 0; j <= sum_p; ++j) {
                dp[i][j] = dp[i+1][j] + (j-nums[i] >= 0 ? dp[i+1][j-nums[i]] : 0);
            }
        }
        return dp[0][sum_p];
    }
};
