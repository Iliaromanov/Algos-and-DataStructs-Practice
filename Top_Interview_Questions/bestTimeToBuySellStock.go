func maxProfit(prices []int) int {
    cur_low := prices[0];
    max_profit := 0;
    for _, price := range prices {
        if price < cur_low {
            cur_low = price;
            continue;
        }
        if price - cur_low > max_profit {
            max_profit = price - cur_low;
        }
    }
    return max_profit;
}