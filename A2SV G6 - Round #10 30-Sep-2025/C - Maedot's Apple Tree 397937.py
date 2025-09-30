# Problem: C - Maedot's Apple Tree - https://codeforces.com/gym/602812/problem/C

import sys
import threading
from math import ceil, log2, log10, remainder
from bisect import bisect_left as bl, bisect_right as br
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations

INF = float('inf')
MOD = 10 ** 9 + 7

def solve():
    n = int(input())

    g = [[] for _ in range(n)]
    
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)

    def dfs(v, p, g, cnt):
        if len(g[v]) == 1 and g[v][0] == p:
            cnt[v] = 1
        else:
            for u in g[v]:
                if u != p:
                    dfs(u, v, g, cnt)
                    cnt[v] += cnt[u]

    cnt = [0] * n
    dfs(0, -1, g, cnt)

    q = int(input())
    for _ in range(q):
        c, k = map(int, input().split())
        c -= 1
        k -= 1

        res = cnt[c] * cnt[k]
        print(res)

def main():
    t = int(input())
    for i in range(t):
        solve()

        # if solve():
        #     print("YES")
        # else:
        #     print("NO")

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()