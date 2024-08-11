#include <string>
using namespace std;

class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        /*
        let dp(i,j) be is it possible to interleave s1 upto i, s2 upto j to get s3 up to i+j inclusive;
        ans dp(0, 0)
        base dp(s1.length(), s2.length()) = true;
             dp(i > s1.length(), j) = false
             dp(i, j > s2.length()) = false
        recurrence dp(i, j) = (s1[i] == s3[i+j] && dp(i+1, j)) || (s2[j] == s3 && dp(i, j+1))
        */
        if (s1.length() + s2.length() != s3.length()) return false;

        bool dp[101][101] = {false};
        for (int i = s1.length(); i >= 0; --i) {
            for (int j = s2.length(); j >= 0; --j) {
                if (i == s1.length() && j == s2.length()) {
                    dp[i][j] = true;
                    continue;
                }
                bool use_s1 = i < s1.length() ? s1[i] == s3[i+j] && dp[i+1][j] : false;
                bool use_s2 = j < s2.length() ? s2[j] == s3[i+j] && dp[i][j+1] : false;
                dp[i][j] = use_s1 || use_s2;
            }
        }
        return dp[0][0];
    }
};
