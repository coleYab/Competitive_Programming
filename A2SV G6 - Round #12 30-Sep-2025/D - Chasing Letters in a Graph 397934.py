# Problem: D - Chasing Letters in a Graph - https://codeforces.com/gym/606404/problem/D

import sys
from collections import deque

def solve():
    n, m = map(int, input().split())
    s = input()
    
    adj = [[] for _ in range(n)]
    indeg = [0] * n
    
    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        indeg[v] += 1
    
    dp = [[0] * 26 for _ in range(n)]
    q = deque()
    
    for i in range(n):
        if indeg[i] == 0:
            q.append(i)
    
    cnt = 0
    while q:
        u = q.popleft()
        cnt += 1
        c = ord(s[u]) - ord('a')
        dp[u][c] += 1
        for v in adj[u]:
            for j in range(26):
                dp[v][j] = max(dp[v][j], dp[u][j])
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    
    if cnt != n:
        print(-1)
    else:
        ans = max(max(row) for row in dp)
        print(ans)

def main():
    t = 1
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()