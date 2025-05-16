# Problem: Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left.bit_length() != right.bit_length():
            return 0

        size = left.bit_length()
        ans = 0

        for i in range(size, -1, -1):
            if (left >> i) != (right >> i):
                break
            ans |= (left >> i) << i

        return ans