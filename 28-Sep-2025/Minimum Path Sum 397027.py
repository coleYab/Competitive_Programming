# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        for i in range(n):
            for j in range(m):
                cur = float("inf")
                if i:
                    cur = min(grid[i - 1][j], cur)
                if j:
                    cur = min(grid[i][j - 1], cur)
                if cur == float("inf"):
                    cur = 0
                grid[i][j] += cur

        return grid[n - 1][m - 1]