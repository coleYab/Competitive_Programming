# Problem: Remove Max Number of Edges to Keep Graph Fully Traversable - https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/


class DSU:
    """
    implement: dsu here and add all the varation needed
    """
    def __init__(self, cap):
        self.parent = [-1 for i in range(cap + 1)]
        self.count = cap 

    def union(self, s1, s2):
        p1 = self.find(s1)
        p2 = self.find(s2)

        if p1 == p2:
            return False

        tot = self.parent[p1] + self.parent[p2]
        if self.parent[p1] > self.parent[p2]:
            self.parent[p2] = tot 
            self.parent[p1] = p2
        else:
            self.parent[p2] = p1
            self.parent[p1] = tot

        self.count -= 1
        return True


    def find(self, node):
        vis = []
        while self.parent[node] >= 0:
            vis.append(node)
            node = self.parent[node]
        for ch in vis:
            self.parent[ch] = node
        return node

    def connected(self, s1, s2):
        return self.find(s1) == self.find(s2)




class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        common = []
        alice = []
        bob  = []
        dsua, dsub = DSU(n), DSU(n)

        for ty, u,v in edges:
            if ty == 3:
                common.append((u,v))
            elif ty == 1:
                alice.append((u,v))
            else:
                bob.append((u,v))

        ans = 0
        for u,v in common:
            dsua.union(u,v)
            if not dsub.union(u,v):
                ans += 1
        for u, v in alice:
            if not dsua.union(u,v):
                ans += 1
        for u,v in bob:
            if not dsub.union(u,v):
                ans += 1
        print(dsua.count, dsub.count, dsua.parent, dsub.parent)
        return ans if dsua.count == dsub.count and dsua.count == 1 else -1