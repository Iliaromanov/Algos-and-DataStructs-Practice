func firstUniqChar(s string) int {
    runes := []rune(s)
    m := map[rune]int{}
    for _, r := range runes {
      if _, found := m[r]; found {
          m[r]++
      } else {
          m[r] = 1
      }
    }
    for i, r := range runes {
        count := m[r]
        if count == 1 {
            return i
        }
    }
    return -1
}