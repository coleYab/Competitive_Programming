# Problem: Spanning Tree - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/E

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
        self.weight = 0
        self.parent = [-1 for i in range(cap + 1)]

    def union(self, s1, s2, weight):
        p1 = self.find(s1)
        p2 = self.find(s2)

        if p1 == p2:
            return

        self.parent[p2] += self.parent[p1]
        self.parent[p1] = p2
        self.weight += weight


    def find(self, node):
        vis = []
        while self.parent[node] >= 0:
            vis.append(node)
            node = self.parent[node]
        for ch in vis:
            self.parent[ch] = node
        return node



def solve():
    n,m = map(int, input().split())
    edges = []
    for i in range(m):
        u,v,w = map(int, input().split())
        edges.append((w,u,v))
    edges.sort()
    dsu  = DSU(n)
    for w,u,v in edges:
        dsu.union(u, v, w)

    print(dsu.weight)


def main():
    t = 1
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
