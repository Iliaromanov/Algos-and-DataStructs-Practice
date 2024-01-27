class Solution {
public:
    void get_char_freqs(string s, int start, int end, vector<int>& freqs)
    {
        for (int i = start; i <= end; ++i)
            ++freqs.at(s[i] - 'a');
    }

    bool checkInclusion(string s1, string s2) {
        if (s1.size() > s2.size()) return false;
        vector<int> s1_freqs(26, 0);

        get_char_freqs(s1, 0, s1.size()-1, s1_freqs);
        
        int s = 0;
        int e = s1.size() - 1;
        vector<int> s2_freqs(26, 0);

        get_char_freqs(s2, s, e, s2_freqs);
        while (1)
        {
            if (s1_freqs == s2_freqs) return true;
            s2_freqs[s2[s] - 'a']--;
            ++s;
            ++e;
            if (e > s2.size() - 1) break;
            s2_freqs[s2[e] - 'a']++;
        }
        return false;
    }
};