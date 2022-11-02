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


print(best_sum(8, [1, 5, 4]))
print(best_sum(100, [1, 2, 5, 25]))

