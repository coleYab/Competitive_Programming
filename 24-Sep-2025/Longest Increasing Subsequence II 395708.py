# Problem: Longest Increasing Subsequence II - https://leetcode.com/problems/longest-increasing-subsequence-ii/description/

class seg_tree:
    def __init__(self, size):
        self.size = 1
        while self.size < size: 
            self.size *= 2
        self.tree = [0] * (self.size * 2)

    def _set(self, idx, val, x, lx, rx):
        if rx - lx == 1:
            self.tree[x] = max(self.tree[x], val)
            return
        
        m = (lx + rx) // 2
        if idx < m:
            self._set(idx, val, 2 * x + 1, lx, m)
        else:
            self._set(idx, val, 2 * x + 2, m, rx)
        
        self.tree[x] = max(self.tree[2 * x + 1], self.tree[2 * x + 2])

    def set(self, idx, val):
        self._set(idx, val, 0, 0, self.size)

    def _get(self, l, r, x, lx, rx):
        if lx >= r or l >= rx: return 0
        if l <= lx and rx <= r: return self.tree[x]
        m = (lx + rx) // 2
        return max(self._get(l, r, 2 * x + 1, lx, m), self._get(l, r, 2 * x + 2, m, rx))

    def get(self, left, right):
        return self._get(left, right, 0, 0, self.size)

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        ans = 0
        st = seg_tree(max(nums) + 2)
        for num in nums:
            cur = st.get(num - k, num) + 1
            ans = max(cur, ans)
            st.set(num, cur)
            # print(sttree)

        return ans