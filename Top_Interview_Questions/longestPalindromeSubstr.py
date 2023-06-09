class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_str = s[0]
        for i in range(len(s)):
            l, r = i, i
            while r < len(s) - 1 and s[i] == s[r+1]:
                r += 1
            while l > 0 and s[i] == s[l-1]:
                l -= 1
            while l > 0 and r < len(s) - 1 and s[l-1] == s[r+1]:
                r += 1
                l -= 1
            
            max_str = max([max_str, s[l:r+1]], key=len)

        return max_str