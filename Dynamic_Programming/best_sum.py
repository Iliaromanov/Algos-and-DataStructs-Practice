from typing import List, Dict


def best_sum(target: int, nums: List[int]) -> int:
    """
    Returns the smallest subset of nums that sums to target.
    None if no such subset exists
    """
    result = None

    def backtrack(target: int, subset: List[int]):
        if target == 0 and (not result or len(subset) < result):
            result = subset[::]
            return
        if target < 0:
            return None

        for num in nums:
            subset.append(num)

            backtrack(target - num, subset[::])

            subset.pop()

        return None

    backtrack(target, [])

    return result