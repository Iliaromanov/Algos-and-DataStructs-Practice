func lengthOfLongestSubstring(s string) int {
    if len(s) <= 1 {
        return len(s)
    }
    maxlen := 0
    runes := []rune(s)
    seen := map[rune]int{runes[0]: 0}
    start, end := 0, 1
    for end < len(runes) {
        if i, exists := seen[runes[end]]; exists {
            // update max
            if end - start > maxlen {
                maxlen = end - start
            }
            if i >= start {
                start = i+1;
            }
        }
        seen[runes[end]] = end
        end++
    }
    // update max
    if end - start > maxlen {
        return end - start
    }
    return maxlen
}