# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        moves = [(1,0), (0, 1), (-1, 0), (0, -1)]
        n = len(matrix)
        m = len(matrix[0])
    
        inb = [[0 for i in range(m)] for i in range(n)]
        dp = [[0 for i in range(m)] for i in range(n)]

        def inbound(i, j):
            return 0 <= i < n and 0 <= j < m

        for i in range(n):
            for j in range(m):
                for dx, dy in moves:
                    ni, nj = dx + i, dy + j
                    if inbound(ni, nj):
                        inb[i][j] += int(matrix[i][j] > matrix[ni][nj])

        que = deque()
        for i in range(n):
            for j in range(m):
                if inb[i][j] == 0:
                    dp[i][j] = 1
                    que.append((i, j))

        ans = 0
        while que:
            i,j = que.popleft()
            for dx, dy in moves:
                ni, nj = dx + i, dy + j
                if inbound(ni, nj) and matrix[i][j] < matrix[ni][nj]:
                    inb[ni][nj] -= 1
                    dp[ni][nj] = max(dp[ni][nj], dp[i][j] + 1)
                    if inb[ni][nj] == 0:
                        que.append((ni, nj))
        
        for row in dp:
            ans = max(ans, max(row))
        
        return ans