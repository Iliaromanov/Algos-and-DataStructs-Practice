from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = defaultdict(lambda: defaultdict(int))
        def dp(i: int, cur_sum: int) -> int:
            if i == len(nums):
                return 1 if cur_sum == target else 0

            if i not in memo or cur_sum not in memo[i]:
                memo[i][cur_sum] = dp(i+1, cur_sum+nums[i]) + dp(i+1, cur_sum-nums[i])

            return memo[i][cur_sum]

        return dp(0, 0)