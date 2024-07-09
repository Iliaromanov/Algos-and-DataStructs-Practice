class Solution {
public:
    int numDecodings(string s) {
        /*
        subproblem: let dp[i] be num decodings starting at i
        answer: dp[0]
        base case: dp[s.length()-1] = 1 if not 0 else 0, dp[s.length()] = 1
        */
        if (s[0] == '0') return 0;
        vector<int> dp(s.length()+1, 1);
        if (s[s.length()-1] == '0') dp[s.length()-1] = 0;
        for (int i = s.length()-2; i >= 0; --i)
        {
            if (s[i] == '0')
            {
                dp[i] = 0;
                continue;
            }
            dp[i] = dp[i+1] + (stoi(s[i]+string()+s[i+1]) < 27 ? dp[i+2] : 0);
        }
        return dp[0];
    }
};
