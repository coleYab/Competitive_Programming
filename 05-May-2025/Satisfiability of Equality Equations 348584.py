# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

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

        self.parent[p1] += self.parent[p2]
        self.parent[p2] = p1


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
    def equationsPossible(self, equations: List[str]) -> bool:
        n = 27
        equal = DSU(n)
        notequal = DSU(n)

        noteq = []
        for s in equations:
            a = ord(s[0]) - ord('a')
            b = ord(s[-1]) - ord('a')

            if a == b and s[1] == '!':
                return False

            if s[1] == '!':
                noteq.append((a,b))
            else:
                equal.union(a,b)

        for a,b in noteq:
            if equal.connected(a,b):
                return False

        return True
