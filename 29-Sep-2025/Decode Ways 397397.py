# Problem: Decode Ways - https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0 for i in range(n + 1)]
        dp[0] = 1             

        for i in range(n):
            if s[i] != '0':
                dp[i + 1] = dp[i]
            else:
                dp[i + 1] == 0
            if i > 0:
                p = int(s[i - 1:i + 1])
                if 10 <= p <= 26:
                    dp[i + 1] += dp[i - 1]
        return dp[n]
                
            