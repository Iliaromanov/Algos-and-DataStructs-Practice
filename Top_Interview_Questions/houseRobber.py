class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        let dp[i] = max profit starting at house index i
        answer: dp[0]
        recurr: dp[i] = max(nums[i] + dp[i + 2], dp[i+1])
        base: dp[-1] = nums[-1], dp[-2] = max(nums[-2], num[-1])
        """
        if len(nums) == 1: return nums[0]
        nums[-2] = max(nums[-2], nums[-1])
        for i in range(len(nums)-3, -1, -1):
            nums[i] = max(nums[i] + nums[i + 2], nums[i+1])

        return nums[0]
