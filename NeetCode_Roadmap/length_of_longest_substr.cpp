class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxlen = 0;
        int start = 0;
        map<char, int> seen;
        for (int i = 0; i < s.length(); ++i)
        {
            if (seen.find(s[i]) != seen.end() and seen[s[i]] >= start)
            {
                start = seen[s[i]] + 1;
            }
            maxlen = max(maxlen, i - start + 1);
            seen[s[i]] = i;
        }
        return maxlen;
    }
};