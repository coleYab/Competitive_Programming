# Problem: Similar String Groups - https://leetcode.com/problems/similar-string-groups/

class DSU:
    def __init__(self, cap):
        self.parent = [-1 for i in range(cap + 1)]
        self.edges = [0 for i in range(cap + 1)]
        self.comp = cap + 1

    def union(self, s1, s2):
        p1, p2 = self.find(s1), self.find(s2)
        if p1 == p2:
            self.edges[p1] += 1
            return 

        self.comp -= 1
        self.edges[p2] += self.edges[p1] + 1
        self.parent[p2] += self.parent[p1]
        self.parent[p1] = p2

    def find(self, node):
        vis = []
        while self.parent[node] >= 0:
            vis.append(node)
            node = self.parent[node]

        for ch in vis:
            self.parent[ch] = node
        return node

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        dsu = DSU(len(strs) - 1)

        def comp(s1, s2):
            cnt = 0
            for a,b in zip(s1, s2):
                cnt += int(a != b)

            return cnt <= 2

        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if comp(strs[i], strs[j]):
                    dsu.union(i, j)

        return dsu.comp