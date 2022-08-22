class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0 for n in nums]
        l = 0
        r = len(nums) - 1
        
        for i in range(len(nums) - 1, -1, -1):
            if abs(nums[l]) > abs(nums[r]):
                result[i] = nums[l] ** 2
                l += 1
            else:
                result[i] = nums[r] ** 2
                r -= 1
                
        return result