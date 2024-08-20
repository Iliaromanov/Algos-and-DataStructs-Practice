class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        """
        freqs = {...}
        power_uniq = sorted(freqs.keys())

        let dp[i] = max total power in power_uniq[:i]
        ans dp(len(power_uniq))
        base dp[i] = 0
        recur dp(i) = max(
            power_uniq[i]*freqs[power_uniq[i]] + dp[i+3],
            dp[i+1]
        )
        """
        freqs = defaultdict(int)
        for n in power:
            freqs[n] += 1

        power_unique = sorted(freqs.keys())

        dp = [0] * (len(power_unique) + 3)

        for i in range(len(power_unique)-1, -1, -1):
            p = power_unique[i]
            j = i
            while j < len(power_unique) and power_unique[j] <= p+2:
                j += 1
            dp[i] = max(
                p * freqs[p] + dp[j], # take power
                dp[i+1] # don't take power
            )

        return dp[0]