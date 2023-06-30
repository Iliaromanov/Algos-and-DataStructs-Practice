class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(cur: List[int], i: int, cur_sum: int): # have sum arg for faster time
            if cur_sum == target:
                result.append(cur)
                return

            if cur_sum > target:
                return

            for idx, num in enumerate(candidates[i:]):
                backtrack(cur + [num], i+idx, cur_sum + num)

        backtrack([], 0, 0)

        return result