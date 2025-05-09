# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        que = deque()
        n = len(isWater)
        m = len(isWater[0])
        for i in range(n):
            for j in range(m):
                if isWater[i][j]:
                    que.append((i, j, 0))

        ans = [[-1 for i in range(m)] for j in range(n)]
        moves = [(0, 1), (1,0), (0, -1), (-1, 0)]
        def inbound(i, j):
            return 0 <= i < n and 0 <= j < m
        
        while que:
            i,j,t = que.popleft()
            if ans[i][j] != -1:
                continue

            ans[i][j] = t
            for dx, dy in moves:
                ni, nj = i + dx, j + dy
                if inbound(ni, nj) and ans[ni][nj] == -1:
                    que.append((ni, nj, t + 1))

        return ans 