class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(cur_s: str, rem: int, unclosed: int):
            if rem + unclosed == 0:
                result.append(cur_s)
                return

            if rem > 0:
                backtrack(cur_s + "(", rem-1, unclosed+1)
            
            if unclosed > 0:
                backtrack(cur_s+")", rem, unclosed-1)

        backtrack("", n, 0)
        return result