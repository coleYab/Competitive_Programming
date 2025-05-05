# Problem: Cutting a graph - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/D

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
        self.max_ans = 1
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

        self.max_ans = max(self.max_ans, -tot)
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
    n, m, q = map(int, input().split())
    qry = []
    cuts = set()
    edges = []
    for i in range(m):
        u,v = map(int, input().split())
        edges.append((u,v))

    for i in range(q):
        a,b,c = map(str, input().split())
        b = int(b)
        c = int(c)
        cuts.add((b,c))
        cuts.add((c,b))
        qry.append((a,b,c))

    dsu = DSU(n)
    for u,v in edges:
        if (u,v) not in cuts:
            dsu.union((u,v))
    qry = qry[::-1]
    ans = []
    for a,b,c in qry:
        if a == "cut":
            dsu.union(b,c)
        else:
            if dsu.connected(b,c):
                ans.append("YES")
            else:
                ans.append("NO")

    ans = ans[::-1]
    print(*ans, sep="\n")

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
