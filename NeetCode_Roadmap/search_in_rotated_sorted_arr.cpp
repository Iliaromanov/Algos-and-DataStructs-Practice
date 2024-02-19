class Solution {
public:
    int search(vector<int>& nums, int target) {
        int len = nums.size();

        // find k
        int l = 0, r = len - 1;
        while (l < r)
        {
            int k = l + (r - l) / 2;

            if (nums[l] <= nums[k] && nums[k] <= nums[r])
            {
                break; // k = l
            }
            else if (nums[r] < nums[l] && nums[l] <= nums[k])
                l = k + 1;
            else if (nums[k] < nums[r] && nums[r] < nums[l])
                r = k;
        }

        int k = l;
        
        l = 0;
        r = len - 1;
        // do binary search
        while (l <= r)
        {
            int m = l + (r - l) / 2;

            if (nums[(m+k) % len] == target)
                return (m+k) % len;
            else if (nums[(m+k) % len] < target)
                l = m + 1;
            else // nums[(m+k) % len] > target
                r = m - 1;
        }

        return -1;
    }
};