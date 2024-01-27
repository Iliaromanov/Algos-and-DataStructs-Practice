class Solution {
public:
    int characterReplacement(string s, int k) {
        int freqs[26] = {};
        int start = 0;
        int result = 0;
        for (int end = 0; end < s.size(); ++end)
        {
            ++freqs[s[end] - 'A'];
            int window_size = end - start + 1;
            int need_to_replace = window_size - *std::max_element(freqs, freqs + 26);
            if (need_to_replace <= k)
                result = std::max(result, window_size);
            
            // slide window until valid 
            while (end - start + 1 - *std::max_element(freqs, freqs + 26) > k)
            {   
                freqs[s[start] - 'A']--;
                start++;
            }
        }
        return result;
    }
};