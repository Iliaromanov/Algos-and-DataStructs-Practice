from typing import List, Dict, Tuple


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


def can_sum_memo(target: int, nums: List[int], memo: Dict[int, bool] = {}) -> bool:
    """
    Returns True if target can be created by summing one or more numbers in nums
    """    
    if target == 0:
        memo[target] = True
        return True

    if target < 0:
        memo[target] = False
        return False

    if target in memo:
        return memo[target]

    for num in nums:
        memo[target] = can_sum_memo(target - num, nums, memo)
        if memo[target]:
            return True

    memo[target] = False
    return False


def can_sum_tab(target: int, nums: List[int]) -> bool:
    table = [False for _ in range(target+1)]
    table[0] = True

    for i, can_sum_to_i in enumerate(table):
        if can_sum_to_i:
            for num in nums:
                if i + num < target + 1:
                    table[i+num] = True

    return table[target]
