from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        
        def backtracking(cur_s, start_i):
            if start_i == len(s):
                result.append(cur_s[:])
                return
            
            if s[start_i].isalpha():
                cur_s += s[start_i].upper()
                backtracking(cur_s, start_i+1)
                cur_s = cur_s[:-1] # same as .pop()
                cur_s += s[start_i].lower()
                backtracking(cur_s, start_i+1)
            else:
                cur_s += s[start_i]
                backtracking(cur_s, start_i+1)
                
        backtracking("", 0)
        
        return result