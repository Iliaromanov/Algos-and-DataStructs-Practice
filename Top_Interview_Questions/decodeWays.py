class Solution:
    def numDecodings(self, s: str) -> int:
        """
        subproblem: dp(i) = num ways to decode s[i:]
        answer: dp(0)
        recurrence: dp(i) = (dp(i+1), if i+1 < len(s) and 1 <= s[i] <= 26 and s[i+1] != 0 else 0) +
                            (dp(i+2), if i+2 < len(s) and 1 <= s[i:i+2] <= 26 else 0)
        """
        dp = [0 for _ in range(len(s))]

        # Base cases
        if s[-1] != "0" and 1 <= int(s[-1]) <= 26:
            dp[-1] = 1
        if len(s) >= 2 and s[-2] != "0":
            if 1 <= int(s[-2:]) <= 26:
                dp[-2] = 1 + dp[-1]
            else:
                dp[-2] = dp[-1]

        # recurrence
        for i in range(len(s)-3, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                continue
            sol1 = dp[i+1] if i+1 < len(s) and 1 <= int(s[i]) <= 26 else 0
            sol2 = dp[i+2] if i+2 < len(s) and 1 <= int(s[i:i+2]) <= 26 else 0
            dp[i] = sol1 + sol2

        return dp[0]