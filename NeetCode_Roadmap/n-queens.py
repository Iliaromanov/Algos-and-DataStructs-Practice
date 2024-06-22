class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        state = [['.']*n for _ in range(n)]
        visited_cols = set()
        visited_diagonals = set() # if cells in same diagonal, their col - row is the same
        visited_antidiagonals = set() # if cells in same antidiagonal, their row + col

        def backtrack(row: int):
            if row == n:
                result.append(["".join(r) for r in state])
                return
            
            for col in range(n):
                diff = col - row
                _sum = col + row
                if not (col in visited_cols or diff in visited_diagonals or _sum in visited_antidiagonals):
                    state[row][col] = 'Q'
                    visited_cols.add(col)
                    visited_diagonals.add(diff)
                    visited_antidiagonals.add(_sum)

                    backtrack(row+1)

                    state[row][col] = '.'
                    visited_cols.remove(col)
                    visited_diagonals.remove(diff)
                    visited_antidiagonals.remove(_sum)

        backtrack(0)
        return result