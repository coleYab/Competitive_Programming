# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))]

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue
                dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)