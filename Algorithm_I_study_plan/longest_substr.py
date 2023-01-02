class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        seen = {s[0]: 0} # shows earliest occurence of each char in cur_s
        max_l = 1
        cur_l = 1
        cur_s = s[0]
        start, end = 0, 1
        while end < len(s):
            if s[end] not in cur_s:
                cur_l += 1
                cur_s += s[end]
            else:
                if cur_l > max_l:
                    max_l = cur_l
                # move start of window to earliest occurence of duplicate char
                start = seen[s[end]] + 1
                cur_s = s[start:end+1]
                cur_l = len(cur_s)
            
            seen[s[end]] = end
            end += 1
            
        if cur_l > max_l:
            max_l = cur_l
            
        return max_l

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        max_len = 1
        seen = { s[0]: 0 }
        l, r = 0, 1
        while r < len(s):
            if s[r] in seen.keys() and seen[s[r]] >= l:
                max_len = max(max_len, r - l)
                l = seen[s[r]] + 1
            else:
                max_len = max(max_len, r - l + 1)
            seen[s[r]] = r
            r += 1
        
        return max_len
