from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        
        while l < r:
            m = l + (r - l) // 2
            result = numbers[l] + numbers[r]
            if result == target:
                return [l + 1, r + 1]
            elif result < target:
                if numbers[m] + numbers[r] < target:
                    l = m + 1
                else:
                    l += 1
            else:
                if numbers[m] + numbers[l] > target:
                    r = m - 1
                else:
                    r -= 1
        
        return -1


class SolutionAlt:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while 1:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1, r+1]
            