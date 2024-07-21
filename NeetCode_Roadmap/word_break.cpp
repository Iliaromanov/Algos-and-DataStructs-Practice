class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        /*
        dp[i] = possible to segment s from i to len s inclusive
        ans: dp[0]
        base: dp[len(s)] = True
        recurr: dp[i] = anyof(s.substr(i, w.length) == w and dp[i+w.length])
        */
        vector<bool> dp(s.length()+1, false);
        dp[s.length()] = true;

        for (int i = s.length() - 1; i >=0; --i)
        {
            for (const auto& w : wordDict)
            {
                if (s.substr(i, w.length()) == w && dp[i+w.length()])
                {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[0];
    }
};