# Problem: Freedom Trail - https://leetcode.com/problems/freedom-trail/

from functools import lru_cache

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ans = float("inf")
        def cost_of(key, prev):
            mn = min(key, prev)
            mx = max(key, prev)
            return min(mx - mn, mn + (len(ring) - mx)) 

        adj = defaultdict(list)
        lettermp = defaultdict(list)
        for i, let in enumerate(ring):
            lettermp[let].append(i)
        for i in lettermp:
            lettermp[i] = tuple(lettermp[i])

        for l in lettermp[key[0]]:
            adj[(0, -1)].append((l, 0))

        for i in range(len(key) - 1):
            next = i + 1
            next_list = []
            for l in lettermp[key[next]]:
                next_list.append((l, next))
            for cur in lettermp[key[i]]:
                adj[(cur, i)].extend(next_list)


        # print(adj)
        vis = set()
        @lru_cache()
        def dfs(node, level):
            if level == len(key) - 1:
                return 0

            ans = float("inf")
            for nch, nlevel in adj[(node, level)]:
                cost = cost_of(nch, node)
                ans = min(ans, dfs(nch, nlevel) + cost)

            return ans + 1

        ans = dfs(0, -1)
        return ans