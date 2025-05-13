# Problem: People are leaving - https://codeforces.com/edu/course/2/lesson/7/2/practice/contest/289391/problem/A

import sys, threading
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
    def __init__(self, cap):
        self.parent = [-1 for i in range(cap + 1)]
        self.count = cap 

    def union(self, s1, s2):
        p1 = self.find(s1)
        p2 = self.find(s2)

        if p1 == p2:
            return False

        tot = self.parent[p1] + self.parent[p2]
        self.parent[p2] += self.parent[p1]
        self.parent[p1] = p2
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
    n, m = map(int, input().split())
    dsu = DSU(n + 1)
    for i in range(m):
        u,v = map(str, input().split())
        v = int(v)
        if u == "?":
            ans = dsu.find(v)
            print(ans if ans <= n else -1)
            continue

        dsu.union(v, v + 1)

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
