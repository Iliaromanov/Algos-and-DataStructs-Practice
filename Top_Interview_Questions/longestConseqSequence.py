class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)  # python sets are implemented as hash sets
        longest_seq = 0
        for num in hashSet:
            if (num - 1) in hashSet:  # O(1) because hashSet
                continue

            seq_len = 1
            seq_num = num + 1
            while seq_num in hashSet:
                seq_num += 1
                seq_len += 1
            
            if seq_len > longest_seq: longest_seq = seq_len

        return longest_seq