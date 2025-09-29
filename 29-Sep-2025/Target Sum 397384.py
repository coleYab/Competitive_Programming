# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        seen = defaultdict(set)
        ans = 0
        @cache
        def dfs(idx, cur):
            if idx >= len(nums):
                return cur == target

            left = dfs(idx + 1, cur - nums[idx])
            right = dfs(idx + 1, cur + nums[idx])
            return left + right
    
        ans = dfs(0, 0)
        return ans