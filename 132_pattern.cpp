class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        // stack[i] = [val, prev_min]
        int glob_min = nums[0];
        vector<pair<int, int>> stack;

        for (auto cur : nums) 
        {
            glob_min = min(cur, glob_min);
            while (stack.size() && stack.back().first <= cur) 
                stack.pop_back();

            if (stack.size() > 0)
            {
                auto [r, l] = stack.back();
                if (l < cur && cur < r) return true;
            }

            if (stack.size() == 0 || stack.back().first != cur)
                stack.emplace_back(cur, glob_min);
        }
        return false;
    }
};