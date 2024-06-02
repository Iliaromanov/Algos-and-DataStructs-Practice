/*
Time Complexity:
- n choices for first pos, n-1 for second, n-2, ...
- n * (n-1) * (n-2) * ... = n!
- there is n! permutations
- at each permutation we need to copy the vec
thus time is O(n * n!)

*/

class Solution {
public:
    vector<vector<int>> result;
    void backtrack(vector<int>& nums, vector<int>& com, int idx){
        if (idx == nums.size())
        {
            result.push_back(com);
            return;
        }
        
        for (int i = 0; i < com.size(); ++i)
        {
            if (com[i] == 11)
            {
                com[i] = nums[idx];
                backtrack(nums, com, idx+1);
                com[i] = 11;
            }
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> com(nums.size(), 11);
        backtrack(nums, com, 0);
        return result;
    }
};