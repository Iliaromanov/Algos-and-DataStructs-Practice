class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];

        int skip_next = 0;
        int next = nums.back();
        for (int i = nums.size() - 2; i >= 0; --i)
        {
            int tmp = next;
            next = max(nums[i] + skip_next, next);
            skip_next = tmp;
        }
        return max(next, skip_next);
    }
};