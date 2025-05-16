# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans = 0
        left = 0
        cur = 0

        for right in range(len(nums)):
            while left < right and cur & nums[right] != 0:
                cur = cur ^ nums[left]
                left += 1
            cur = cur | nums[right]
            ans = max(right - left + 1, ans)

        return ans