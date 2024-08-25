#include <vector>
#include <queue>

using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        std::priority_queue<int, vector<int>, std::greater<int>> min_heap;

        for (const auto n : nums) {
            min_heap.push(n);
            if (min_heap.size() > k) min_heap.pop(); 
        }

        return min_heap.top();
    }
};