# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        N = 26
        edges = []
        for i in range(len(original)):
            u = ord(original[i]) - ord('a')
            v = ord(changed[i]) - ord('a')
            w = cost[i]
            edges.append((u, v, w))
        
        INF = float('inf')
        min_cost = [[INF] * N for _ in range(N)]
        
        for start in range(N):
            dist = [INF] * N
            dist[start] = 0
            for _ in range(N - 1):
                for u, v, w in edges:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
            
            for end in range(N):
                min_cost[start][end] = dist[end]
        
        if len(source) != len(target):
            return -1 
        
        total = 0
        for s_ch, t_ch in zip(source, target):
            if s_ch == t_ch:
                continue
            
            s_idx = ord(s_ch) - ord('a')
            t_idx = ord(t_ch) - ord('a')
            cur_cost = min_cost[s_idx][t_idx]
            
            if cur_cost == INF:
                return -1
            total += cur_cost
        
        return total
