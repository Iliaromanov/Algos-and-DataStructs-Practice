package main

func rotate(nums []int, k int)  {
    result := make([]int, len(nums), len(nums));
    l := len(nums);    
    for i := 0; i < l; i++ {
        new_i := (i + k) % l;
        result[new_i] = nums[i];
    }
    copy(nums, result);
}