# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

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

    ss = [False for i in range(n)]
    for i in range(n):
        ss[i] = s[i] == '-' or ss[i]
        ss[(i + 1) % n] = ss[(i + 1) % n] or s[i] == '-'

    # print(ss)
    ans = 0
    for i in ss:
        ans += int(i)
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
