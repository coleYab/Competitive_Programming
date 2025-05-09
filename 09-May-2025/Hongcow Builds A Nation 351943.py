# Problem: Hongcow Builds A Nation - https://codeforces.com/contest/744/problem/A

"""
 * Author: Yeabsira Moges(nba_yeabsira)
"""
import sys
import time
from math import ceil, log2, log10, remainder
from bisect import bisect_left as bl, bisect_right as br
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations
from typing import * # for leetcode 


INF = float('inf')
MOD = 10 ** 9 + 7


class DSU:
    """
    implement: dsu here and add all the varation needed
    """
    def __init__(self, cap):
        self.parent = [-1 for i in range(cap + 1)]
        self.edges = [0 for i in range(cap + 1)]

    def union(self, s1, s2, w = 1):
        p1, p2 = self.find(s1), self.find(s2)
        if p1 == p2:
            self.edges[p1] += w
            return 

        self.edges[p2] += self.edges[p1] + w
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


def solve():
    n,m,k = map(int, input().split())
    dsu = DSU(n)
    a = list(map(int, input().split()))
    es = []
    for i in range(m):
        u,v = map(int, input().split())
        es.append((u,v))
        dsu.union(u,v)

    nval = set()
    for i in a:
        nval.add(dsu.find(i))

    mpar = None
    msz = float("-inf")
    pars = set()
    aa = set()
    for c in a:
        aa.add(dsu.find(c))
    a = aa   

    for i in range(1, n + 1):
        if dsu.parent[i] < 0:
            if i not in a:
                pars.add(i) 
        if dsu.parent[i] < 0 and msz < -dsu.parent[i] and dsu.find(i) in nval:
            msz = -dsu.parent[i]
            mpar = i 

    # print(pars)
    pars = list(pars)
    for i in range(len(pars) - 1):
        dsu.union(pars[i], pars[i + 1], 0)
    if pars:
        dsu.union(mpar, pars[0], 0)
    
    ans = 0
    for i in range(1, n + 1):
        if dsu.parent[i] < 0:
            sz = -dsu.parent[i]
            ans += ((sz * (sz - 1)) // 2) - dsu.edges[i]

    # print(dsu.parent)
    print(ans)


def main():
    t = 1
    # t = int(input())
    for i in range(t):
        start_time = time.perf_counter()

        solve()
        # if solve():
        #     print("YES")
        # else:
        #     print("NO")

        end_time = time.perf_counter()
        execution_time = end_time - start_time
        # print(f"Time taken for test case {i+1}: {execution_time:.6f} seconds")
  

if __name__ == "__main__":
    main()

    # recursive things
    # sys.setrecursionlimit(1 << 30)
    # threading.stack_size(1 << 27)
    # main_thread = threading.Thread(target=main)
    # main_thread.start()
    # main_thread.join()
