# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf") for i in range(n)]
        adj = defaultdict(list)

        for u, v, w in times:
            u -= 1
            v -= 1
            adj[u].append((v, w))
            # adj[v].append((u, w))

        heap = []
        heappush(heap, (0, k - 1))
        dist[k - 1] = 0

        while heap:
            u = heappop(heap)[1]

            for ch in adj[u]:
                v, w = ch[0], ch[1]
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    # par[v] = u
                    heappush(heap, (dist[v], v))
        
        return max(dist) if max(dist) != float("inf") else -1