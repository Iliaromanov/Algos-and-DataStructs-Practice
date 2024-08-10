#include <vector>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        /*
        let dp[i][0] = max profit starting at day i and not holding anything
            dp[i][1] = max profit starting at day i and holding previously bought
        ans dp[i][0]

        rec dp[i][j] = max(
                dp[i+1][j], // skip day
                j == 0 ? 
                    -prices[i] + dp[i+1][1] : // buy
                    prices[i] + dp[i+2][0] // sell
            )
        */
        int dp[5002][2] = {0};

        for (int day = prices.size()-1; day >= 0; --day) {
            for (int holding = 0; holding <= 1; ++holding) {
                dp[day][holding] = std::max(
                    dp[day+1][holding], // skip
                    holding ?
                        prices[day] + dp[day+2][0] : // sell
                        -prices[day] + dp[day+1][1]  // buy
                ); 
            }
        }
        return dp[0][0];
    }
};
