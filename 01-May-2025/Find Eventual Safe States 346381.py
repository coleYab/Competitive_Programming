# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

from typing import *
from collections import *

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        n = len(graph)
        ans = set()

        vis = [0] * len(graph)
        safe = set()
        for u, v in enumerate(graph):
            if len(v) == 0:
                ans.add(u)
                safe.add(u)
            adj[u].extend(v)

        inb = [0] * len(graph)
        for i in range(n):
            for j in adj[i]:
                inb[j] += 1


        def dfs(node):
            if vis[node]:
                return node in safe

            vis[node] = True
            for ch in adj[node]:
                if not dfs(ch):
                    return False

            safe.add(node)
            return True

        for i in range(len(graph)):
            if dfs(i):
                ans.add(i)

        return sorted(ans)