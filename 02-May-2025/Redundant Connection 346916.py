# Problem: Redundant Connection - https://leetcode.com/problems/redundant-connection/


class DSU:
    """
    implement: dsu here and add all the varation needed
    """
    def __init__(self, cap):
        self.parent = [-1 for i in range(cap + 1)]

    def union(self, s1, s2):
        p1 = self.find(s1)
        p2 = self.find(s2)

        if p1 == p2:
            return

        tot = self.parent[p1] + self.parent[p2]
        if self.parent[p1] > self.parent[p2]:
            self.parent[p2] = tot 
            self.parent[p1] = p2
        else:
            self.parent[p1] = tot 
            self.parent[p2] = p1

    def find(self, node):
        vis = []
        while self.parent[node] > 0:
            vis.append(node)
            node = self.parent[node]
        for ch in vis:
            self.parent[ch] = node

        return node

    def connected(self, s1, s2):
        return self.find(s1) == self.find(s2)


class Solution:
    def findRedundantConnection(self, e: List[List[int]]) -> List[int]:
        n = len(e)
        dsu = DSU(n)
        for u,k in e:
            if dsu.connected(u,k):
                return u, k
            dsu.union(u,k)
        