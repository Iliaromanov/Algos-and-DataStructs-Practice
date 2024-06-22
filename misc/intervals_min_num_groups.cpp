class Solution {
public:
    int minGroups(vector<vector<int>>& intervals)
    {
        std::sort(intervals.begin(), intervals.end());
        std::priority_queue<int> heap;
        for (const auto& i : intervals)
        {
            if (heap.size() && -1 * heap.top() < i[0])
                heap.pop();
            heap.push(-1 * i[1]);
        }
        return heap.size();
    }
};