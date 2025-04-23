# Problem: Course Schedule II - https://leetcode.com/problems/course-schedule-ii/description/

class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        inb = [0] * n

        for u, v in prerequisites:
            adj[v].append(u)
            inb[u] += 1

        path = []

        vis = set()
        cur = set()
        def dfs(node):
            if node in cur:
                return False
            if node in vis:
                return True

            path.append(node)
            vis.add(node)
            cur.add(node)
            for ch in adj[node]:
                inb[ch] -= 1
                if inb[ch] <= 0:
                    if not dfs(ch):
                        return False

            return True
    
        for i in range(n):
            if i not in vis and inb[i] == 0:
                dfs(i)

        for v in inb:
            if v > 0:
                return []

        return path