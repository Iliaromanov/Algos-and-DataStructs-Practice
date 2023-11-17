class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    continue
                # row
                key = f"r{row}:{board[row][col]}"
                if key in seen:
                    return False
                seen.add(key)
                # column
                key = f"c{col}:{board[row][col]}"
                if key in seen:
                    return False
                seen.add(key)

                # subbox
                key = f"b{row // 3}-{col // 3}:{board[row][col]}"
                if key in seen:
                    return False
                seen.add(key)

        return True