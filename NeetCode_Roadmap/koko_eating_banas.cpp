class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int left = 1;
        int right = *std::max_element(piles.begin(), piles.end());

        while (left < right)
        {
            int k = left + (right - left) / 2;

            int cur_h = 0;
            for (int i = 0; i < piles.size(); ++i)
                cur_h += piles[i] / k + (piles[i] % k != 0);

            if (cur_h <= h)
                right = k;
            else
                left = k + 1;
        }
        
        return right;
    }
};