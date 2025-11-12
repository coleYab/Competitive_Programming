# Problem: Make Sum Divisible by P - https://leetcode.com/problems/make-sum-divisible-by-p/

class Solution:
    def minSubarray(self, a: List[int], p: int) -> int:
        tot = sum(a)
        rem = tot % p
        hm = {0: -1}
        ans = float("inf")
        cur = 0
        if tot % p == 0:
            return 0
    
        for i, v in enumerate(a):
            cur += v
            cur %= p
            req = ((cur - rem) % p) + p
            req %= p
            if req in hm:
                ans = min(ans, i - hm[req])
            hm[cur
            ] = i

        if ans == len(a):
            return -1
    
        return ans if ans != float("inf") else -1 