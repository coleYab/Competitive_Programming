# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        heap = []
        adj = defaultdict(list)
        for ed, w in zip(edges, succProb):
            adj[ed[0]].append((ed[1], w))
            adj[ed[1]].append((ed[0], w))
        
        dist = [0 for i in range(n)]
        dist[start] = -1
        heappush(heap, (-1, start))
        while heap:
            prb, node = heappop(heap)
            for ch, w in adj[node]:
                cprb  = prb * w
                if cprb < dist[ch]:
                    dist[ch] = cprb
                    heappush(heap, (cprb, ch))
        return -dist[end]
