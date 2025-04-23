# Problem: Count Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        res = []
        vis = set()
        path = []

        adj = defaultdict(list)
        for k, v in edges:
            adj[k].append(v)
            adj[v].append(k)

        def dfs(node):
            if node in vis:
                return
            vis.add(node)
            path.append(node)
            for ch in adj[node]:
                dfs(ch)
            
        ans = 0
        for i in range(n):
            path = []
            if i not in vis:
                dfs(i)
                comp = True
                for i in range(len(path)):
                    for j in range(i + 1, len(path)):
                        if path[i] in adj and path[j] in adj[path[i]]:
                            pass
                        else:
                            comp = False
                    if not comp:
                        break

                ans += int(comp)

        return ans