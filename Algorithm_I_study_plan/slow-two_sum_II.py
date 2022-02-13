class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while 1:
            result = numbers[left] + numbers[right]
            if result == target:
                return [left + 1, right + 1]
            elif result > target:
                right -= 1
            else:
                left += 1