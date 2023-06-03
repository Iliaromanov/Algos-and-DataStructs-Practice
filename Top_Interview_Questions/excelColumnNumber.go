// Runtime
// 0 ms
// Beats
// 100%
// Memory
// 2.1 MB
// Beats
// 99.50%

func titleToNumber(columnTitle string) int {
    result := 0;
    for _, r := range columnTitle {
      d := int(r) - 'A' + 1
      result = result * 26 + d
    }
    return result
}