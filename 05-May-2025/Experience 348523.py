# Problem: Experience - https://codeforces.com/edu/course/2/lesson/7/1/practice/contest/289390/problem/C

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
        self.add = [0 for i in range(cap + 1)]
 
    def union(self, s1, s2):
        p1 = self.find(s1)
        p2 = self.find(s2)
 
        if p1 == p2:
            return
 
        tot = self.parent[p1] + self.parent[p2]
        if self.parent[p1] > self.parent[p2]:
            self.parent[p1] = p2
            self.parent[p2] = tot
            self.add[p1] -= self.add[p2]
        else:
            self.parent[p1] = tot 
            self.parent[p2] = p1 
            self.add[p2] -= self.add[p1]
 
    def add_score(self, s1, score):
        par = self.find(s1)
        self.add[par] += score
 
    def find(self, node):
        if self.parent[node] < 0:
            return node
        while self.parent[node] >= 0:
            node = self.parent[node]
        return node
 
    def find_score(self, node):
        ans = 0
        while self.parent[node] > 0:
            # print(node, self.parent[node])
            ans += self.add[node]
            node = self.parent[node]
        ans += self.add[node]
        return ans
 
 
def solve():
    n,m = map(int, input().split())
    dsu = DSU(n)
    for i in range(m):
        qry = input().split()
        if qry[0] == "join":
            u,v = map(int, qry[1:])
            dsu.union(u,v)
        elif qry[0] == "add":
            u,v = map(int, qry[1:])
            dsu.add_score(u,v)
        else:
            u = int(qry[1])
            print(dsu.find_score(u))
 
 
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