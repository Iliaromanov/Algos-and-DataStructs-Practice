func majorityElement(nums []int) int {
    candidate := nums[0]
    count := 0
    for _, num := range nums {
      if candidate == num {
        count++
        continue
      } else {
        count--
      }

      if count <= 0 {
        candidate = num
        count = 1
      }
    }
    return candidate;
}