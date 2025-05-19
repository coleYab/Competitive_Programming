# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        letts = []
        for idx, i in enumerate(s):
            if i.islower() or i.isupper():
                letts.append(idx)

        if not letts:
            return [s]
        for i in range(1 << len(letts)):
            cur = [i if not (i.isupper() or i.islower()) else i.lower() for i in s]
            for idx, v in enumerate(bin(i)[2:][::-1]):
                if v == '1':
                    cur[letts[idx]] = cur[letts[idx]].upper()
        
            ans.append("".join(cur))            

        return ans