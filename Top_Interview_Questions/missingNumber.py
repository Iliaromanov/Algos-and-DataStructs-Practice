class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      n = len(nums)
      sum_to_n = n * (n + 1) // 2
      sum_nums = sum(nums)
      return sum_to_n - sum_nums