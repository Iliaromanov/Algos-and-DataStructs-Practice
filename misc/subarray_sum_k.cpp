class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int result = 0;
        int cur_sum = 0;
        std::unordered_map<int, int> count_prefix_sum;
        for (const int num : nums)
        {
            cur_sum += num;
            
            if (cur_sum - k == 0) result++;

            auto it = count_prefix_sum.find(cur_sum - k);
            if (it != count_prefix_sum.end())
                result += it->second;
            
            it = count_prefix_sum.find(cur_sum);
            if (it != count_prefix_sum.end())
                ++it->second;
            else
                count_prefix_sum[cur_sum] = 1;
        }
        return result;
    }
};