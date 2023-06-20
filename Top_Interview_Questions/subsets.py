class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(cur: List[int], i: int):
            if i == len(nums):
                result.append(cur)
                return

            backtrack(cur + [nums[i]], i+1)
            backtrack(cur, i+1)

        backtrack([], 0)
        return result