class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prod = 1
        for num in nums:
            result.append(prod)
            prod *= num
        
        prod = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= prod
            prod *= nums[i]

        return result