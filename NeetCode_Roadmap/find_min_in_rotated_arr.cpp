class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;
        while (l < r)
        {
            int m = l + (r - l) / 2;

            if (nums[l] <= nums[m] && nums[m] <= nums[r])
                return nums[l];
            else if (nums[m] < nums[r] && nums[r] < nums[l])
                r = m;
            else if (nums[r] < nums[l] && nums[l] <= nums[m])
                l = m + 1;
        }
        return nums[l];
    }
};