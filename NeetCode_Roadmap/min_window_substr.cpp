class Solution {
public:
    bool containsChars(std::unordered_map<char, int>& s_char_counts, std::unordered_map<char, int>& t_char_counts)
    { // return true if s_char_counts contain subset of chars of t_char_counts
      //  count of s_char_counts >= t_char_counts
      for (const auto &p : t_char_counts)
      {
        if (const auto it = s_char_counts.find(p.first); 
           it == s_char_counts.end() || it->second < p.second)
            return false;
      }
      return true;
    }

    string minWindow(string s, string t) {
        if (s == "" || t == "")
            return "";
        string result = "";
        std::unordered_map<char, int> t_char_counts;
        for (char c : t) {
            if (t_char_counts.find(c) == t_char_counts.end())
                t_char_counts[c] = 1;
            else
                t_char_counts[c]++;
        }
        int left = 0;
        int right = 0;
        std::unordered_map<char, int> s_char_counts;

        while (right < s.size()) {
            if (t_char_counts.find(s[right]) != t_char_counts.end()) {
                if (s_char_counts.find(s[right]) != s_char_counts.end())
                    s_char_counts[s[right]]++;
                else
                    s_char_counts[s[right]] = 1;
            }

            if (containsChars(s_char_counts, t_char_counts))
            {
                while (left <= right && containsChars(s_char_counts, t_char_counts)) {
                    if (s_char_counts.find(s[left]) != s_char_counts.end()) {
                        s_char_counts[s[left]]--;
                        if (s_char_counts[s[left]] == 0)
                            s_char_counts.erase(s[left]);
                    }
                    left++;
                }
                if (result == "" || right - left + 2 < result.size()) // + 2 cus of the above if cond
                {
                    result = s.substr(left-1, right - left + 2);
                }
            }

            right++;
        }
        return result;
    }
};