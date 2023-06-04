func isAnagram(s string, t string) bool {
    sFreqs := getFreqMap(s)
    tFreqs := getFreqMap(t)

    if len(sFreqs) != len(tFreqs) {
      return false
    }

    for k, v := range tFreqs {
      if sVal, found := sFreqs[k]; found {
        if sVal != v {
          return false
        }
      } else {
        return false
      }
    }
    return true
}

func getFreqMap(s string) map[rune]int {
  runes := []rune(s)
  result := map[rune]int{}
  for _, r := range runes {
    if _, found := result[r]; found {
      result[r]++
    } else {
      result[r] = 0
    }
  }
  return result
}