# Problem: The Unique Topological Sort - https://basecamp.eolymp.com/en/problems/10652

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
    n,m = map(int, input().split())
    adj = defaultdict(list)
    inb = [0 for i in range(n + 1)]
    for i in range(m):
        u,v = map(int, input().split())
        adj[u].append(v)
        inb[v] += 1 
    cnt = 0
    que = deque()
    for i in range(1, n):
        if inb[i] == 0:
            que.append(i)

    if len(que) > 1:
        return False

    while que:
        top = que.popleft()
        cnt += 1
        curcnt = 0
        for ch in adj[top]:
            inb[ch] -= 1 
            if inb[ch] == 0:
                que.append(ch)
                curcnt += 1 

        if curcnt > 1:
            return False

    return cnt == n
def main():
    t = 1
    # t = int(input())
    for i in range(t):
        start_time = time.perf_counter()

        # solve()
        if solve():
            print("YES")
        else:
            print("NO")

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
