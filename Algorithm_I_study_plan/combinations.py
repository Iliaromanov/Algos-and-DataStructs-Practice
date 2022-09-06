from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def backtrack(cur_comb: List[int], start: int, remain: int):
            # solution found
            if remain == 0:
                result.append(cur_comb[:])
                return
            
            # iterate through potential solutions
            for i in range(start, n+1):
                # place current potential addition to comb
                cur_comb.append(i)
                
                # backtrack with that potential solution
                backtrack(cur_comb, i+1, remain-1)
                
                # remove addition to comb to try other possible solutions
                cur_comb.pop()
        
        backtrack([], 1, k)
        return result