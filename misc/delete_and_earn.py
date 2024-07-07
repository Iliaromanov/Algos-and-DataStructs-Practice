class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count[num]+1 if num in count else 1
        count_pairs = sorted([[k, v] for k, v in count.items()], key=lambda x: x[0])

        dp = [0 for _ in range(len(count_pairs)+1)]
        dp[-2] = count_pairs[-1][0] * count_pairs[-1][1]

        for i in range(len(count_pairs)-2, -1, -1):
            neighbor_allowed = count_pairs[i][0] + 1 < count_pairs[i+1][0]
            dp[i] = max(
                count_pairs[i][0] * count_pairs[i][1] + dp[i+1 if neighbor_allowed else i+2],
                dp[i+1]
            )
        
        return max(dp[0], dp[1] if len(count_pairs) > 1 else 0)
        