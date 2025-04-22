# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])
        ans = 0
        que = deque()
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    que.append((i, j, 0))


        inbound = lambda i, j: 0 <= i < n and 0 <= j < m
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def bfs():
            nonlocal ans, fresh
            while que:
                i, j, lvl = que.popleft()
                if not inbound(i, j) or grid[i][j] == 0:
                    continue

                for dx, dy in moves:
                    que.append((i +dx, j + dy, lvl + 1))
                fresh -= int(grid[i][j] == 1)
                grid[i][j] = 0
                ans = max(ans, lvl)

        bfs()
        return ans if not fresh else -1



        