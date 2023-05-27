func generate(numRows int) [][]int {
    // init answer
    var triangle [][]int;
    for i := 0; i < numRows; i++ {
        level := make([]int, i+1);
        level[0] = 1;
        level[i] = 1;
        triangle = append(triangle, level);
    }

    // start at row 3 cus first two filled above
    for row := 2; row < numRows; row++ {
        for col := 1; col < row; col++ {
            triangle[row][col] = triangle[row-1][col-1] + triangle[row-1][col];
        }
    }
    return triangle;
}