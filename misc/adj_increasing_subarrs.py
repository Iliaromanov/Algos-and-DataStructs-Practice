class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        """
        1,2,3, -2,-1,0
        """
        nums.append(float('-inf'))
        p1, p2 = 1, k+1
        seen_len = 1
        while p2 < len(nums):
            if nums[p1] > nums[p1-1] and nums[p2] > nums[p2-1]:
                seen_len += 1
                if seen_len >= k:
                    return True
            else:
                seen_len = 1
            p1+=1
            p2+=1

        return seen_len == k