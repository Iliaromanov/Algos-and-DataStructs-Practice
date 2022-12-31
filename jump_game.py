from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        i = goal - 1

        while i >= 0:
            if i + nums[i] >= goal:
                goal = i

            i -= 1

        return goal == 0