class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        /*
        let:       dp[i][j] = lcs of text1 up to i and text2 up to j
        ans:       dp[text1.length()-1][text2.length()-2]
        base case: dp[0][0] = 1 if text1[0] == text2[0] else 0
        recur:     dp[i][j] = t1[i] == t2[j] ? dp[i-1][j-1] :
                                               max(dp[i+1][j], dp[i][j+1])
        */

        vector<vector<int>> dp(text1.length(), vector<int>(text2.length(), 0));

        for (int i = 0; i < text1.length(); ++i) {
            for (int j = 0; j < text2.length(); ++j) {
                if (text1[i] == text2[j]) {
                    dp[i][j] = 1 + (i-1 >= 0 && j-1 >= 0 ? dp[i-1][j-1] : 0);
                } else {
                    dp[i][j] = std::max(
                        i-1 >= 0 ? dp[i-1][j] : 0,
                        j-1 >= 0 ? dp[i][j-1] : 0
                    );
                }
            }
        }

        return dp[text1.length()-1][text2.length()-1];
    }
};