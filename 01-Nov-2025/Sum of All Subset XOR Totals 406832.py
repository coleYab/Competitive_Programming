# Problem: Sum of All Subset XOR Totals - https://leetcode.com/problems/sum-of-all-subset-xor-totals/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0

        for i in range(1 << len(nums)):
            cur = 0
            s = bin(i)[::-1]
            for i in range(len(s) - 2):
                if s[i] == '1':
                    cur = cur ^ nums[i]
            total += cur

        return total