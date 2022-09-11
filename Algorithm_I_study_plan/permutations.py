from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def backtrace(cur_perm, remaining):
            # reached solution
            if not remaining:
                result.append(cur_perm[:])
                return
                
            # iterate over possibilities
            for num in remaining:
                # add it to cur_perm and rm from remaining
                cur_perm.append(num)
                new_remaining = remaining[:]
                new_remaining.remove(num)
                
                # backtrace with cur_perm
                backtrace(cur_perm, new_remaining)
                
                # rm from cur_perm
                cur_perm.pop()
            
            
        backtrace([], nums[:])
        
        return list(result) 