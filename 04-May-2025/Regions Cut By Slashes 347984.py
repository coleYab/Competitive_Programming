# Problem: Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/description/

"""
I really love dsu
"""
class DSU:
    def __init__(self, cap):
        self.parent = [-1 for i in range(cap + 1)]
        self.components = cap

    def union(self, s1, s2):
        p1 = self.find(s1)
        p2 = self.find(s2)

        if p1 == p2:
            return

        tot = self.parent[p1] + self.parent[p2]
        self.parent[p2] = p1
        self.parent[p1] = tot
        self.components -= 1
    def find(self, node):
        vis = []
        while self.parent[node] >= 0:
            vis.append(node)
            node = self.parent[node]
        for ch in vis:
            self.parent[ch] = node
        return node


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        mapping = ['N', 'E', 'S', 'W']
        opp = {'N' : 'S', 'S' : 'N', 'E': 'W', 'W' : 'E' }
        n = len(grid)
        dsu = DSU(n * n * 4) 

        def transform(i, j, dir, n):
            idx = mapping.index(dir)    
            posn = i * n + j
            return posn * 4 + idx 

        def inbound(i, j):
            return 0 <= i < n and 0 <= j < n

        moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for i in range(n):
            for j in range(n):
                for idx, (dx, dy) in enumerate(moves):
                    if inbound(i + dx, j + dy):
                        dir = mapping[idx]
                        ni = transform(i, j, dir, n)
                        nj = transform(i + dx, j + dy, opp[dir], n)
                        dsu.union(ni, nj)

                if grid[i][j] != '\\':
                    ni = transform(i, j, 'N', n)
                    nj = transform(i, j, 'W', n)
                    dsu.union(ni, nj)
                    ni = transform(i, j, 'S', n)
                    nj = transform(i, j, 'E', n)
                    dsu.union(ni, nj)

                if grid[i][j] != '/':
                    ni = transform(i, j, 'N', n)
                    nj = transform(i, j, 'E', n)
                    dsu.union(ni, nj)
                    ni = transform(i, j, 'S', n)
                    nj = transform(i, j, 'W', n)
                    dsu.union(ni, nj)

        return dsu.components