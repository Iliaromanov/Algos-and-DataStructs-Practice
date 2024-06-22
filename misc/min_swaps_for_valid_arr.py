class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        _min, _max = min(nums), max(nums)
        _min_d = nums.index(_min)
        _max_d = 0
        _max_i = len(nums) - 1

        while nums[_max_i] != _max:
            _max_i -= 1
            _max_d += 1

        sum_d = _min_d + _max_d

        if nums.index(_min) <= _max_i:
            return sum_d
        return sum_d - 1