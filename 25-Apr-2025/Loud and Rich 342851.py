# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        adj = defaultdict(list)
        ans = [(quiet[i], i) for i in range(len(quiet))]
        inb = [0] * len(quiet)
        n = len(quiet)

        for u, v in richer:
            adj[u].append(v)
            inb[v] += 1

        que = deque()
        for i, v in enumerate(inb):
            if v == 0:
                que.append(i)

        vis = set()
        while que:
            cur = que.popleft()
            vis.add(cur)
            for ch in adj[cur]:
                if ans[cur] < ans[ch]:
                    ans[ch] = ans[cur]
                if ch not in vis:
                    inb[ch] -= 1
                    if inb[ch] == 0:
                        que.append(ch)

        ans = [b for a,b in ans]
        return ans