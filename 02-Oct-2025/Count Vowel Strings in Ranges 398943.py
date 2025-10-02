# Problem: Count Vowel Strings in Ranges - https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        ps = [0] * (n + 1)

        vl = set('aeiou')
        for i in range(n):
            v = words[i]
            vwl = v[0] in vl and v[-1] in vl
            ps[i + 1] = ps[i] + vwl
        
        ans = []
        for l, r in queries:
            ans.append(ps[r + 1] - ps[l])

        return ans