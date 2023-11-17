class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int cur_prod = 1;
        int s = nums.size();
        vector<int> prefix{nums};
        for (int i = 0; i < s; ++i) {
            prefix[i] = cur_prod;
            cur_prod *= nums[i];
        }
        cur_prod = 1;
        for (int i = s - 1; i >= 0; --i) {
            prefix[i] *= cur_prod;
            cur_prod *= nums[i];
        }
        return prefix;
    }
};
