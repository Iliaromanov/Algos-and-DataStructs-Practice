class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 1) return nums[0];
        if (nums.size() == 2) return std::max(nums[0], nums[1]);

        std::vector<int> nums_copy = nums; // need 1 copy to not overlap between two calls
        return std::max(houseRobber(nums, 0, nums.size()-2), houseRobber(nums_copy, 1, nums.size()-1));
    }

    // runs house robber I on nums[s] to nums[f] inclusive
    int houseRobber(vector<int>& nums, int s, int f)
    {
        // f - s + 1 == 1 is impossible since in rob the min size == 3
        if (f - s + 1 == 2) return std::max(nums[s], nums[f]);

        nums[f - 1] = std::max(nums[f], nums[f-1]);
        for (int i = f-2; i >= s; --i)
        {
            nums[i] = std::max(nums[i] + nums[i+2], nums[i+1]);
        }

        return nums[s];
    }
};