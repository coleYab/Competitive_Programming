# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

#!/usr/bin/env python3
import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        heapq.heapify(nums)

        # print(nums)

        while nums[0] < k:
            n1 = heapq.heappop(nums)
            n2 = heapq.heappop(nums)
            heapq.heappush(nums, max(n1, n2) + min(n1, n2) * 2)
            # print(nums)
            ans += 1

        return ans
