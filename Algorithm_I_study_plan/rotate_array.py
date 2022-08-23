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



class Solution:
    """
    O(n) time, O(1) space
    """
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        steps = k % len(nums)
        
        # reverse entire list
        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
            
        # reverse up to k - 1
        l, r = 0, steps - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        
        # reverse k to end of list
        l, r = steps, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
            