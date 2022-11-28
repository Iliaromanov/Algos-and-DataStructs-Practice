
"""Memoization Solution"""
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


"""Tabulation Solution"""
def grid_traveler(m, n):
    table = [[0 for _ in range(n+1)] for _ in range(m+1)]
    if n > 0 and m > 0:
        table[1][1] = 1

    for r in range(m+1):
        for c in range(n+1):
            if r < m:
                table[r+1][c] += table[r][c]
            if c < n:
                table[r][c+1] += table[r][c]
    
    return table[m][n]



print(grid_traveler(3, 3))
