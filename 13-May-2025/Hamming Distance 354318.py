# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        while x or y:
            ans += (x & 1) ^ (y & 1)
            x = x >> 1
            y = y >> 1
            print(x, y)
        return ans