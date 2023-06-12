func searchRange(nums []int, target int) []int {
    if len(nums) == 0 {
        return []int{-1, -1}
    }

    // find lower bound
    l, r := 0, len(nums) - 1
    for l < r {
        mid := l + (r - l) / 2
        if nums[mid] >= target {
            r = mid
        } else {
            l = mid + 1
        }
    }
    if nums[l] != target {
        return []int{-1, -1}
    }

    result := []int{l}

    // find upper bound
    r = len(nums) - 1 // no need to reset l
    end := l
    for l < r {
        mid := l + (r - l) / 2
        if nums[mid] <= target {
            if nums[mid] == target {
                end = mid
            }
            l = mid + 1
        } else {
            r = mid - 1
        }
    }
    if nums[l] == target && l > end {
        return append(result, l)
    }
    return append(result, end)
}