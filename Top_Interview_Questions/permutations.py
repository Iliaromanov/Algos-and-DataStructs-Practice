class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(cur: List[int], rem: List[int]):
            if len(rem) == 0:
                result.append(cur)
            
            for num in rem:
                rem_cp = rem.copy()
                rem_cp.remove(num)
                backtrack(cur + [num], rem_cp)
        
        backtrack([], nums)
        
        return result