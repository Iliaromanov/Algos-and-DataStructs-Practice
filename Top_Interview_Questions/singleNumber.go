func singleNumber(nums []int) int {
    // use XOR; A ^ A = 0, so all duplicates give zero
    // and 0 ^ B = B; this will give the unique number
    ans := 0;
    for _, num := range nums {
        ans ^= num; // ans XOR num
    }
    return ans;
}