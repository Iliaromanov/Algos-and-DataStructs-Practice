class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def isPalindrome(s: str) -> bool:
            return s == s[::-1]  # O(n); (same as 2 pointer approach)

        def backtrack(i: int, cur_parts: List[str]) -> None:
            if i >= len(s):
                result.append(cur_parts)
                return

            for split_i in range(i+1, len(s)+1):
                if isPalindrome(s[i:split_i]):
                    backtrack(split_i, cur_parts + [s[i:split_i]])


        backtrack(0, [])
        
        return result