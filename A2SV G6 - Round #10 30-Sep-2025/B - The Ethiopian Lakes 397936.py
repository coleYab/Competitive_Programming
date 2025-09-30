# Problem: B - The Ethiopian Lakes - https://codeforces.com/gym/602812/problem/B

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
    n,m = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(n)]

    ans = 0

    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    inbound = lambda i, j: 0<= i < n and 0 <= j < m

    def dfs(i, j):
        if not (inbound(i,j) and board[i][j]):
            return 0
        ans = board[i][j]
        board[i][j] = 0
        for dx, dy in moves:
            ans += dfs(i + dx, j + dy)
        return ans

    for i in range(n):
        for j in range(m):
            if board[i][j]:
                cur = dfs(i, j)
                ans = max(cur, ans)

    print(ans)

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