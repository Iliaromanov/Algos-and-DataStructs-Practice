class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0;
        int buy = prices[0];
        for (int price : prices)
        {
            if (price < buy) buy = price;
            else max_profit = max(max_profit, price - buy);
        }
        return max_profit;
    }
};
