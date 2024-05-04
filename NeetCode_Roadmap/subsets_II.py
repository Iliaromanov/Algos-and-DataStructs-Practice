class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(sub: List[int], i: int):
            if i == len(nums):
                result.append(sub.copy())
                return

            val = nums[i]
            backtrack(sub + [val], i+1)
            while i < len(nums) and nums[i] == val:
                i += 1
            
            backtrack(sub, i)

        backtrack([], 0)

        return result
