class Solution:
    def climbStairs(self, n: int) -> int:
        solved = {}
        
        def memoization(n: int) -> int:
            if n == 1:
                return 1
            if n == 2:
                return 2
            
            if n in solved:
                return solved[n]
            
            solved[n] = memoization(n-1) + memoization(n-2)
            
            return solved[n]
        
        return memoization(n)
        