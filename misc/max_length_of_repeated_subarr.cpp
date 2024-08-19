#include <vector>
#include <cmath>

using namespace std;

class Solution {
public:
    int findLength(vector<int>& nums1, vector<int>& nums2) {
        /*
        let dp(i, j) = longest repeating subarr starting at nums1[i:], nums2[j:] inclusive
        ans dp(0, 0)
        base dp(nums1.size(), nums2.size()) = 0
        recu dp(i, j) = 1+dp(i+1, j+1) if nums1[i] == nums2[j] else 0
        */
        int dp[1001][1001] = {0};

        int res = 0;
        for (int i = nums1.size()-1; i >= 0; --i) {
            for (int j = nums2.size()-1; j >= 0; --j) {
                dp[i][j] = nums1[i] == nums2[j] ? 1+dp[i+1][j+1] : 0;
                res = max(res, dp[i][j]);
            }
        }
        return res;
    }
};