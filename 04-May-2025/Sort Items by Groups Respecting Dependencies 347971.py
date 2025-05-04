# Problem: Sort Items by Groups Respecting Dependencies - https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # print(group)
        lg = max(group) + 1
        for i in range(n):
            if group[i] == -1:
                group[i] = lg
                lg += 1

        gadj = defaultdict(set)
        grouping = [defaultdict(set) for i in range(lg)]
        gitems = [[] for i in range(n)]

        for i in range(n):  
            itemgroup = group[i]
            gitems[itemgroup].append(i)
            for v in beforeItems[i]:
                if itemgroup != group[v]:
                    gadj[group[v]].add(itemgroup)
                    continue
                grouping[itemgroup][v].add(i)

        def topo(adj, items):
            inb = defaultdict(int)
            for u in adj:
                for ch in adj[u]:
                    inb[ch] += 1
            
            que = deque()
            for u in items:
                if inb[u] == 0:
                    que.append(u)
            ans = []        
            while que:
                top = que.popleft()
                ans.append(top)
                for ch in adj[top]:
                    inb[ch] -= 1
                    if inb[ch] == 0:
                        que.append(ch)
            if len(ans) != len(items):
                return [], False

            return ans, True
        go, val = topo(gadj, list(range(lg)))
        if not val:
            return []
        ans = []
        for v in go:
            t, ok = topo(grouping[v], gitems[v])
            if not ok:
                return []
            ans.extend(t)
        return ans
    

    # Ow god I love topo sort