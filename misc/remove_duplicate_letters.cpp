class Solution {
public:
    string removeDuplicateLetters(string s) {
        int count[26];
        int added[26];
        vector<char> stack;

        for (char c : s) ++count[c - 'a'];

        for (char c : s)
        {
            while (stack.size() && stack.back() >= c && !added[c - 'a'] && count[stack.back() - 'a'])
            {
                added[stack.back() - 'a'] = 0;
                stack.pop_back();
            }
            if (!added[c - 'a'])
            {
                stack.push_back(c);
                added[c - 'a'] = 1;
            }
                
            count[c - 'a']--;
        }
        std::string result = "";
        for (char c : stack)
            result += c;
        return result;
    }
};
