func canJump(nums []int) bool {
    if len(nums) == 1 {
        return true
    }
    cur := len(nums) - 1
    for i := cur - 1; i >= 0; i-- {
        if i + nums[i] >= cur {
            cur = i
        }
    }
    if cur == 0 {
        return true
    }
    return false
}