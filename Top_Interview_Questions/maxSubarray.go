func maxSubArray(nums []int) int {
    max_sum := nums[0];
    for i := 1; i < len(nums); i++ {
        nums[i] = max(nums[i], nums[i] + nums[i-1])
        max_sum = max(nums[i], max_sum);
    }
    return max_sum;
}

func max(a int, b int) int {
    if a > b {
        return a;
    }
    return b;
}