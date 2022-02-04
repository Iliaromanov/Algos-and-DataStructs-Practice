# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if (n == 1 and isBadVersion(1)):
            return 1
        
        left = 1
        right = n
        
        while True:
            if (left + 1 == right):
                if isBadVersion(left):
                    return left
                else:
                    return right
            
            mid = (left + right) // 2
            
            if not isBadVersion(mid):
                left = mid
            else:
                right = mid