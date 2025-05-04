# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        dp = [float("inf") for i in range(n)]
        inb = [0 for i in range(n)]
        for u, v in edges:
            adj[u].append(v)    
            adj[v].append(u)
            inb[u] += 1
            inb[v] += 1

        que = deque()
        for i in range(n):
            if inb[i] > 1:
                continue
            dp[i] = 0
            que.append(i)

        # print(inb)
        while que:
            top = que.popleft()
            for ch in adj[top]:
                inb[ch] -= 1
                if inb[ch] == 1:
                    dp[ch] = dp[top] + 1
                    que.append(ch)

        mx = max(dp)
        ans = []
        for i, v in enumerate(dp):
            if v == mx:
                ans.append(i)

        return ans