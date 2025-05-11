# Problem: Construct Quad Tree - https://leetcode.com/problems/construct-quad-tree/description/

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def divide(start, end):
            same = True
            for i in range(start[0], end[0] + 1):
                for j in range(start[1], end[1] + 1):
                    same = same and grid[start[0]][start[1]] == grid[i][j]

            if start == end or same:
                return Node(grid[start[0]][start[1]], True, None, None, None, None)

            midx = (start[0] + end[0]) // 2
            midy = (start[1] + end[1]) // 2

            topLeft = divide(start, [midx, midy])
            bottomLeft = divide([start[0], midy + 1], [midx, end[1]])
            topRight = divide([midx + 1, start[1]], [end[0], midy])
            bottomRight = divide([midx + 1, midy + 1], end)


            return Node(1, False, topLeft, bottomLeft, topRight, bottomRight)

        return divide([0, 0], [len(grid) - 1, len(grid) - 1])

