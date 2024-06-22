class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> seen;
        for (int i = 0; i < nums.size(); i++) {
            if (seen.find(target - nums[i]) != seen.end()) {
                vector<int> result = {i, seen.find(target - nums[i])->second};
                return result;
            } else {
                seen[nums[i]] = i;
            }
        }
        
        return vector<int>{1};
    }
};