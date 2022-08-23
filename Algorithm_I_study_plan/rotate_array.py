from typing import List

class Solution:
    """
    Linear Space Solution
    """
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        steps = k % len(nums)
        
        result = [n for n in nums]
        
        for i, num in enumerate(result):
            nums[(i + steps) % len(nums)] = num