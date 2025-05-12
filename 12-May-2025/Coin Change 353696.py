# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], n: int) -> int:
        dp = [float("inf") for i in range(n + 1)]
    
        dp[0] = 0
        for i in range(1, n + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[max(0, i - c)] + 1)

        return dp[n] if dp[n] != float("inf") else -1