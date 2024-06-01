class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>> result;
        vector<int> empty = {};
        backtrack(0, 0, target, candidates, empty, result);
        return result;
    }

    void backtrack(
        int idx, int sum, int target, vector<int>& candidates, vector<int>& cur_comb, vector<vector<int>>& result)
    {
        if (sum == target)
        {
            result.emplace_back(cur_comb);
            return;
        }

        if (idx >= candidates.size() || sum > target)
            return;

        cur_comb.push_back(candidates[idx]);
        backtrack(idx, sum+candidates[idx], target, candidates, cur_comb, result);
        cur_comb.pop_back();
        backtrack(idx+1, sum, target, candidates, cur_comb, result);
    }
};