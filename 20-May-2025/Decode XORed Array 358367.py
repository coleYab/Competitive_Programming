# Problem: Decode XORed Array - https://leetcode.com/problems/decode-xored-array/description/

class Solution:
    def decode(self, en: List[int], first: int) -> List[int]:
        ans = [0 for i in range(len(en) + 1)]
        ans[0] = first
        for i in range(1, len(ans)):
            ans[i] = ans[i - 1] ^ en[i - 1]

        return ans