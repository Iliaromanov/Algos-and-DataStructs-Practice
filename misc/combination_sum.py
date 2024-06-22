from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtracking(cur: List[int]):
            s = sum(cur)
            if s == target and sorted(cur) not in result:
                result.append(sorted(cur.copy()))
                return
            if s > target:
                return
            
            for candidate in candidates:
                cur.append(candidate)
                
                backtracking(cur.copy())
                
                cur.remove(candidate)
                
        backtracking([])
        
        return result
        