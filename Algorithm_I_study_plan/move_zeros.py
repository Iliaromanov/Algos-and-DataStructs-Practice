from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        glob_i = 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[glob_i] = num
                glob_i += 1
        
        while glob_i < len(nums):
            nums[glob_i] = 0
            glob_i += 1