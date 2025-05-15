# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ps = [arr[0]]

        for i in range(1, len(arr)):
            ps.append(ps[-1] ^ arr[i])
        
        ans = []
        for u,v in queries:
            cur = ps[v]
            if u > 0:
                cur ^= ps[u - 1]
            ans.append(cur)

        return ans
