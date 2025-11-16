# Problem: Distribute Candies Among Children II - https://leetcode.com/problems/distribute-candies-among-children-ii/

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def comb(a, b):
            if a < b or b < 0:
                return 0
            return math.comb(a, b)
        
        ans = 0
        for k in range(0, 4):
            ans += ((-1) ** k) * comb(3, k) * comb(n - k * (limit + 1) + 2, 2)
        return ans