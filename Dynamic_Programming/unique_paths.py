class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        solved = {}
        
        def dp(m, n):            
            if m == 1 and n == 1:
                return 1
            if (m, n) in solved:
                return solved[(m, n)]
            
            if m != 1 and n != 1:
                solved[(m, n)] = dp(m-1, n) + dp(m, n-1)
            elif m == 1:
                solved[(m, n)] = dp(m, n-1)
            else:
                solved[(m, n)] = dp(m-1, n)
            
            return solved[(m, n)]
        
        return dp(m, n)