from typing import List


def can_sum_recursive(target: int, nums: List[int]) -> bool:
    """
    Returns True if target can be created by summing one or more numbers in nums
    """
    if target == 0:
        return True

    if target < 0:
        return False

    for i in range(len(nums)):
        if can_sum_recursive(target - nums[i], nums):
            return True

    return False
