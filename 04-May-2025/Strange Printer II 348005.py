# Problem: Strange Printer II - https://leetcode.com/problems/strange-printer-ii/

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        _mx = max(map(max, targetGrid))
        start = [[float("inf"), float("inf")] for i in range(_mx)]
        end = [[float("-inf"), float("-inf")] for i in range(_mx)]
        n = len(targetGrid)
        m = len(targetGrid[0])

        for i in range(n):
            for j in range(m):
                idx = targetGrid[i][j]
                start[idx - 1][0] = min(start[idx - 1][0], i)
                start[idx - 1][1] = min(start[idx - 1][1], j)
                end[idx - 1][0] = max(end[idx - 1][0], i)
                end[idx - 1][1] = max(end[idx - 1][1], j)
    
        adj = defaultdict(set)
        inb = [0 for i in range(_mx)]

        def overlaps(i, j):
            if end[i][0] < start[j][0] or end[j][0] < start[i][0]:
                return False
            if end[i][1] < start[j][1] or end[j][1] < start[i][0]:
                return False 

            return True

        def get_intersection(i, j):
            p1 = [max(start[i][0], start[j][0]), max(start[i][1], start[j][1])]
            p2 = [min(end[i][0], end[j][0]), min(end[i][1], end[j][1])]
            return p1, p2

        def hascolor(i, j, color):
            p1, p2 = get_intersection(i, j)

            for i in range(p1[0], p2[0] + 1):
                for j in range(p1[1], p2[1] + 1):
                    if targetGrid[i][j] == color:
                        return True       

            return False

        for i in range(_mx):
            if start[i][0] == float("inf"):
                continue
            for j in range(i + 1, _mx):
                if not overlaps(i, j):
                    continue
                if hascolor(i, j, i + 1):
                    adj[i].add(j)
                    inb[j] += 1
                if hascolor(i, j, j + 1):
                    adj[j].add(i)
                    inb[i] += 1
        
        cnt = 0
        que = deque()
        for i in range(_mx):
            if start[i][0] == float("inf"):
                cnt += 1
                continue
        
            if inb[i] == 0:
                que.append(i)
        path = []
        while que:
            top = que.popleft()
            path.append(top)
            cnt += 1
            for ch in adj[top]:
                inb[ch] -= 1
                if inb[ch] == 0:
                    que.append(ch)

        return cnt == _mx