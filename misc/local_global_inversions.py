from typing import List

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        for i, num in enumerate(nums):
            if i - nums[i] > 1 or i - nums[i] < -1:
                return False

        return True 