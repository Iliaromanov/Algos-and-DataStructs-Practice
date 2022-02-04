from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target <= nums[0]:
                return 0
            return 1
        
        l = 0
        r = len(nums) - 1
        
        while True:
            if l + 1 == r:
                if target <= nums[l]:
                    return l
                elif target <= nums[r]:
                    return r
                return r+1
            
            mid = (l + r) // 2
            
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid
            else:
                r = mid