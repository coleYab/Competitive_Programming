# Problem: D - Lakes in Bahirdar - https://codeforces.com/gym/602812/problem/D

import sys
import threading
from math import ceil, log2, log10, remainder
from bisect import bisect_left as bl, bisect_right as br
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations

INF = float('inf')
MOD = 10 ** 9 + 7

MOVES = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solve():
    n, m, k = map(int, input().split())
    board = [list(input()) for i in range(n)]

    inbound = lambda i, j: 0 <= i < n and 0<= j < m

    visited = [[0] * m for _ in range(n)]
    def dfs(i, j):
        stack = [(i, j)]
        is_border = False

        cnt = 0
        while stack:
            curi, curj = stack.pop()
            if (not inbound(curi, curj) or visited[curi][curj]):
                continue
                
            if board[curi][curj] == '*':
                continue
        
            visited[curi][curj] = True
            cnt += 1
            for dx, dy in MOVES:
                nxti, nxtj = curi + dx, curj + dy
                is_border = is_border or (not inbound(nxti, nxtj))
                stack.append((nxti, nxtj))
            
        return cnt if not is_border else 0

    ans = {}
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and board[i][j] == '.':
                cur = dfs(i, j) 
                if cur > 0:
                    ans[(i, j)] = cur


    lakes = sorted(ans.items(), key=lambda a: -a[1])

    def fill(i, j):
        stack = [(i, j)]
        is_border = False

        cnt = 0
        while stack:
            curi, curj = stack.pop()
            if (not inbound(curi, curj)):
                continue
                
            if board[curi][curj] == '*':
                continue
        
            board[curi][curj] = '*'
            cnt += 1
            for dx, dy in MOVES:
                nxti, nxtj = curi + dx, curj + dy
                is_border = is_border or (not inbound(nxti, nxtj))
                stack.append((nxti, nxtj))
   

    kk = len(lakes)
    ans = 0
    for i in range(kk):
        if len(lakes) == k:
            break
        (ttt, j), cnt = lakes.pop()
        fill(ttt, j)
        ans += cnt


    print(ans)
    for ln in board:
        print(*ln, sep="")

def main():
    t = 1
    # t = int(input())
    for i in range(t):
        solve()


if __name__ == '__main__':
    main()

    # for recursive uncomment it below
    # sys.setrecursionlimit(1 << 30)
    # threading.stack_size(1 << 27)

    # main_thread = threading.Thread(target=main)
    # main_thread.start()
    # main_thread.join()