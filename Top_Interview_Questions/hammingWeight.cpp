// Runtime
// 0 ms
// Beats
// 100%
// Memory
// 6.1 MB
// Beats
// 30.80%

class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        while (n != 0) {
          if ((n & 1) == 1) {
            count++;
          }
          n >>= 1;
        }
        return count;
    }
};