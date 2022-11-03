from typing import List, Dict


def best_sum(target: int, nums: List[int]) -> int:
    """
    Returns the smallest subset of nums that sums to target.
    None if no such subset exists
    """
    if target == 0:
        return []
    
    if target < 0:
        return None

    shortest_combo = None

    for num in nums:
        remainder = target - num
        remainder_comb = best_sum(remainder, nums)
        if remainder_comb != None:
            comb = remainder_comb + [num]
            if not shortest_combo or len(comb)<len(shortest_combo):
                shortest_combo = comb
    
    return shortest_combo

def best_sum_memo(target: int, nums: List[int], memo={}) -> int:
    """
    Returns the smallest subset of nums that sums to target.
    None if no such subset exists
    """
    if target in memo:
        return memo[target]

    if target == 0:
        return []
    
    if target < 0:
        return None

    shortest_combo = None

    for num in nums:
        remainder = target - num
        remainder_combo = best_sum_memo(remainder, nums, memo)
        if remainder_combo != None:
            comb = remainder_combo + [num]
            if not shortest_combo or len(comb)<len(shortest_combo):
                shortest_combo = comb
    
    memo[target] = shortest_combo
    return shortest_combo
