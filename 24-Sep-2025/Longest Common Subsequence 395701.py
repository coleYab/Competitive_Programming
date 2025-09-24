# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

dp = {}
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str, l=0,r=0) -> int:
        if l == 0 and r == 0:
            global dp
            dp = {}
        if len(text1) <= l or r >= len(text2):
            return 0
        if (l, r) in dp: return dp[(l, r)]
        ans = 0
        if text1[l] == text2[r]:
            ans = 1 + self.longestCommonSubsequence(text1, text2, l+1,r+1)
        else:
            ans = max(self.longestCommonSubsequence(text1, text2, l,r+1), self.longestCommonSubsequence(text1, text2, l+1,r))


        # print(dp)

        dp[(l, r)] = ans
        return ans

