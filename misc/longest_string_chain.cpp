class Solution {
public:
    bool is_predecessor(string_view s1, string_view s2)
    {
        if (s1.length() < s2.length()) swap(s1, s2);
        if (s1.length() - s2.length() != 1) return false;
        bool saw_del_char = false;
        for (int i = 0; i < s1.length(); ++i)
        {
            int j = saw_del_char ? i - 1 : i;

            if (s1[i] != s2[j])
            {
                if (saw_del_char) return false;
                saw_del_char = true;
                continue;
            }
        }
        return true;
    }

    int longestStrChain(vector<string>& words) {
        sort(
            words.begin(), 
            words.end(), 
            [](string_view w1, string_view w2) {return w1.length() < w2.length();}
        );
        vector<int> dp(words.size(), 1);
        for (int i = words.size() - 2; i >=0; --i)
        {
            for (int j = i+1; j < words.size(); ++j)
            {
                if (is_predecessor(words[i], words[j]))
                    dp[i] = max(dp[i], 1+dp[j]);
            }
        }
        int result = 1;
        for (auto val : dp) 
        {
            result = max(result, val);
        }
        return result;
    }
};