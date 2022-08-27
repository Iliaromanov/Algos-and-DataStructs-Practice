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