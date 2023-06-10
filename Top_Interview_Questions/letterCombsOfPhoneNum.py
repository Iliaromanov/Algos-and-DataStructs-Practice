class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        dig2letter = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []
        def backtrack(cur_s: str, i: int):
            if i == len(digits):
                result.append(cur_s)
                return
            
            for letter in dig2letter[digits[i]]:
                cur_s += letter
                backtrack(cur_s, i+1)
                cur_s = cur_s[:-1]
        backtrack("", 0)
        return result