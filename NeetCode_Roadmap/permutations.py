class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(comb: List[int], rem: List[int]):
            if len(rem) == 0:
                result.append(comb.copy())

            for i, val in enumerate(rem):
                comb.append(val)
                backtrack(comb, rem[:i] + (rem[i+1:] if i < len(rem)-1 else []))
                comb.pop()

        backtrack([], nums)

        return result
