

func searchCleaner(nums []int, target int) int {
    l, r := 0, len(nums) - 1
    for l <= r {
        mid := (l + r) / 2
        if nums[mid] == target {
            return mid
        } else if nums[l] <= nums[mid] { // left side sorted part
            if nums[mid] < target || target < nums[l] {
                l = mid + 1
            } else {
                r = mid - 1
            }
        } else { // right side sorted part
            if nums[mid] > target || target > nums[r] {
                r = mid - 1
            } else {
                l = mid + 1
            }
        }
    }
    return -1
}


func search(nums []int, target int) int {
    // find index of min
    lo, hi := 0, len(nums) - 1
    for lo < hi {
        mid := lo + (hi - lo) / 2
        if nums[hi] < nums[mid] {
            lo = mid + 1
        } else {
            hi = mid
        }
    }
    shift := lo
    lo, hi = 0, len(nums)-1
    for lo < hi {
        mid := lo + (hi - lo) / 2
        real_mid := getIndex(mid, shift, len(nums))
        if nums[real_mid] == target {
            return real_mid
        } else if nums[real_mid] < target {
            lo = mid + 1
        } else {
            hi = mid
        }
    }
    if nums[getIndex(lo, shift, len(nums))] == target {
        return getIndex(lo, shift, len(nums))
    }
    return -1
}

func getIndex(i int, shift int, length int) int {
    return (i + shift) % length
}