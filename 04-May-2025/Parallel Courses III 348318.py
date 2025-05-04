# Problem: Parallel Courses III - https://leetcode.com/problems/parallel-courses-iii/

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = defaultdict(list)
        dp = [0 for i in range(n)]
        free = 0

        inb = [0 for i in range(n)]
        oub = [0 for i in range(n)]
        for u, v in relations:
            u -= 1
            v -= 1
            adj[u].append(v)
            inb[v] += 1
            oub[u] += 1

        que = deque()
        for i in range(n):
            if inb[i] == 0 and oub[i] == 0:
                free = max(free, time[i])
                continue

            if inb[i] == 0:
                dp[i] = time[i]
                que.append(i)

        while que:
            top = que.popleft()
            for ch in adj[top]:
                inb[ch] -= 1
                dp[ch] = max(dp[top], dp[ch])
                if inb[ch] == 0:
                    dp[ch] += time[ch]
                    que.append(ch)

        return max(max(dp), free)