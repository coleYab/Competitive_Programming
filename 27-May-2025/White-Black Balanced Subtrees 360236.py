# Problem: White-Black Balanced Subtrees - https://codeforces.com/contest/1676/problem/G

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
    s = input()
    mp = 'WB'
    count = [[0, 0] for i in range(n)]

    adj = defaultdict(list)
    inb = [0] * n
    for i,v in enumerate(a):
        adj[i + 1].append(v - 1)
        inb[v - 1] += 1

    que = deque()
    for i, v in enumerate(inb):
        if v == 0:
            que.append(i)
    
    while que:
        top = que.popleft()
        count[top][mp.index(s[top])] += 1
        for ch in adj[top]:
            count[ch][1] += count[top][1]
            count[ch][0] += count[top][0]
            inb[ch] -= 1
            if inb[ch] == 0:
                que.append(ch)       

    ans = 0
    for u, v in count:
        ans += int(u == v)
    
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
