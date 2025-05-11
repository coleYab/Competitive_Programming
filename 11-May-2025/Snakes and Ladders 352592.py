# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board):
        def transform(idx):
            i = idx//len(board)
            j = idx%len(board)
            if i % 2:
                return board[-(i+1)][-(j+1)]
            else:
                return board[-(i+1)][j]

        n = len(board)
        que = deque()
        visited= [-1 for _ in range(n*n)]
        que.append(0)
        visited[0]= 0
        while que:
            node = que.popleft()
            for i in range(1, 7):
              if node + i < n*n:
                t = transform(node+i)
                if t != -1:
                  if visited[t-1]==-1:
                    visited[t-1]= visited[node]+1
                    que.append(t-1)
                else:
                  if visited[node+i]==-1:
                   visited[node+i]= visited[node]+1
                   que.append(node+i)
        return visited[-1]