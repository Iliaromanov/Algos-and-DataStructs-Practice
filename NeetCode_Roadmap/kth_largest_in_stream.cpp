#include <vector>
#include <queue>



class KthLargest {
public:
    KthLargest(int k, std::vector<int>& nums) : max_size{k} {
        for (const auto n : nums) 
            min_heap.push(n);
        
        while (min_heap.size() > k)
            min_heap.pop();
    }
    
    int add(int val) {
        min_heap.push(val);
        if (min_heap.size() > max_size)
            min_heap.pop();
        
        return min_heap.top();
    }

private:
    std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap;
    int max_size;
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
