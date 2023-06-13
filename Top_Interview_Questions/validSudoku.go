func isValidSudoku(board [][]byte) bool {
    seen := map[string]bool{}
    for row := 0; row < 9; row++ {
        for col := 0; col < 9; col++ {
            num := string(board[row][col])
            if num != "." {
                rowKey := fmt.Sprint(num, "row", row)
                if _, exists := seen[rowKey]; exists {
                    return false
                } else {
                    seen[rowKey] = true
                }
                colKey := fmt.Sprint(num, "col", col)
                if _, exists := seen[colKey]; exists {
                    return false
                } else {
                    seen[colKey] = true
                }
                boxKey := fmt.Sprint(num, "box", row/3, "-", col/3)
                if _, exists := seen[boxKey]; exists {
                    return false
                } else {
                    seen[boxKey] = true
                }
            }
        }
    }
    return true
}