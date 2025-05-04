# Problem: Merge Sort - https://codeforces.com/problemset/problem/873/D

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
    n,m = map(int, input().split())
    a = list(range(1, n + 1))

    valid = [True]
    def divide(a):
        nonlocal m
        # nonlocal valid
        if m <= 0 or len(a) == 1:
            return a 

        if m == 1 and len(a) > 1:  
            return a

        mid = len(a) // 2
        # print(a[mid], a[mid - 1])
        a[mid - 1], a[mid] = a[mid], a[mid - 1]
        # print(a[mid], a[mid - 1])
        m -= 2
        left = divide(a[:mid])
        right = divide(a[mid:])
        return left + right

    m -= 1
    ans = divide(a)    
    if m > 0:
        print(-1)
        return

    print(*ans)

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
