# Problem: E - Simple Cycle With Minimal Lightest Edge - https://codeforces.com/gym/607625/problem/E

"""
 * Author: Yeabsira Moges(nba_yeabsira)
"""
import sys, threading
import time
from math import ceil, log2, log10, remainder
from bisect import bisect_left as bl, bisect_right as br
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations
from typing import * # for lode


INF = float('inf')
MOD = 10 ** 9 + 7


class DSU:
    """
    implement: dsu here and add all the varation needed
    """
    def __init__(self, cap):
        self.parent = [-1 for i in range(cap + 1)]
        self.bad = []
        self.count = cap

    def union(self, s1, s2, c):
        p1 = self.find(s1)
        p2 = self.find(s2)

        if p1 == p2:
            self.bad = (s1, s2, c)
            # print(self.bad)
            return False

        tot = self.parent[p1] + self.parent[p2]
        if self.parent[p1] >= self.parent[p2]:
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



def solve():
    n,m = map(int, input().split())
    adj = defaultdict(set)
    dsu = DSU(n)
    edges = []
    for i in range(m):
        u,v,c = map(int, input().split())
        if u == v:
            continue
        edges.append((c, u, v))

    edges.sort(reverse=True)
    for c, u, v in edges:
        if dsu.union(u,v,c):
            adj[u].add(v)
            adj[v].add(u)

    u,v,c = dsu.bad
    parent = [0 for i in range(n + 1)]
    vis = set()
    parent[u] = -1
    def dfs(start, end):
        stack = [start]
        while stack:
            top = stack.pop()
            if top == end:
                break
            if top in vis:
                continue
            vis.add(top)
            for ch in adj[top]:
                if ch not in vis:
                    parent[ch] = top
                    stack.append(ch)            


    dfs(u,v)
    path = [v]
    end = parent[v]
    while end > 0:
        path.append(end)
        end = parent[end]

    print(c, len(path))
    print(*path)


def main():
    t = 1
    t = int(input())
    for i in range(t):
        solve()

if __name__ == "__main__":
    main()