class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums = list(set(nums))
        result = []
        def backtrack(i: int, cur: List[int]):
            if i >= len(nums):
                result.append(cur.copy())
                return

            cur.append(nums[i])
            backtrack(i+1, cur)
            cur.pop()
            backtrack(i+1, cur)

        backtrack(0, [])
        return result
        