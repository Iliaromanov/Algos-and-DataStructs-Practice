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


"""TABULATION"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        table = [0 for _ in range(n+1)]
        table[1] = 1
        table[2] = 1

        for i, num in enumerate(table):
            if i+1 < len(table): table[i+1] += num
            if i+2 < len(table): table[i+2] += num

        return table[n]
        