# Problem: Array Elimination - https://codeforces.com/contest/1601/problem/A

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
    a = list(map(int, input().split()))

    if len(set(a)) == 1 and a[0] == 0:
        print(*list(range(1, n + 1)))
        return

    cnt = [0 for i in range(100)]
    for num in a:
        for i in range(100):
            cnt[i] += (num >> i) & 1 

    ans = [1]
    for i in range(2, n + 1):
        valid = True
        for j in cnt:
            if j % i != 0:
                valid = False
                break

        if valid:
            ans.append(i)

    print(*ans)

def main(): 
    t = 1
    t = int(input())
    for i in range(t):
        solve()

if __name__ == "__main__":
    main()

