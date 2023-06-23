class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        translations = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def find_word(row: int, col: int, board: List[List[str]], target: str) -> bool:
            if target == "":
                return True

            result = False
            old = board[row][col]
            board[row][col] = "0"  # mark visited
            for i, j in translations:
                new_r = row + i
                new_c = col + j
                if 0 <= new_r < len(board) and 0 <= new_c < len(board[0]) and board[new_r][new_c] == target[0]:
                    result = result or find_word(new_r, new_c, board, target[1:])
                
                if result is True:
                    return True

            board[row][col] = old

            return result

        result = False
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    result = result or find_word(r, c, board, word[1:])

                if result is True:
                    return True

        return result