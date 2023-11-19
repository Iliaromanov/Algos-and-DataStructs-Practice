class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        sort(nums.begin(), nums.end());
        int s = nums.size();
        int i = 0;
        while (i < s-2) {
            int first = nums.at(i);
            int l = i+1; 
            int r = s-1;
            while (l < r) {
                int second = nums.at(l);
                int third = nums.at(r);
                int sum = first + second + third;
                if (sum == 0) {
                    result.push_back(vector<int>{first, second, third});
                    while (l < r and nums.at(l) == second) ++l;
                    while (l < r and nums.at(r) == third) --r;
                }
                else if (sum > 0) {
                    --r;
                } else {
                    ++l;
                }
            }
            while (i < s and nums.at(i) == first) ++i;
        }
        return result;
    }
};