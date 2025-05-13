# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0 for i in range(n + 1)]

        for i in range(n + 1):
            for j in bin(i)[2:]:
                ans[i] += int(j == '1')

        return ans