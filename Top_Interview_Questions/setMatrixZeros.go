func setZeroes(matrix [][]int)  {
    zeroFirstRow := false
    zeroFirstCol := false
    for i := 0; i < len(matrix); i++ {
        for j := 0; j < len(matrix[0]); j++ {
            if matrix[i][j] == 0 {
                if i == 0 {
                    zeroFirstRow = true
                }
                if j == 0 {
                    zeroFirstCol = true
                }
                matrix[0][j] = 0
                matrix[i][0] = 0
            }
        }
    }

    // zero out columns
    for i := 1; i < len(matrix[0]); i++ {
        if matrix[0][i] == 0 {
            for j := 1; j < len(matrix); j++ {
                matrix[j][i] = 0
            }
        }
    }

    // zero out rows
    for i := 1; i < len(matrix); i++ {
        if matrix[i][0] == 0 {
            for j := 1; j < len(matrix[0]); j++ {
                matrix[i][j] = 0
            }
        }
    }

    if zeroFirstRow == true {
        for i := 0; i < len(matrix[0]); i++ {
            matrix[0][i] = 0;
        }
    }
    if zeroFirstCol == true {
        for i := 0; i < len(matrix); i++ {
            matrix[i][0] = 0;
        }
    }
}