# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class DSU:
    def __init__(self, cap):
        self.parent = [-1 for i in range(cap + 1)]
        self.min = [i for i in range(cap + 1)]

    def union(self, s1, s2):
        p1, p2 = self.find(s1), self.find(s2)
        if p1 == p2:
            return False

        self.parent[p1] += self.parent[p2]
        self.min[p1] = min(self.min[p2], self.min[p1])
        self.parent[p2] = p1
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
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        dsu = DSU(n * m)
        def transform(i, j):
            return i * m + j
    
        for i in range(n):
            for j in range(m):
                if i < n - 1 and grid[i][j] in [2, 3, 4] and grid[i + 1][j] in [2, 5, 6]:
                    dsu.union(transform(i,j), transform(i + 1, j))
                if j < m - 1 and grid[i][j] in [1, 4, 6] and grid[i][j + 1] in [3, 5, 1]:
                    dsu.union(transform(i,j), transform(i, j + 1))

        return dsu.find(0) == dsu.find(n * m - 1)
