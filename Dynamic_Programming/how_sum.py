from typing import List, Dict

def how_sum_recursive(target: int, nums: List[int]) -> List[List[int]]:
    """
    Returns ANY SINGLE combinations from nums that sums to target
    """

    def backtrack(t: int, cur: List[int]):
        if t == 0:
            return cur
        if t < 0:
            return None

        for num in nums:
            cur.append(num)

            result = backtrack(t - num, cur[::])
            if result:
                return result 

            cur.pop()

        return None

    return backtrack(target, [])


print(how_sum_recursive(7, [5, 3, 4, 7]))