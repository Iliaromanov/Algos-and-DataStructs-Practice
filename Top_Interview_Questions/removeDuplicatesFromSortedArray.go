func removeDuplicates(nums []int) int {
    slow, fast := 0, 1;
    l := len(nums);
    for fast < l {
        if nums[slow] == nums[fast] {
            fast++;
        } else {
            slow++;
            nums[slow] = nums[fast];
        }
    }
    return slow + 1;
}