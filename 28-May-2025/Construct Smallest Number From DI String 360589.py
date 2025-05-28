# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        a = list(range(1, len(pattern) + 2))
        ans = "9999999999999"
        for perm in permutations(a):
            val = True
            for i in range(len(pattern)):
                if pattern[i] == "D" and perm[i] < perm[i + 1]:
                    break
                if pattern[i] == "I" and perm[i] > perm[i + 1]:
                    break
                if i == len(pattern) - 1:
                    print(perm)
                    ans = min("".join(map(str, perm)), ans)

        return ans