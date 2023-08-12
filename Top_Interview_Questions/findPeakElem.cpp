class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        if (nums.size() <= 1 or nums[0] > nums[1]) return 0;
        if (nums[nums.size() - 1] > nums[nums.size() - 2]) return nums.size() - 1;
        int l = 1;
        int r = nums.size() - 2;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]) return mid;
            
            if (nums[mid + 1] > nums[mid]) l = mid + 1;
            else r = mid - 1;
        }
        return -1;
    }
};