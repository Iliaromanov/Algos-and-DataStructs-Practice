class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> result;
        int i = 0;
        while (i < nums.size() - 2) {
            twoSum(nums, result, -1 * nums[i], i + 1);
            i++;
            // ensure i isn't duplicated
            while (i < nums.size() && nums[i] == nums[i-1]) i++;
        }
        return result;
    }

    void twoSum(vector<int>& nums, vector<vector<int>>& result, int target, int start) {
        int l = start, r = nums.size() - 1;
        while (l < r) {
            int sum = nums[l] + nums[r];
            if (sum == target) {
                result.push_back(vector<int>{-1*target, nums[l], nums[r]});
                l++;
                r--;
                // ensure l isn't duplicate
                while (l < nums.size() && nums[l] == nums[l-1]) l++;
                // ensure r isn't duplicate
                while (r > 0 && nums[r] == nums[r+1]) r--;
            } else if (sum > target) {
                r--;
            } else {
                l++;
            }
        }
    }
};