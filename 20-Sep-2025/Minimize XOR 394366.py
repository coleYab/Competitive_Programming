# Problem: Minimize XOR - https://leetcode.com/problems/minimize-xor/description/

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        sz = num2.bit_count()
        ans = num1
        sz -= num1.bit_count()
        # print(ans, sz)

        for i in range(0, 32):
            if sz >= 0:
                break
            if (ans >> i) & 1 == 1:
                ans ^= (1 << i)
                sz += 1

        for i in range(0, 32):
            if sz == 0:
                break
            if (ans >> i) & 1 == 0:
                ans |= (1 << i)
                sz -= 1
        return ans