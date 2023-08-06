class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_min = nums.copy()
        dp_max = nums.copy()
        for i in range(len(nums)-2, -1, -1):
            dp_min[i] = min(nums[i], dp_min[i+1]*nums[i], dp_max[i+1]*nums[i])
            dp_max[i] = max(nums[i], dp_min[i+1]*nums[i], dp_max[i+1]*nums[i])

        return max(dp_max)