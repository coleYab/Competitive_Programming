# Problem: Belted Rooms - https://codeforces.com/problemset/problem/1428/B

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

def solve():
    n = int(input())
    s = input()
    c = s.count('-')
    if len(set(s)) == 1 or (len(set(s)) == 2 and '-' in s):
        print(n)
        return

    cango = [False for i in range(n)]
    for i in range(n):
        cango[i] = s[i] == '-' or cango[i]
        cango[(i + 1) % n] = cango[(i + 1) % n] or s[i] == '-'

    ans = 0
    for i in cango:
        ans += int(i)

    print(ans)

def main():
    t = 1
    t = int(input())
    for i in range(t):
        solve()

if __name__ == "__main__":
    main()
