# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class DSU:
    """
    implement: dsu here and add all the varation needed
    """
    def __init__(self, cap):
        self.parent = [-1 for i in range(cap + 1)]

    def union(self, s1, s2):
        p1, p2 = self.find(s1), self.find(s2)
        if p1 == p2:
            return False    
        self.parent[p2] += self.parent[p1]
        self.parent[p1] = p2
        return True

    def find(self, node):
        vis = []
        while self.parent[node] >= 0:
            vis.append(node)
            node = self.parent[node]
        for ch in vis:
            self.parent[ch] = node
        return node

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        def dist(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        for i in range(n):
            for j in range(i + 1, n):
                w = dist(i, j)
                edges.append((w, i, j))

        dsu = DSU(n + 1)
        edges.sort()
        ans = 0
        for w, u, v in edges:
            if dsu.union(u, v):
                ans += w

        return ans