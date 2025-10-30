# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

from math import ceil

mod = 10 ** 9 + 7

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        return (pow(5, ceil(n / 2), mod=mod) * pow(4, n // 2, mod=mod)) % mod