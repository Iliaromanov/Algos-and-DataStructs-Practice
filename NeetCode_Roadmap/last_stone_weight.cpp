class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        std::priority_queue<int> max_heap(stones.begin(), stones.end());

        while (max_heap.size() != 0) {
            if (max_heap.size() == 1)
                return max_heap.top();
            
            int y = max_heap.top();
            max_heap.pop();
            int x = max_heap.top();
            max_heap.pop();
            if (x == y) continue;
            max_heap.push(y - x);
        }
        return 0;
    }
};
