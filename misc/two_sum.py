# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            tmp_lst = [n for n in nums]
            tmp_lst.remove(num)
            
            try:
                pair_num_idx = tmp_lst.index(target - num)
                
                if pair_num_idx >= i:
                    pair_num_idx += 1
                
                return [i, pair_num_idx]
            except ValueError:
                continue
