func generateParenthesis(n int) []string {
    return backtrack([]string{}, "", n, 0);
}

func backtrack(result []string, cur_s string, n int, m int) []string {
    if n == 0 && m == 0 {
        result = append(result, cur_s);
        return result;
    }

    if n > 0 {
        result = backtrack(result, cur_s + "(", n-1, m+1);
    }

    if m > 0 {
        result = backtrack(result, cur_s + ")", n, m-1);
    }
    
    return result;
}