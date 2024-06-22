class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sums = []
        s = 0
        for num in nums:
            s += num
            self.prefix_sums.append(s)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_sums[right]
        return self.prefix_sums[right] - self.prefix_sums[left - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)