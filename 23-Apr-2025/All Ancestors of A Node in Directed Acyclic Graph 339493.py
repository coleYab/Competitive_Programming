# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        inb = [0] * n
        for u,v in edges:
            adj[u].append(v)
            inb[v] += 1

        inb = list([v, i] for i, v in enumerate(inb))
        hm = {}
        for i, v in enumerate(inb):
            hm[v[1]] = v

        ans = [set() for i in range(n)]
        while inb:
            val, idx = inb[-1]
            if val != 0:
                inb.sort(reverse=True)

            val, idx = inb.pop()
            for ch in adj[idx]:
                hm[ch][0] -= 1            
                ans[ch].add(idx)
                for v in ans[idx]:
                    ans[ch].add(v)

        return [sorted(an) for an in ans]
