func twoSum(nums []int, target int) []int {
    seen := make(map[int]int);

    for i, num := range nums {
        if matching_i, found := seen[target - num]; found {
            return []int{matching_i, i};
        } else {
            seen[num] = i;
        }
    }

    return []int{-1, -1};
}