class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start: int, remaining: int, cur: List[int]):
            if remaining == 0:
                result.append(cur.copy())
                return
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                candidate = candidates[i]

                cur.append(candidate)
                backtrack(i, remaining - candidate, cur)
                cur.pop()

        backtrack(0, target, [])

        return result
