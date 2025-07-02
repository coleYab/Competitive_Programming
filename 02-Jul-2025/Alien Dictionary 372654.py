# Problem: Alien Dictionary - https://practice.geeksforgeeks.org/problems/alien-dictionary/1

#User function Template for python3
from collections import defaultdict, deque

class Solution:
    def findOrder(words):
        n = len(words)
        letters = set()
        adj = defaultdict(set)
        inb = defaultdict(int)
    
        max_len = 0
        for i in range(n):
            max_len = max(max_len, len(words[-1]))
    
    
        inb = defaultdict(int)
        for c in words[0]:
            letters.add(c)
        for i in range(n - 1):
            cur = words[i]
            next = words[i + 1]
            for c in next:
                letters.add(c)
    
            i = 0
            while i < max(len(cur), len(next)):
                if i >= min(len(cur), len(next)):
                    if i < len(cur) and i >= len(next):
                        return ""
                    break
                    
                if cur[i] != next[i]:
                    if next[i] not in adj[cur[i]]:
                        inb[next[i]] += 1
                    adj[cur[i]].add(next[i])
                    break
                i += 1
    
        que = deque()
        for letter in letters:
            if inb[letter] == 0:
                que.append(letter)
     
        vis = set()
        ans = []
        while que:
            node = que.popleft()
            ans.append(node)
            for ch in adj[node]:
                inb[ch] -= 1
                if inb[ch] <= 0:
                    que.append(ch)
        
        if len(ans) != len(letters):
            return ""
    
        return "".join(ans)


