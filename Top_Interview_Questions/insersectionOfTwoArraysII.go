func intersect(nums1 []int, nums2 []int) []int {
    m := map[int]int{}
    result := []int{}
    for _, n := range nums1 {
      if _, ok := m[n]; ok {
        m[n]++
      } else {
        m[n] = 1
      }
    }

    for _, n := range nums2 {
      if val, ok := m[n]; ok && val > 0 {
        m[n]--
        result = append(result, n)
      }
    }
    return result
}