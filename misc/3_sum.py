from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums) # O(n*log(n))
        if len(nums) < 3:
            return []

        if nums[0] > 0:
            return []

        seen = {}
        # O(n)
        for i, num in enumerate(nums):
            seen[num] = i

        # O(n^2)
        i = 0
        while i < len(nums):
            num1 = nums[i]
            # if num_1 positive then can't 
            #  find following numers to bring down to zero
            if num1 > 0:
                break
            j = i + 1
            while j < len(nums):
                num2 = nums[j]
                target = -1 * (num1 + num2)
                if target in seen and seen[target] > j:
                    result.append([num1, num2, target])
                
                j = seen[num2] # set j to last occurence of num2 to avoid duplicates
                j += 1
            
            i = seen[num1] # set i to last occurence of num1 to avoid duplicates
            i += 1

        return result

# Alternate solution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums) # O(n*logn)
        result = []
        known = {}

        # hash the whole array to know latest occurences
        for i, num in enumerate(nums):
            known[num] = i

        def twoSum(nums, num1): # O(n)
            nonlocal result
            l, r = 0, len(nums) - 1

            while l < r:
                triple = [num1, nums[l], nums[r]]
                if sum(triple) == 0 and (not result or result[-1] != triple):
                    result.append(triple)
                    l += 1
                elif sum(triple) < 0:
                    l += 1
                else:
                    r -= 1

        k = 0
        while k < len(nums):
            if nums[k] > 0:
                break
            twoSum(nums[k+1:], nums[k])
            k = known[nums[k]] + 1 # jump to latest occurence and increment

        return result