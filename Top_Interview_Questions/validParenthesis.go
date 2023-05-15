func isValid(s string) bool {
    var stack []rune;
    opening := map[rune]rune{')': '(', '}': '{', ']': '['};
    for _, char := range s {
        opening_char, found := opening[char];
        if found {
            if len(stack) == 0 || stack[len(stack) - 1] != opening_char {
                return false;
            } else {
                stack = stack[:len(stack) - 1]; // pop
            }
        } else {
            stack = append(stack, char); // push
        }
    }
    return len(stack) == 0;
}