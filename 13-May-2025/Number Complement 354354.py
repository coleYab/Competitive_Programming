# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        s = list(bin(num)[2:])
        ans = 0
        for i in s:
            if i == '0':
                ans = (ans << 1) + 1
            else:
                ans = (ans << 1)
                
        return ans
