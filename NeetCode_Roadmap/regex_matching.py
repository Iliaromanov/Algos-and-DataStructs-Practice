class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        let dp(i, j) be do s[:i+1] and p[:j+1] match
        ans dp(len(s)-1,len(p)-1)
        base case dp(i, j) = False, dp(0, 0) = True, dp(0, k) = True for all p[:k] convertable to "" 
        recur dp(i, j) = 
            case isaplpha(j)
                ... = dp(i-1,j-1) and s[i] == p[j]

            case j == .
                dp(i-1,j-1)

            case j == *
                # use
                dp(i-1, j) and s[i] == p[j-1] or p[j-1] == '.'
                # don't use
                dp(i, j-2)

        """
        s = '_' + s
        p = '_' + p
        dp = [[False for _ in range(len(p))] for _ in range(len(s))]
        dp[0][0] = True

        # mark patterns reducable to "" true for s=""
        for i in range(len(p)):
            if p[i] == "*" and (dp[0][i-1] or dp[0][i-2]):
                dp[0][i] = True

        for i in range(1, len(s)):
            for j in range(1, len(p)):
                if p[j] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == "*":
                    dp[i][j] = (
                        (dp[i-1][j] and (s[i] == p[j-1] or p[j-1] == '.')) or   # use '*'
                        dp[i][j-2] # don't use '*'
                    )
                else:
                    dp[i][j] = s[i] == p[j] and dp[i-1][j-1]

        return dp[len(s)-1][len(p)-1]