func search(nums []int, target int) int {
    if (len(nums) == 1) {
        if (nums[0] == target) {
            return 0;
        }
        return -1;
    }
    left := 0;
    right := len(nums) - 1;
    for (true) {
        if (left + 1 == right) {
            if (nums[left] == target) {
                return left;
            }
            if (nums[right] == target) {
                return right;
            }
            break;
        }
        mid := (left + right) / 2;
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] < target) {
            left = mid;
        } else {
            right = mid;
        }
    }
    return -1;
}