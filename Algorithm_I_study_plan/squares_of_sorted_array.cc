#include <iostream>
#include <vector>

class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> result = nums;
        int left = 0;
        int right = nums.size() - 1;
        for (int i = nums.size() - 1; i >= 0; i--) {
            int l_val = abs(nums[left]);
            int r_val = abs(nums[right]);
            if (l_val > r_val) {
                result[i] = l_val * l_val;
                ++left;
            } else {
                result[i] = r_val * r_val;
                --right;
            }
        }
        return result;
    }
};