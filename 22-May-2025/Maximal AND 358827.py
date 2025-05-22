# Problem: Maximal AND - https://codeforces.com/problemset/problem/1669/H

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
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    ps = [0] * 31
    for i in range(31):
        for j in range(n):
            ps[i] += (a[j] >> i) & 1

    ans = 0
    # print(ps)
    for i in range(30, -1, -1):
        if n - ps[i] == 0:
            ans |= 1 << i 

        elif n - ps[i] <= m:
            ans |= 1 << i
            m -= n - ps[i]

    print(ans)



def main():
    t = 1
    t = int(input())
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