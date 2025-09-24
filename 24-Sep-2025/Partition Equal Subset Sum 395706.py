# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = {}

        def dfs(idx, total, target):
            state = (idx, total)
            if state in dp:
                return dp[state]
            
            if total == target:
                return True

            if idx >= len(nums):
                return False

            dp[state] = dfs(idx + 1, total + nums[idx], target) or dfs(idx + 1, total, target)
            # print(state, dp)
            return dp[state]

        tot = sum(nums)
        if tot % 2 == 0:
            return dfs(0, 0, tot // 2)

        return False
            