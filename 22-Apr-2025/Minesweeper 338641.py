# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click   
        n, m = len(board), len(board[0])
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board

        # now do you magic nigga
        unreveled = set()
        vis = set()
        moves = [(1, 0), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1), (-1, 0), (0, -1)]
        inbound = lambda a, b: 0 <= a < n and 0 <= b < m
        
        def count_bomb(i, j):
            cnt = 0
            for dx, dy in moves:
                ni = dx + i
                nj = dy + j 
                if inbound(ni, nj) and board[ni][nj] == 'M':
                    cnt += 1
            return cnt

        def bfs(i, j):
            que = deque()
            que.append((i, j))
            
            while que:
                curi, curj = que.popleft()
                if not inbound(curi, curj) or (curi, curj) in vis:
                    continue

                vis.add((curi, curj))
                cnt = count_bomb(curi, curj)
                if cnt != 0:
                    board[curi][curj] = str(cnt)
                    continue

                if board[curi][curj] == 'E':
                    board[curi][curj] = 'B'

                for dx, dy in moves:
                    que.append((curi + dx, curj + dy))

        bfs(x, y)
        return board
