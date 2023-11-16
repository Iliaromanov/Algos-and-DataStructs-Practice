class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = {}
        for num in nums:
            if num in freqs:
                freqs[num] += 1
            else:
                freqs[num] = 1
        
        # bucket for each frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freqs.items():
            buckets[freq].append(num)

        result = []
        remaining = k
        for i in range(len(buckets) - 1, -1, -1):
            freq_bucket = buckets[i]
            for num in freq_bucket:
                result.append(num)
                remaining -= 1
                if remaining == 0:
                    break
            if remaining == 0:
                    break
        return result