from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        
        buy = prices[0]
        for price in prices:
            if price < buy:
                buy = price
            else:
                profit = max(profit, price - buy)
                
        return profit