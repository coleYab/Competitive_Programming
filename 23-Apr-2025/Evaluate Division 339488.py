# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], qs: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for idx, [u, v] in enumerate(equations):
            graph[u].append((v, values[idx]))
            graph[v].append((u, 1 / values[idx]))

        vis = set()
        def dfs(node, end, path):
            if len(graph[node]) == 0:
                return False
            if node == end:
                path.append(1)
                return True

            if node in vis:
                return False
            
            vis.add(node)
            for ch, den in graph[node]:
                path.append(den)
                if dfs(ch, end, path):
                    return True
                path.pop()

            return False

        ans = []
        for u, v in qs:
            vis = set()
            path = []

            r= dfs(u, v, path)
            print(u, v, path)
            if r:
                top = path[0]
                for i in range(1, len(path)):
                    top *= path[i]
                ans.append(top)
            else:
                ans.append(-1)
        return ans