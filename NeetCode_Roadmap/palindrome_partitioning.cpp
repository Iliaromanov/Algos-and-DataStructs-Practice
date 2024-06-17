/*
Time Complexity:
O(n^2 * 2^n)
- The number of possible partitions is the same as the number of
possible outcomes of placing a "|" in between chars in s.
there are n-1 such positions, and at each position we can either place "|" or not.
Thus there is 2^(n-1) possible partitions

the n^2 is for the loop in the backtracking and calling .substr inside it

*/


class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> result;
        vector<string> empty{};
        backtrack(0, empty, result, s);
        return result;
    }

    void backtrack(int start, vector<string>& cur_comb, vector<vector<string>>& result, string_view s)
    {
        if (start == s.length())
        {
            result.emplace_back(cur_comb);
            return;
        }

        for (int i = start+1; i <= s.length(); ++i)
        {
            string sub = string(s.substr(start, i-start));
            if (is_palindrome(sub))
            {
                cur_comb.push_back(sub);
                backtrack(i, cur_comb, result, s);
                cur_comb.pop_back();
            }
        }
    }

    bool is_palindrome(string_view s)
    {
        int l = 0, r = s.length() - 1;
        while (l < r)
        {
            if (s[l] != s[r]) return false;
            ++l;
            --r;
        }
        return true;
    }
};