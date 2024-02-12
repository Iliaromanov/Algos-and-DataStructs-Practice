class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        std::deque<int> window_indices;
        std::vector<int> result;
        int end = 0;

        // do first k window
        while (end < k)
        {
            while (!window_indices.empty() && nums[end] >= nums[window_indices.back()])
                window_indices.pop_back();
            window_indices.push_back(end);
            ++end;
        }

        result.push_back(nums[window_indices.front()]);

        // slide the window
        int len = nums.size();
        while (end < len)
        {
            // check if max went out of window
            if (window_indices.front() <= end - k)
                window_indices.pop_front();

            while (!window_indices.empty() && nums[end] >= nums[window_indices.back()])
                window_indices.pop_back();
            
            window_indices.push_back(end);
            result.push_back(nums[window_indices.front()]);
            ++end;
        }

        return result;
    }   
};

