class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int max_sum = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            nums[i] = max(nums[i], nums[i-1] + nums[i]);
            max_sum = max(max_sum, nums[i]);
        }
        return max_sum;
    }
};