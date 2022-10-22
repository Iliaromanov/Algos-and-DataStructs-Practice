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


def how_sum_memo(target: int, nums: List[int]) -> List[List[int]]:
    """
    Returns ANY SINGLE combinations from nums that sums to target
    """

    def backtrack_memo(t: int, cur: List[int], memo = {}):
        if t == 0:
            return cur
        if t < 0:
            return None

        if t in memo:
            return memo[t]

        for num in nums:
            cur.append(num)

            result = backtrack_memo(t - num, cur[::])
            memo[t] = result
            if result:
                return result 

            cur.pop()

        memo[t] = None
        return None

    return backtrack_memo(target, [])


print(how_sum_recursive(8, [2, 3, 5]))
print(how_sum_memo(300, [7, 14]))
print(how_sum_memo(7, [5, 3, 4, 7]))
