class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {

        auto comp_dist = [](std::vector<int>& p1, std::vector<int>& p2) {
            auto euc_dist = [](int x, int y) {
                return std::sqrt(std::pow(x, 2) + std::pow(y, 2));
            };
            return euc_dist(p1[0], p1[1]) < euc_dist(p2[0], p2[1]);
        };
        std::priority_queue<std::vector<int>, std::vector<std::vector<int>>, decltype(comp_dist)> 
            max_heap;

        for (auto p : points) {
            max_heap.push(p);
            if (max_heap.size() > k) max_heap.pop();
        }

        std::vector<vector<int>> result;
        while (max_heap.size()) {
            result.push_back(max_heap.top());
            max_heap.pop();
        }
        return result;
    }
};