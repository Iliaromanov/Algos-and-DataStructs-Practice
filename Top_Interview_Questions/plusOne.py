from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 0:
            return [1]
        if digits[len(digits) - 1] == 9:
            return self.plusOne(digits[:len(digits) - 1]) + [0]
        digits[len(digits) - 1] += 1
        return digits