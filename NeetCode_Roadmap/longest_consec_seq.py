class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        best = 0
        for num in nums:
            count = 1
            if num not in hash_set:
                continue
            lower, upper = num, num
            while lower is not None or upper is not None:
                if lower is not None:
                    hash_set.remove(lower)
                if upper is not None and lower != upper:
                    hash_set.remove(upper)
                
                if lower is not None and lower - 1 in hash_set:
                    lower -= 1
                    count += 1
                else:
                    lower = None

                if upper is not None and upper + 1 in hash_set:
                    upper += 1
                    count += 1
                else:
                    upper = None
            best = max(best, count)

            if len(hash_set) == 0:
                break

        return best
