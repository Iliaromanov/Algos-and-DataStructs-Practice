class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(comb: List[int], total: int, start: int):
            if total == target:
                result.append(comb)
                return
            
            if total > target:
                return

            i = start
            while i < len(candidates):
                val = candidates[i]
                backtrack(comb + [val], total + val, i+1)
                while i < len(candidates) and candidates[i] == val:
                    i += 1

        backtrack([], 0, 0)
        return result
