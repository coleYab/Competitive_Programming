# Problem: Permutation Sequence - https://leetcode.com/problems/permutation-sequence/description/

from itertools import permutations

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        a = [i for i in range(1, n + 1)]
        perms = []
        for i in permutations(a):
            perms.append(list(i))
        perms.sort()
        return ''.join(map(str, perms[k - 1]))
