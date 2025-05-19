# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        allxor = nums2[0]
        for i in range(1, len(nums2)):
            allxor ^= nums2[i]
        
        ans = 0
        for num in nums1:
            if len(nums2) % 2 == 1:
                ans ^= num
            ans ^= allxor
        
        return ans