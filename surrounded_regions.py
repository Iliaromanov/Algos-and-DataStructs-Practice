from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def mark_not_surrounded(r, c):
            board[r][c] = "N"

            for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_r, new_c = r + i, c + j

                if 0 <= new_r < len(board) and 0 <= new_c < len(board[0]) and \
                   board[new_r][new_c] == "O":
                   mark_not_surrounded(new_r, new_c)

        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O" and (
                    r == 0 or r == len(board) - 1 or c == 0 or c == len(board[0]) - 1
                ):
                    mark_not_surrounded(r, c)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "N":
                    board[r][c] = "O"