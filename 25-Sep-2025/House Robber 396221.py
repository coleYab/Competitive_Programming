# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 10)
        ans = 0
        if len(nums) < 2:
            return max(nums)
    
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            if i >= 3:
                dp[i] = max(dp[i - 3] + nums[i], dp[i])

        return max(dp)