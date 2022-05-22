from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        
        while l < r:
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                r = mid
            else:
                l = mid + 1
                
        if l >= len(nums):
            return len(nums)
        if l <= 0:
            return 0
        
        if nums[l] > target:
            return l
        return l + 1