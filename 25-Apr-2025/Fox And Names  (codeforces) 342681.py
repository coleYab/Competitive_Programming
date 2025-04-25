# Problem: Fox And Names  (codeforces) - https://codeforces.com/contest/510/problem/C

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

def solve():
    n = int(input())
    words = [input() for i in range(n)]
    letters = set([chr(i) for i in range(ord('a'), ord('z') + 1)])
    adj = defaultdict(set)

    inb = defaultdict(int)

    for i in range(n - 1):
        cur = words[i]
        next = words[i + 1]
        for i in range(max(len(cur), len(next))):
            if i >= len(cur):
                break

            if i >= len(next):
                return "Impossible"

            if cur[i] != next[i]:
                inb[next[i]] += int(next[i] not in adj[cur[i]])
                adj[cur[i]].add(next[i])
                break

    que = deque()
    for c in letters:
        if inb[c] == 0:
            que.append(c)

    vis = set()
    path = []
    while que:
        cur = que.popleft()
        if cur in vis:
            continue    

        path.append(cur)
        for ch in adj[cur]:
            inb[ch] -= 1
            if inb[ch] <= 0: que.append(ch)

    if len(path) != len(letters):
        return "Impossible"

    return "".join(path)


def main():
    t = 1
    for i in range(t):
        start_time = time.perf_counter()
        print(solve())
        # if solve():
        #     print("YES")
        # else:
        #     print("NO")
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        # print(f"Time taken for test case {i+1}: {execution_time:.6f} seconds")
  

if __name__ == "__main__":
    main()