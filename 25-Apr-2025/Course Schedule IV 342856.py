# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, n: int, pre: List[List[int]], qs: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        dp = defaultdict(set)
        inb = [0] * n
        for u, v in pre:
            adj[u].append(v)
            inb[v] += 1

        que = deque()
        for i in range(n):
            if inb[i] == 0:
                que.append(i)

        vis = set()
        while que:
            cur = que.popleft()
            if cur in vis:
                continue
            vis.add(cur)
            for ch in adj[cur]:
                dp[ch] = dp[ch].union(dp[cur])
                dp[ch].add(cur)
                inb[ch] -= 1
                if inb[ch] == 0:
                    que.append(ch)

        ans = []
        for q, p in qs:
            ans.append(p in dp and q in dp[p])
        return ans

