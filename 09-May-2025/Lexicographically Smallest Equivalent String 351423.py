# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class DSU:
    """
    implement: dsu here and add all the varation needed
    """
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
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dsu = DSU(26)
        for i in range(len(s1)):
            dsu.union(ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a'))

        ans = []
        for i in range(len(baseStr)):
            p = dsu.find(ord(baseStr[i]) - ord('a')) 
            ans.append(chr(ord('a') + dsu.min[p]))

        return "".join(ans)


