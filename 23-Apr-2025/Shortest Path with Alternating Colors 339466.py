# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        badj = defaultdict(list)
        radj = defaultdict(list)

        for u,v in redEdges:
            radj[u].append(v)
        for u,v in blueEdges:
            badj[u].append(v)

        dis = [-1 for i in range(n)]

        vis = set()
        def bfs(node, col):
            que = deque()
            que.append((node, 0, col))
            while que:
                cur_node, cur_len, cur_col = que.popleft()
                if (cur_node, cur_col) in vis:
                    continue

                childs = badj[cur_node]
                vis.add((cur_node, cur_col))
                dis[cur_node] = cur_len if dis[cur_node] == -1 else min(cur_len, dis[cur_node])
                if cur_col == 1:
                    childs = radj[cur_node]
                
                for ch in childs:
                    que.append((ch, cur_len + 1, cur_col ^ 1))


        bfs(0, 0)
        vis=set()
        bfs(0, 1)
        return dis