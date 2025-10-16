# Problem: Permutations II - https://leetcode.com/problems/permutations-ii/description/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perms = set()
        for i in permutations(nums):
            perms.add(tuple(i))
        return list(map(list, perms))