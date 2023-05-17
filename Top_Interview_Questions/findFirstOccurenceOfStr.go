func strStr(haystack string, needle string) int {
    if len(haystack) < len(needle) {
        return -1;
    }

    start, end := 0, len(needle) - 1;

    for end < len(haystack) {
        var i int;
        for i = start; i <= end; i++ {
            if needle[i - start] != haystack[i] {
                start++;
                end = start + len(needle) - 1;
                break; 
            }
        }
        if i > end {
            return start;
        }
    }
    return -1;
}