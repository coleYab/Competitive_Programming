# Problem: Heaters - https://leetcode.com/problems/heaters/

from typing import *
from collections import *

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
    
        def check(mid):
            idx = 0
            for num in houses:
                while idx < len(heaters) and not (heaters[idx] - mid <= num <= heaters[idx] + mid):
                    idx += 1
                    if idx == len(heaters):
                        return False
    
            return idx < len(heaters)

        ans = 0
        left, right = 0, 1 << 100
        while left <= right:
            mid = (left +right) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans