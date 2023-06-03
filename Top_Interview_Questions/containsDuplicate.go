func containsDuplicate(nums []int) bool {
    seen := map[int]bool{}
    for _, n := range nums {
      if _, ok := seen[n]; ok {
        return true
      }
      seen[n] = true
    }
    return false
}